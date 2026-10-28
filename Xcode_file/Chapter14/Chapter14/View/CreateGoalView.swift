//
//  CreateGoalView.swift
//  Chapter14
//
//  Created by Jethro Ming on 2026/7/8.
//

import SwiftUI

struct CreateGoalView: View {
    var goalViewModel: GoalViewModel
    @Environment(\.presentationMode) var presentationMode
    @State var goalText: String = ""
    @State var targetDate: Date = Date()
    
    var body: some View {
        NavigationStack {
            // 主要视图
            VStack {
                goalTextView
                targetDatePickerView
                Spacer()
            }
            .navigationBarItems(leading: closeBtnView, trailing: commitBtnView)
        }
        
    }
    
    // 目标名称
    private var goalTextView: some View {
        TextField("写下你的目标", text: $goalText)
            .padding()
            .background(Color(.systemGray6))
            .cornerRadius(16)
            .padding(.horizontal)
    }
    
    // 达成日期
    private var targetDatePickerView: some View {
        VStack {
            HStack {
                Text("达成日期")
                Spacer()
                Text(targetDate.toString())
            }
            DatePicker("", selection: $targetDate, in: Date()..., displayedComponents: .date)
                .datePickerStyle(.wheel)
        }
        .padding()
        .background(Color(.systemGray6))
        .cornerRadius(16)
        .padding(.horizontal)
    }
    
    // 关闭按钮
    private var closeBtnView: some View {
        Button(action: {
            presentationMode.wrappedValue.dismiss()
        }, label: {
            Image(systemName: "x.circle.fill")
                .font(.title)
                .foregroundStyle(Color(.systemGray3))
        })
    }
    
    // 确认按钮
    private var commitBtnView: some View {
        Button(action: {
            // 新增目标
            goalViewModel.addGoal(goalText: goalText, targetDate: targetDate)
            // 关闭窗口
            presentationMode.wrappedValue.dismiss()
        }, label: {
            Text("确定")
                .bold()
                .foregroundStyle(Color.white)
                .padding(.vertical, 10)
                .padding(.horizontal, 20)
                .background(.green)
                .clipShape(Capsule())
        })
    }
}



#Preview {
    CreateGoalView(goalViewModel: GoalViewModel())
}

