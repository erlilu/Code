//
//  ContentView.swift
//  Chapter6App
//
//  Created by Jethro Ming on 2026/5/23.
//

import SwiftUI

struct ContentView: View {
    @State var isAgree: Bool = false
    
    var body: some View {
        VStack {
            pageImageView
            sloganTextView
            authorizedLoginBtnView
            userAgreementView
        }
        .padding(40)
        .background(Color.bgColor)
    }
    
    //picture of font page
    private var pageImageView: some View {
        VStack {
            Spacer()
            
            Image("image_fontPage")
                .resizable()
                .aspectRatio(contentMode: .fit)
            
            Spacer()
        }
    }

    //slogan words
    private var sloganTextView: some View {
        Text("遇见生活中的美好")
            .font(.title3)
            .bold()
            .foregroundColor(.purple)
    }

    //login + struct
    private var authorizedLoginBtnView: some View {
        VStack(spacing: 10){
            Button(action: {
            }) {
                LoginBtnView(btnName: "微信登录", btnTextColor: .white, btnBackgroundColor: .green)
            }
            
            Button(action: {
            }) {
                LoginBtnView(btnName: "QQ登录", btnTextColor: .white, btnBackgroundColor: .blue)
            }
            
            Button(action: {
            }) {
                LoginBtnView(btnName: "Apple登录", btnTextColor: .white, btnBackgroundColor: .black)
            }
            
            Button(action: {
            }) {
                LoginBtnView(btnName: "手机号登录", btnTextColor: .black, btnBackgroundColor: Color(.systemGray5))
            }
        }
    }

    private var userAgreementView: some View {
        HStack {
            Button(action: {
                self.isAgree.toggle()
            }){
                Image(systemName:isAgree ?"checkmark.circle.fill" : "circle")
                    .foregroundColor(isAgree ? .green : .gray)
            }
            Text("已阅读并同意隐私政策和用户协议")
                .font(.system(size: 14))
                .foregroundColor(.gray)
        }
        .font(.system(size: 14))
        .foregroundColor(.gray)
    }
    
}




#Preview {
    ContentView()
}
