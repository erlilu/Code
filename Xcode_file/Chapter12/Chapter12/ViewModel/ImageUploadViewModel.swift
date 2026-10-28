//
//  ImageUploadViewModel.swift
//  Chapter12
//
//  Created by Jethro Ming on 2026/7/6.
//
import SwiftUI
import Observation
import PhotosUI


@Observable
class ImageUploadViewModel {
    var selectedImage: UIImage? = nil
    var uploadStatus: UploadStatus = .idle
    
    // 你的后端图片上传接口地址（请替换为你的真实 Java/Node 后端地址）
    let uploadURLString = "https://api.yourserver.com/v1/upload"
    
    /// 处理从相机/相册中选中的原始条目
    func processSelectedItem(_ item: PhotosPickerItem?) async {
        guard let item = item else { return }
        
        await MainActor.run { self.uploadStatus = .idle }
        
        do {
            // 将选中的照片安全地加载为二进制数据 (Data)
            if let data = try await item.loadTransferable(type: Data.self),
               let uiImage = UIImage(data: data) {
                
                // 成功转为 UIImage，刷新 UI 展现
                await MainActor.run {
                    self.selectedImage = uiImage
                }
            }
        } catch {
            await MainActor.run {
                self.uploadStatus = .failed(error: "加载图片失败: \(error.localizedDescription)")
            }
        }
    }
    
    /// 执行 HTTP Multipart/Form-Data 上传流程
    func uploadImage() async {
        guard let image = selectedImage else { return }
        // 将图片压缩为 JPEG 二进制流（准备上传）
        guard let imageData = image.jpegData(compressionQuality: 0.8) else { return }
        guard let url = URL(string: uploadURLString) else { return }
        
        await MainActor.run { self.uploadStatus = .uploading(progress: 0.1) }
        
        // 构建标准的表单上传协议 (Multipart Form Data)
        let boundary = "Boundary-\(UUID().uuidString)"
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("multipart/form-data; boundary=\(boundary)", forHTTPHeaderField: "Content-Type")
        
        var body = Data()
        body.append("--\(boundary)\r\n".data(using: .utf8)!)
        body.append("Content-Disposition: form-data; name=\"file\"; filename=\"photo.jpg\"\r\n".data(using: .utf8)!)
        body.append("Content-Type: image/jpeg\r\n\r\n".data(using: .utf8)!)
        body.append(imageData)
        body.append("\r\n--\(boundary)--\r\n".data(using: .utf8)!)
        
        do {
            await MainActor.run { self.uploadStatus = .uploading(progress: 0.5) }
            
            // 使用现代异步网络库发送请求
            let (data, response) = try await URLSession.shared.upload(for: request, from: body)
            
            if let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 {
                await MainActor.run { self.uploadStatus = .success }
                print("服务器返回数据: \(String(data: data, encoding: .utf8) ?? "")")
            } else {
                await MainActor.run { self.uploadStatus = .failed(error: "服务器响应错误") }
            }
        } catch {
            await MainActor.run { self.uploadStatus = .failed(error: error.localizedDescription) }
        }
    }
}
