//
//  ContentView.swift
//  Chapter5App
//
//  Created by Jethro Ming on 2026/5/22.
//

import SwiftUI

struct ContentView: View {
    //info
    let introductionText: String = "Jethro Ming, an independent iOS developer, is a complete novice with absolutely no experience. His ambition is to become an excellent product manager, a super-skilled developer, and achieve financial freedom as soon as possible."
    
    var body: some View {
        //滚动布局容器视图
        ScrollView {
            //MARK: - personal
            //No.1 layout container [VS] ---- information
            VStack (spacing: 32){
                
                //avatar
                Image("avatar")
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .clipShape(Circle())
                    .overlay(
                        Circle()
                            .stroke(Color(.systemRed), lineWidth: 2)
                )
                    .frame(width: 160)
                
                //information
                VStack (spacing: 10){
                    Text("Fugoiky")
                        .font(.title2)
                        .bold()
                    Text("iOS developer")
                        .font(.title3)
                    HStack{
                        Image(systemName: "location.fill")
                            .foregroundColor(.gray)
                        Text("ShangDong")
                            .font(.title3)
                            .foregroundColor(.gray)
                    }
                    
                    // personal introduction
                    Text(introductionText)
                        .foregroundColor(.gray)
                        .padding()
                }
                
            }
            
            Divider()
            
            //MARK: - achievement
            //No.2 layout way []  ---- personal achievement
            HStack{
                VStack(spacing: 10){
                    Text("1280")
                        .font(.title2)
                        .bold()
                    Text("follows")
                        .font(.system(size: 14))
                        .foregroundColor(.gray)
                }
                
                Spacer()
                
                VStack(spacing: 10){
                    Text("25")
                        .font(.title2)
                        .bold()
                    Text("following")
                        .font(.system(size: 14))
                        .foregroundColor(.gray)
                }
                
                Spacer()
                
                VStack(spacing: 10){
                    Text("1384")
                        .font(.title2)
                        .bold()
                    Text("followers")
                        .font(.system(size: 14))
                        .foregroundColor(.gray)
                }
                
                Spacer()
                
                VStack(spacing: 10){
                    Text("1.4w")
                        .font(.title2)
                        .bold()
                    Text("heat")
                        .font(.system(size: 14))
                        .foregroundColor(.gray)
                }
            }
            .padding(.horizontal, 48)
            .padding(.vertical, 20)
            .background(Color(.systemGray6))
            .cornerRadius(16)
            .padding(.horizontal, 20)

            Divider()
            
            //MARK: volumes
            //No.3 layout way [] ---- volumes
            VStack{
                //ForEach 循环遍历
                ForEach(Article.articles, id: \.title) { item in
                    HStack(spacing: 20){
                        //title page
                        Image(item.image)
                            .resizable()
                            .frame(width: 80, height: 80)
                            .cornerRadius(4)
                        
                        //information of books
                        VStack(alignment: .leading){
                            HStack {
                                Text(item.title)
                                    .font(.title2)
                                    .bold()
                                
                                Spacer()
                                
                                Image(systemName: "ellipsis")
                                    .foregroundColor(.gray)
                        }
                            Spacer()
                            
                            HStack(spacing: 20) {
                                Text("\(item.articleNum)"+"篇文章")
                                Text("\(item.subscriptionNum)" + "人订阅")
                            }
                            .foregroundColor(.gray)
                        }
                        
                        Spacer()
                    }
                    .frame(height: 80)
                    .padding(.horizontal)
                }

            }
        }
        
    }
}

#Preview("information") {
    ContentView()
}


