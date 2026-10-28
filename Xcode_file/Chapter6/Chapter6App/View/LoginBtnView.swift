//
//  LoginBtnView.swift
//  Chapter6App
//
//  Created by Jethro Ming on 2026/5/24.
//

import Foundation
import SwiftUI

//快捷登录的结构体，单独为文件
struct LoginBtnView: View {
    var btnName: String
    var btnTextColor: Color
    var btnBackgroundColor: Color
    
    var body: some View {
        Text(btnName)
            .foregroundColor(btnTextColor)
            .frame(maxWidth: .infinity, maxHeight: 48)
            .background(btnBackgroundColor)
            .cornerRadius(8)
    }
}
