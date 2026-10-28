//
//  ContentView.swift
//  Chapter11
//
//  Created by Jethro Ming on 2026/7/3.
//

import SwiftUI

struct ContentView: View {
    //参数声明
//    @State var historyDaily: [HistoryDaily] = [
//        HistoryDaily(id: 1, year: 2017, body: "教育部颁布新修订的《普通高等学校学生管理规定》并开始施行。"),
//        HistoryDaily(id: 2, year: 2011, body: "我国个税起征点从2000元上调到3500元"),
//        HistoryDaily(id: 3, year: 2008, body: "全国范围内全面免除城市义务教育阶段学生学杂费。"),
//        HistoryDaily(id: 4, year: 1996, body: "《中华人民共和国职业教育法》正式施行。"),
//    ]
    
    //引入ViewModel
    @State var viewModel = ViewModel()
    
    
    var body: some View {
        //视图
        NavigationStack {
            ScrollView {
                ForEach(viewModel.historyDaily, id: \.id) { item in
                    TextItem(id: item.id, year: item.year, text: item.body)
                    
                }
            }
            .navigationTitle("历史上的今天")
        }
        .onAppear(perform: {
            viewModel.fetchTodayInHistory()
        })
    }
}

//TextItem 视图
struct TextItem: View {
    var id: Int
    var year: Int
    var text: String
    var body: some View {
        HStack(spacing: 10) {
            Text(String(year))
                .frame(maxWidth: 80, maxHeight: 120)
                .background(Color(.systemGray6))
                .clipShape(ConcentricRectangle(corners: 8))
            Text(text)
                .multilineTextAlignment(.leading)
                .frame(maxWidth: .infinity, minHeight: 80)
                .padding(.horizontal)
                .background(Color(.systemGray6))
                .clipShape(ConcentricRectangle(corners: 8))
                .lineLimit(2)
        }
        .padding(.horizontal)
    }
}

#Preview {
    ContentView()
}
