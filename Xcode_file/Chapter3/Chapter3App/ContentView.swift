//
//  ContentView.swift
//  Chapter3App
//
//  Created by Jethro Ming on 2026/5/15.
//

import SwiftUI

struct ContentView: View {
    @State var isStarted: Bool = false
    @State var isPaused: Bool = false
    
    
    var body: some View {
        // 嵌套到VStack里面，老版本视图首先展示基于容器视图
        VStack{
            if isPaused {
                //新版本可以先试目标逻辑
                HStack {
                    Button("stop!"){
                        self.isStarted = false
                        self.isPaused = false
                    }
                    .buttonStyle(CustomButtonStyle(backgroundColor: .red))
                    
                    Button("continue..."){
                        self.isPaused = false
                    }
                    .buttonStyle(CustomButtonStyle(backgroundColor: .green))
                    .transition(.asymmetric(insertion: .slide, removal: .scale))  //asymmetric非对称转场
                }
            } else {
                Button(isStarted ? "paused" : "start~"){
                    //显性动画,配合动画方式监听值进行动画
                    withAnimation {
                        if !isStarted {
                            self.isStarted = true
                        } else {
                            self.isPaused = true
                        }
                    }
                }
                .buttonStyle(CustomButtonStyle(backgroundColor: .blue))
                //转场动画，默认、透明过度、缩放、滑动等
                .transition(.scale.combined(with: .slide))  //combined进行组合
                
                
            }
            
        }
        //隐形动画方式
        .animation(.easeInOut(duration: 0.3), value: isPaused)
        .animation(.spring(), value: isStarted)

    }
}





// 自定义按钮样式
struct CustomButtonStyle: ButtonStyle {
    var backgroundColor: Color
    
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.system(size: 20))
            .foregroundColor(.white)
            .padding(.horizontal, 32)
            .padding(.vertical, 10)
            .background(backgroundColor)
            .cornerRadius(8)
    }
}


#Preview {
    ContentView()
}
