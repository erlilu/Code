//
//  ContentView.swift
//  Chapter8App
//
//  Created by Jethro Ming on 2026/5/27.
//

import SwiftUI

struct ContentView: View {
    //参数声明
    @State private var height: Float = 177
    @State private var weight: Float = 54
    @State private var showBMIResultView: Bool = false
    @State private var bmiNum: Float = 0
    @State private var bmiResult: String = "正常"
    @State private var bmiColor: Color = Color.green
    
    
    var body: some View {
        NavigationStack{
            ZStack(alignment: .bottom){
                inputFormView
                
                VStack(spacing: 48) {
                    bmiReferenceView
                    computeBtnView
                }
            }
            .navigationTitle("BMI计算器")
            .navigationBarTitleDisplayMode(.inline)
            //MARK: 导航跳转路径
            .navigationDestination(isPresented: $showBMIResultView) {
                BMIResultView(height: height, weight: weight, bmiNum: bmiNum, bmiResult: bmiResult, bmicolor: bmiColor)
                }
        }
        
    }
    
    //信息录入
    private var inputFormView: some View {
        Form {
            LabeledContent("身高(cm)") {
                TextField("请输入：", value: $height, format: .number)
                    .foregroundStyle(Color(.green))
            }
            
            LabeledContent("体重(kg)") {
                TextField("请输入：", value: $weight, format: .number)
                    .foregroundStyle(Color(.green))
            }
        }
        .multilineTextAlignment(.trailing)
        
    }
    
    
    //参考标准
    private var bmiReferenceView: some View {
        VStack(spacing: 20) {
            HStack {
                Image(systemName: "paperplane")
                Text("参考标准")
                    .font(.title)
                    .bold()
            }
            
            BMIReferenceItemView(bmiColor: Color.blue, bmiResult: "过轻", bmiScope: "BMI<=18.5")
            BMIReferenceItemView(bmiColor: Color.green, bmiResult: "正常", bmiScope: "18.5<BMI<=24")
            BMIReferenceItemView(bmiColor: Color.yellow, bmiResult: "过重", bmiScope: "24<BMI<=28")
            BMIReferenceItemView(bmiColor: Color.orange, bmiResult: "肥胖", bmiScope: "28<BMI<=32")
            BMIReferenceItemView(bmiColor: Color.red, bmiResult: "重度肥胖", bmiScope: "BMI>32")
        }
        .padding()
        .background(Color.white)
        .clipShape(RoundedRectangle(cornerRadius: 16))
        .padding(.horizontal)
    }
    
    
    //计算按钮
    private var computeBtnView: some View {
        Button(action: {
            computerBMI()
            self.showBMIResultView.toggle()
        }) {
            Text("立即计算")
                .font(.system(size: 17))
                .foregroundStyle(Color.white)
                .frame(maxWidth: .infinity, maxHeight: 48)
                .background(Color.green)
                .clipShape(RoundedRectangle(cornerRadius: 16))
                .padding(.horizontal)
        }
    }
    
    
    //BMI计算方法
    func computerBMI() {
        let squaredHeight = (height / 100) * (height / 100)
        bmiNum = weight / squaredHeight
        updateBMIResult()
    }
    
    //更新BMI结果
    func updateBMIResult() {
        switch bmiNum {
        case ...18.5:
            bmiResult = "过轻"
            bmiColor = Color.blue
        case 18.5 ..< 24:
            bmiResult = "正常"
            bmiColor = Color.green
        case 24 ..< 28:
            bmiResult = "过重"
            bmiColor = Color.yellow
        case 28 ..< 32:
            bmiResult = "肥胖"
            bmiColor = Color.orange
        default:
            bmiResult = "重度肥胖"
            bmiColor = Color.red
        }
    }
    
}

    


//参考标准-结构体
struct BMIReferenceItemView: View {
    var bmiColor: Color
    var bmiResult: String
    var bmiScope: String
    
    var body: some View {
        HStack(spacing: 20){
            // 色块
            Rectangle()
                .fill(bmiColor)
                .frame(width: 60, height: 20)
                .presentationCornerRadius(4)
            
            // 参考结果
            Text(bmiResult)
                .foregroundStyle(Color(bmiColor))
            
            Spacer()
            
            // BMI范围
            Text(bmiScope)
        }
    }
}

#Preview {
    ContentView()
}
