//
//  ContentView.swift
//  Chapter10
//
//  Created by Jethro Ming on 2026/6/16.
//

import SwiftUI

struct ContentView: View {
    //参数声明
    let imageURL: String = "https://inews.gtimg.com/om_bt/O7nc-IEY_oP93FRGtx3cQgvX2QE3oNA2vRkDOmGcKtN2cAA/1000"
    @State private var imageID: UUID = UUID()
    
    var body: some View {
        VStack (spacing: 20) {
            webImageView
                .id(imageID)
            refreshBtnView
        }
        
    }
    
    
    
    //网络图片视图
    private var webImageView: some View {
        //显示图片
        AsyncImage(url: URL(string: imageURL)) { phase in
            switch phase {
            //step 1 返回为emoty空
            case .empty:
                ProgressView()    //正在加载
            //step 2 返回success正确
            case .success(let image):
                image
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .clipShape(RoundedRectangle(cornerRadius: 8))
                    .padding()
            //step 3 返回failure错误
            case .failure(_):  //加入_
                Text("加载失败......")
            //step 4 返回"@unknown default"其他状态
            @unknown default:
                EmptyView()
            }
        }
    }
    
    
    // 刷新按钮视图
    private var refreshBtnView: some View {
        Button (action: {
            self.imageID = UUID() //重构ID
        }, label: {
            HStack {
                Image(systemName: "gobackward")
                Text("重新加载")
            }
            .foregroundStyle(.white)
            .padding()
            .background(.green)
            .clipShape(RoundedRectangle(cornerRadius: 8))
            .padding()
        })
        
    }
    
    
}

#Preview {
    ContentView()
}
