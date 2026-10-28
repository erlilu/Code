//
//  ContentView.swift
//  Chapter14
//
//  Created by Jethro Ming on 2026/7/8.
//

import SwiftUI

struct ContentView: View {
    var goalViewModel: GoalViewModel
    
    @State var showCreateGoalView: Bool = false
    let sheetHeight = Utils.screenHeigt * 2 / 3
    
    var body: some View {
        ZStack {
            Color(.systemGray6).ignoresSafeArea(edges: .all)
            goalCardListView
        }
        // 界面显示时
        .onAppear() {
            goalViewModel.fetchGoals()
        }
        .sheet(isPresented: $showCreateGoalView) {
            CreateGoalView(goalViewModel: GoalViewModel())
                .presentationDetents([.height(sheetHeight)])
        }
    }
    
    
    // 界面标题&新增操作
    private var topBarView: some View {
        HStack {
            Text("目标人生")
                .font(.title)
                .bold()
            Spacer()
            Button(action: {
                self.showCreateGoalView.toggle()
            }, label: {
                Label("新增", systemImage: "plus")
                    .foregroundStyle(Color.white)
                    .bold()
                    .padding()
                    .background(.black)
                    .clipShape(Capsule())
            })
        }
        .padding(.horizontal)
    }
    
    // 目标卡片列表
    private var goalCardListView: some View {
        TabView {
            ForEach(goalViewModel.goals) { goal in
                GoalCardView(goalText: goal.goalText ?? "", targetDate: goal.targetDate ?? Date(), currentProgress: Int(goal.currentProgress))
            }
        }
        .tabViewStyle(PageTabViewStyle())
        .indexViewStyle(PageIndexViewStyle(backgroundDisplayMode: .always))
    }
    
}


// 目标卡片
struct GoalCardView: View {
    var goalText: String
    var targetDate: Date
    var currentProgress: Int
    
    var body: some View {
        VStack(spacing: 48) {
            VStack(spacing: 20){
                goalTextView
                targetDateView
                untilTargetDaysView
            }
            subjectImageView
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(.white)
        .cornerRadius(16)
        .padding()
        
    }
    // 目标
    private var goalTextView: some View {
        Text(goalText)
            .font(.system(size: 28))
            .bold()
            .lineLimit(1)
    }
    // 达成日期
    private var targetDateView: some View {
        Label(targetDate.toString() + "前", systemImage: "calendar")
            .foregroundStyle(Color.gray)
    }
    // 剩余天数
    private var untilTargetDaysView: some View {
        Text("剩余" + "\(Date().daysUntilDate(targetDate))" + "天")
            .foregroundStyle(Color.white)
            .bold()
            .padding()
            .background(.orange)
            .clipShape(Capsule())
    }
    // 主题图片
    private var subjectImageView: some View {
        Image("onboarding1")
            .resizable()
            .aspectRatio(contentMode: .fit)
            .frame(height: 320)
    }
}



#Preview {
    ContentView(goalViewModel: GoalViewModel())
}
