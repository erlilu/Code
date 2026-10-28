//
//  NextNoteView.swift
//  Chapter7App
//
//  Created by Jethro Ming on 2026/5/24.
//

import Foundation
import SwiftUI
 
//搭建“新增笔记”界面 -- Text Field
struct NextNoteView: View {
    //参数声明
    @State private var inputText: String = ""
    @Binding var showNewNoteView: Bool
    @Binding var notes: [Note]
    
    //显示文本框
    var body: some View {
        VStack(spacing: 20){
            HStack{
                closeBtnView
                Spacer()
                submitBtnView
            }
            .padding(.horizontal)
            inputTextView
            Spacer()
        }
    }
    
    
    
    
    //文本框
    private var inputTextView: some View {
        TextField("请输入", text: $inputText)
            .textFieldStyle(RoundedBorderTextFieldStyle())
            .padding(.horizontal)
    }
    
    
    //关闭按钮
    private var closeBtnView: some View {
        Button(action: {
            self.showNewNoteView.toggle()
        }) {
            Image(systemName: "chevron.down.circle.fill")
                .font(.system(size: 28))
                .foregroundColor(Color(.systemGray3))
        }
    }
    
    //完成按钮
    private var submitBtnView: some View {
        Button(action: {
            self.showNewNoteView.toggle()
            self.notes.append(Note(noteContent: inputText))
        }){
            Text("完成")
                .font(.system(size: 17))
                .foregroundColor(.white)
                .padding(.all, 8)
                .background(.green)
                .cornerRadius(8)
        }
    }
}


#Preview {
    //预览默认设置
    NextNoteView(showNewNoteView: .constant(false), notes: .constant([]))
}
