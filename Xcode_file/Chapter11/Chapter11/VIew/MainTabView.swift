//
//  MainTabView.swift
//  Chapter11
//
//  Created by Jethro Ming on 2026/7/4.
//

import SwiftUI

struct MainTabView: View {
    var body: some View{
        
        TabView {
            ContentView()
                .tabItem {
                    Image(systemName: "house")
                    Text("首页")
                }
            
            CalendarView()
                .tabItem {
                    Image(systemName: "calendar")
                    Text("日历")
                }
            
            ProfileView()
                .tabItem {
                    Image(systemName: "person")
                    Text("我的")
                }
        }
    }
}

#Preview {
    MainTabView()
}

