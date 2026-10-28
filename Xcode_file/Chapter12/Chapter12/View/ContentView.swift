//
//  ContentView.swift
//  Chapter12
//
//  Created by Jethro Ming on 2026/7/5.
//

import SwiftUI

struct ContentView: View {
    // 引入FaceIDAuthManager
    var faceIDAuthManager = FaceIdAuthManager()
    
    var body: some View {
        NavigationStack {
            ZStack {
                Color(.systemGray6).ignoresSafeArea(edges: .all)
                
                VStack(spacing: 20) {
                    ColumnCardView(title: "人脸识别", desc: "识别你的身份", columnImage: "camera")
                        // 调用身份认证方法
                        .onTapGesture {
                            if !faceIDAuthManager.isFaceIDAuthenticated {
                                // 调用识别函数
                                faceIDAuthManager.authenticiateWithFaceID()
                            }
                        }
                    ColumnCardView(title: "身份证正面", desc: "上传身份证人像面", columnImage: "portrait")
                    ColumnCardView(title: "身份证反面", desc: "上传身份证国徽面", columnImage: "backSide")
                    
                    Spacer()
                }
                .padding()
            }
            .navigationTitle("身份认证")
            .navigationBarTitleDisplayMode(.inline)
        }
    }
}

#Preview {
    ContentView()
}
