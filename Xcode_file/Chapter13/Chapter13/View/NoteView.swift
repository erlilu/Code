//
//  NoteView.swift
//  Chapter13
//
//  Created by Jethro Ming on 2026/7/6.
//

import SwiftUI

struct NoteView: View {
    // 声明共享对象
    @State var viewModel = ViewModel()
    
    var body: some View {
        ZStack {
            Color(.systemGray6).ignoresSafeArea(edges: .all)
//            NoteCard(sentence: "this is a sentence.", create_time: "2026.07.06")
            // 判断逻辑
            if viewModel.sentenceModel.isEmpty {
                defaultImageView
            } else {
                noteCardList
            }
        }
    }
    
    
    // 笔记列表
    private var noteCardList: some View {
        ScrollView {
            ForEach(viewModel.sentenceModel) { item in
                NoteCard(sentence: item.sentence, create_time: item.create_time)
                    .contextMenu {
                        Button("delete") {
                            viewModel.deleteNote(id: item.id)
                        }
                    }
            }
        }
    }
    
    
    // 默认图
    private var defaultImageView: some View {
        Image("david-underland-oH6Pfg6uMOE-unsplash")
            .resizable()
            .aspectRatio(contentMode: .fill)
            .frame(width: 200, height: 200)
    }
    
}


// 笔记卡片
struct NoteCard: View {
    var sentence: String
    var create_time: String
    
    var body: some View {
        HStack {
            VStack {
                Text(sentence)
                    .lineLimit(2)
                Spacer()
                Text(create_time)
                    .foregroundStyle(Color.gray)
            }
            Spacer()
        }
        .frame(maxWidth: .infinity, minHeight: 60, maxHeight: 80)
        .padding()
        .background(.white)
        .cornerRadius(16)
        .padding(.horizontal)
    }
}

#Preview {
    NoteView()
        .environment(ViewModel())
}
