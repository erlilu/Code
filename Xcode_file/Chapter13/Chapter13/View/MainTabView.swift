//
//  MainTabView.swift
//  Chapter13
//
//  搭建底部导航栏
//  Created by Jethro Ming on 2026/7/6.
//

import SwiftUI

struct MainTabView: View {
    // 设置视图背景色
    init() {
        UITabBar.appearance().backgroundColor = UIColor(.white)
    }
    
    var body: some View {
        TabView {
            ContentView()
                .tabItem {
                    Label("推荐", systemImage: "square.filled.on.square")
                }
            NoteView()
                .tabItem {
                    Label("笔记", systemImage: "note.text")
                }
        }
    }
}


#Preview {
    MainTabView()
        .environment(ViewModel())
}
