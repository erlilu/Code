//
//  BMIResultView.swift
//  Chapter8App
//
//  Created by Jethro Ming on 2026/5/28.
//

import Foundation
import SwiftUI

struct BMIResultView: View {
    var body: some View {
        VStack{
            computerResultView
            Spacer()
            reComputerBtnView
        }
        .navigationBarHidden(true)
    }
    
    //参数声明
    var height: Float
    var weight: Float
    var bmiNum: Float
    var bmiResult: String
    var bmicolor: Color
    
    //声明环境变量
    @Environment(\.dismiss) var dissmiss
    
    //计算结果 + 参数赋值
    private var computerResultView: some View {
        VStack(spacing: 28) {
            Text("你的BMI是")
                .font(.system(size: 17))
                .foregroundStyle(Color.gray)
            
            Text(String(format: "%.2f", bmiNum))
                .font(.system(size: 48))
                .bold()
                .foregroundStyle(Color.green)
            
            Text(bmiResult)
                .font(.system(size: 23))
                .bold()
                .padding(.vertical, 6)
                .padding(.horizontal, 30)
                .background(bmicolor)
                .clipShape(RoundedRectangle(cornerRadius: 32, ))
            
            
            HStack{
                Text(String(format: "%.0f", height))
                Text("|")
                Text(String(format: "%.0f", weight))
            }
            .font(.system(size: 17))
            .foregroundStyle(Color.gray)
        }
        .padding()
        .frame(maxWidth: .infinity)
        .background(Color(.systemGray6))
        .clipShape(RoundedRectangle(cornerRadius: 16))
        .padding()
    }
    
    //重新计算按钮
    private var reComputerBtnView: some View {
        Button(action: {
            dissmiss()
        }) {
            HStack {
                Image(systemName: "gobackward")
                Text("重新计算")
            }
            .font(.system(size: 17))
            .foregroundStyle(Color.white)
            .frame(width: 200, height: 48)
            .background(Color.blue)
            .clipShape(RoundedRectangle(cornerRadius: 8))
            .padding(.horizontal)
        }
    }
    
}


//赋值预览
#Preview {
    BMIResultView(height: 175, weight: 65, bmiNum: 21.22, bmiResult: "正常", bmicolor: Color.green)
}
