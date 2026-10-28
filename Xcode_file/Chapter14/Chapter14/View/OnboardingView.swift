//
//  OnboardingView.swift
//  Chapter14
//
//  Created by Jethro Ming on 2026/7/8.
//

import SwiftUI



// 功能卡片
struct OnboardingView: View {
    @State var showCreateGoalView: Bool = false
    let sheetHeight = Utils.screenHeigt * 2 / 3
    
    var body: some View {
        VStack {
            tabPageView
            startBtnView
        }
        .sheet(isPresented: $showCreateGoalView) {
            CreateGoalView(goalViewModel: GoalViewModel())
                .presentationDetents([.height(sheetHeight)])  // 弹窗高度
        }
        
    }
    
    
    // 轮播卡片
    private var tabPageView: some View {
        TabView {
            OnboardingPageView(imageName: "onboarding1", title: "目标打卡", description: "看见每一天的改变")
            OnboardingPageView(imageName: "onboarding2", title: "每日计划", description: "养成自律好习惯")
            OnboardingPageView(imageName: "onboarding3", title: "自我管理", description: "认真对待每一个目标")
            OnboardingPageView(imageName: "onboarding4", title: "付诸行动", description: "聚焦你的目标")
            OnboardingPageView(imageName: "onboarding5", title: "重启人生", description: "成为更好的自己")
        }
        .tabViewStyle(PageTabViewStyle())
        .indexViewStyle(PageIndexViewStyle(backgroundDisplayMode: .always))
    }
    
    
    // 开始使用按钮
    private var startBtnView: some View {
        Button(action: {
            self.showCreateGoalView.toggle()
        }, label: {
            Label("开始使用", systemImage: "paperplane")
                .foregroundStyle(Color.white)
                .bold()
                .frame(width: 150, height: 50)
                .background(.green)
                .clipShape(Capsule())
        })
    }
}




// 功能卡片
struct OnboardingPageView: View {
    var imageName: String
    var title: String
    var description: String
    
    var body: some View {
        VStack(spacing: 32) {
            Image(imageName)
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(height: 320)
            
            VStack(spacing: 15) {
                Text(title)
                    .font(.title)
                    .bold()
                Text(description)
                    .font(.title2)
                    .multilineTextAlignment(.center)
                    .foregroundStyle(Color.gray)
            }
        }
    }
}

#Preview {
    OnboardingView()
}
