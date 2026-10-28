//
//  ContentView.swift
//  Chapter2App
//
//  Created by Jethro Ming on 2026/5/15.
//

import SwiftUI

struct ContentView: View {
    let sentences = [
        "没有奇迹，只有你努力的痕迹；没有运气，只有你坚持的勇气。",
        "生活原本沉闷，但跑起来就有风，每一步都在铺就未来的路 。",
        "人生不必急于求成，默默沉淀慢慢深耕，时光从不辜负坚持的人 。",
        "那些打不倒你的，终将使你更强大，熬过低谷自会惊艳时光 。",
        "每天早晨提醒自己，生命短暂而美好，没时间纠结，没时间计较 。",
        "不怕慢，只怕站。每一步前行，都是向着梦想的迈进，坚持就是胜利的开始。",
    ]
    
    let images = [
        "chapter02App-01",
        "chapter02App-02",
        "chapter02App-03",
    ]
    
    @State var sentence : String = ""
    @State var image : String = ""
    var body: some View {
        ZStack {
            Image(image)
                .resizable()
                .aspectRatio(contentMode: .fill)
                .ignoresSafeArea()
            Text(sentence)
                .foregroundStyle(.white)
        }
        //.padding()
        //视图显示时
        .onAppear(perform: {
            self.image = images.randomElement() ?? ""
        })
        .onAppear(perform: {
            self.sentence = sentences.randomElement() ?? ""
        })
    }
}

#Preview {
    ContentView()
}
