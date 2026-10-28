//
//  ContentView.swift
//  Chapter7App
//
//  Created by Jethro Ming on 2026/5/24.
//

import SwiftUI

struct ContentView: View {
    @State private var notes = Note.notes
    @State private var showNewNoteView: Bool = false
    
    var body: some View {
        ZStack(alignment: .bottomTrailing){
            VStack {
                noteTitleView
                noteListView
            }
            addBtnView
        }
        //打开弹窗功能
        .sheet(isPresented: $showNewNoteView){
            NextNoteView(showNewNoteView: $showNewNoteView, notes: $notes) //参数绑定
                .presentationDetents([.medium]) //弹到中间
        }
    }
    
    
    
    //Note list view 笔记列表
    private var noteListView: some View {
        List($notes, editActions: .all) { $note in
            Text(note.noteContent)
        }
        .listStyle(.plain)
    }
    
    
    //title of interface 页面标题
    private var noteTitleView: some View {
        Text("Note 笔记")
            .font(.title)
            .bold()
    }
    
    
    //add button 新增按钮
    private var addBtnView: some View {
        Button(action: {
            self.showNewNoteView.toggle()
        }) {
            Image(systemName: "plus.circle.fill")
                .font(.system(size: 48))
                .padding(.horizontal)
        }
    }
    
}

#Preview {
    ContentView()
}
