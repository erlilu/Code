//
//  ContentView.swift
//  Chapter4App
//
//  Created by Jethro Ming on 2026/5/19.
//

import SwiftUI

// contenView 为View视图
struct ContentView: View {
    // body中有多个修饰符修饰，故用some View.本质：一种不透明类型
    var body: some View {
        VStack(spacing: 60) {
            //关闭按钮
            HStack {
                Spacer()
                systemImageView
            }
            .padding(.horizontal)
            
            //主要内容
            VStack(spacing: 32) {
                imageView
                textView
            }
        }
        .padding(.vertical, 32)
        .frame(maxWidth: .infinity)
        .background(Color(.systemGray6))
        .cornerRadius(16)
        .padding()
    }
    
    //图标
//    private var imageView: some View{
//        Image(systemName: "globe")
//            .imageScale(.large)
//            .foregroundColor(.accentColor)
//    }
    
    private var imageView: some View {
        Image("chapter02App-03")
            .resizable()
            .aspectRatio(contentMode: .fit)
            .frame(width: 200)
            .cornerRadius(16)
    }
    
    //文字
    private var textView: some View{
        Button (action: {
            //单击后操作
        }) {
            Text("立即订阅")
                .font(.system(size: 17))
                .bold()
                .foregroundColor(Color.white)
                .frame(width: 120, height: 40)
                .background(Color.green)
                .cornerRadius(32)
            }
        }
        
    
    //图标
    private var systemImageView: some View {
        Button(action :{
            //单击后操作
        }) {
            Image(systemName: "xmark.circle.fill")
                .font(.system(size: 23)) //系统字体，字号23
                .foregroundColor(.gray)
            }
        }
        
}



#Preview {
    ContentView()
}
