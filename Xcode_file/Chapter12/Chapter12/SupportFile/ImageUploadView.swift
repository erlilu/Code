//
//  ImageUploadView.swift
//  Chapter12
//
//  实现拍照和图片上传
//  Created by Jethro Ming on 2026/7/6.
//

import SwiftUI

struct ImageUploadView: View {
    @State private var viewModel = ImageUploadViewModel()
    @State private var pickerItem: PhotosPickerItem? = nil // 绑定选择器的核心对象
    
    var body: some View {
        NavigationStack {
            VStack(spacing: 25) {
                // 图片预览区
                ZStack {
                    RoundedRectangle(cornerRadius: 16)
                        .fill(Color(.systemGray6))
                        .frame(height: 260)
                    
                    if let image = viewModel.selectedImage {
                        Image(uiImage: image)
                            .resizable()
                            .scaledToFill()
                            .frame(height: 260)
                            .clipShape(RoundedRectangle(cornerRadius: 16))
                    } else {
                        VStack(spacing: 12) {
                            Image(systemName: "photo.badge.plus")
                                .font(.largeTitle)
                                .foregroundStyle(.secondary)
                            Text("未选择照片")
                                .font(.subheadline)
                                .foregroundStyle(.secondary)
                        }
                    }
                }
                .padding(.horizontal)
                
                // 按钮控制区
                VStack(spacing: 12) {
                    // 🌟 苹果新封装的多合一选择器：同时支持相册浏览和实时相机拍摄
                    PhotosPicker(
                        selection: $pickerItem,
                        matching: .images, // 只筛选图片
                        preferredItemEncoding: .automatic
                    ) {
                        Label("拍照或从相册选择", systemImage: "camera.fill")
                            .font(.headline)
                            .frame(maxWidth: .infinity)
                            .padding()
                            .background(Color.blue)
                            .foregroundStyle(.white)
                            .clipShape(RoundedRectangle(cornerRadius: 12))
                    }
                    
                    // 上传到服务器按钮
                    if viewModel.selectedImage != nil {
                        Button(action: {
                            Task { await viewModel.uploadImage() }
                        }) {
                            Label("上传图片到服务器", systemImage: "cloud.sun.fill")
                                .font(.headline)
                                .frame(maxWidth: .infinity)
                                .padding()
                                .background(Color.green)
                                .foregroundStyle(.white)
                                .clipShape(RoundedRectangle(cornerRadius: 12))
                        }
                        .disabled(isUploading) // 上传中禁用按钮
                    }
                }
                .padding(.horizontal)
                
                // 状态提示区
                statusView
                
                Spacer()
            }
            .navigationTitle("发布动态")
            // 🌟 核心绑定：当系统选择器(相机或相册)返回结果后，立刻异步解析图片
            .onChange(of: pickerItem) { _, newItem in
                Task {
                    await viewModel.processSelectedItem(newItem)
                }
            }
        }
    }
    
    // 计算属性：判断是否在上传中
    private var isUploading: Bool {
        if case .uploading = viewModel.uploadStatus { return true }
        return false
    }
    
    // 渲染动态状态面板
    @ViewBuilder
    private var statusView: some View {
        switch viewModel.uploadStatus {
        case .idle:
            EmptyView()
        case .uploading(let progress):
            VStack {
                ProgressView(value: progress)
                    .progressViewStyle(.linear)
                Text("正在发送给服务器...")
                    .font(.caption)
                    .foregroundStyle(.secondary)
            }
            .padding()
        case .success:
            Label("图片上传成功！", systemImage: "checkmark.circle.fill")
                .foregroundStyle(.green)
                .font(.subheadline)
        case .failed(let error):
            Label("上传失败: \(error)", systemImage: "exclamationmark.triangle.fill")
                .foregroundStyle(.red)
                .font(.subheadline)
        }
    }
}

#Preview {
    ImageUploadView()
}
