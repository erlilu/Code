//
//  WebImageVIew.swift
//  Chapter10
//
//  Created by Jethro Ming on 2026/6/28.
//

import SwiftUI

struct WebImageVIew: View {
    //参数声明
    @State private var image: UIImage? = nil
    let imageURL: String = "https://inews.gtimg.com/om_bt/O7nc-IEY_oP93FRGtx3cQgvX2QE3oNA2vRkDOmGcKtN2cAA/1000"
   
    
    
    var body: some View {
        VStack {
            if let image = image {
                webImageView(image: image)
            } else {
                emptyImageView
            }
        }
        // 方法调用
        .onAppear(perform: loadImage)
    }
    
    // MARK: 网络请求方法
    func loadImage() {
        let session = URLSession(configuration: .default)
        
        let task = session.dataTask(with: URL(string: imageURL)!) {
            //配置task的参数：接收下载的数据内容、存储请求响应信息、存储请求过程中的错误信息
            data, response, error in
            if let httpResponse = response as? HTTPURLResponse {
                //获取HTTP状态码
                let statusCode = httpResponse.statusCode
                
                if statusCode == 200, let data = data, let fetchedImage = UIImage(data: data) {
                    //成功获取图片数据
                    DispatchQueue.main.async {
                        self.image = fetchedImage
                    }
                } else {
                    //处理HTTP状态码错误或数据为空
                    print("HTTP状态码错误:\(statusCode)")
                }
            } else if let error = error {
                //处理网络请求错误
                print("错误信息:\(error.localizedDescription)")
            } else {
                //位置错误或数据为空
                print("未知错误")
            }
        }
        task.resume()
    }
    
    // WebImageView 视图
    func webImageView(image: UIImage) -> some View {
        Image(uiImage: image)
            .resizable()
            .aspectRatio(contentMode: .fit)
            .clipShape(ConcentricRectangle(corners: 8))
            .padding()
    }
    
    
    // 默认视图
    private var emptyImageView: some View {
        VStack(spacing: 20) {
            ProgressView()
            Text("加载中...")
        }
    }
    
    
}

#Preview {
    WebImageVIew()
}
