//
//  ContentView.swift
//  Chapter13
//
//  Created by Jethro Ming on 2026/7/6.
//

import SwiftUI

struct ContentView: View {
    
    @State var viewModel = ViewModel()
    
    @State var sentences: [(Color, String)] = [
        (.red, "‌温柔要有，但不是妥协，我们要在安静中，不慌不忙的坚强‌。"),
        (.green, "‌生活就是做出选择，一旦你做出了你的选择，你就必须活在你的决定中‌。"),
        (.blue, "‌过去的一天能不翻就不要翻，翻落了灰尘会迷了双眼‌。‌‌‌"),
        (.pink, "‌一弯新月宛如一叶小舟，翘着尖尖的船头，在深夜的静湖中划行‌。"),
        (.purple, "‌阳光如同金色的丝线，透过树叶的缝隙，洒在地面上，织就了一幅斑驳的画卷‌。")
    ]
    
    @State private var selectedTabIndex = 0
    @State private var sentence: String = ""
    
    var body: some View {
        ZStack {
            Color(.systemGray6).ignoresSafeArea(edges: .all)
            VStack{
                Text(sentence)
                slideCard
                copyBtnView
            }
        }
        // 视图显示时
        .onAppear(){
            sentence = sentences[selectedTabIndex].1
        }
    }
    
    
    // 滑动卡片
    private var slideCard: some View {
        // 参数绑定
        TabView(selection: $selectedTabIndex) {
                ForEach(0 ..< sentences.count, id: \.self) { index in
                    TextCard(bgColor: sentences[index].0, text: sentences[index].1)
                }
            }
            .tabViewStyle(PageTabViewStyle(indexDisplayMode: .never))
            .frame(height: UIScreen.main.bounds.height / 3)
            .onChange(of: selectedTabIndex) { _, newIndex in
                sentence = sentences[newIndex].1
            }
       
    }

    
    // 收藏按钮
    private var copyBtnView: some View {
        Button(action: {
            viewModel.addNote(sentence: sentence)
        }, label: {
            Label("收藏", systemImage: "square.filled.on.square")
                .bold()
                .foregroundStyle(Color.white)
                .padding(.vertical)
                .padding(.horizontal, 48)
                .background(.green)
                .cornerRadius(16)
        })
    }
}


// 文字卡片
struct TextCard: View {
    var bgColor: Color
    var text: String
    
    var body: some View {
            ZStack {
                Rectangle()
                    .fill(bgColor)
                    .cornerRadius(16)
                    .opacity(0.5)
                
                Text(text)
                    .font(.system(size: 20))
                    .foregroundStyle(Color.white)
                    .padding(32)
            }
            .frame(height: UIScreen.main.bounds.height / 3)
            .padding()
        }
    
}



#Preview {
    ContentView()
        .environment(ViewModel())
}
