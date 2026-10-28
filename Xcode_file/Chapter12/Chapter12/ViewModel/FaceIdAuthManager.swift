//
//  FaceIdAuthManager.swift
//  Chapter12
//
//  Created by Jethro Ming on 2026/7/5.
//

import SwiftUI
import LocalAuthentication      // 生物识别框架
import Observation      // 现代响应式框架，使用 @Observable 宏生效


// 实现FaceID认证方法
// 一旦属性改变，任何绑定它的 swiftUI 界面都会自动刷新
@Observable
class FaceIdAuthManager {
    var isFaceIDAuthenticated = false
    // 可选类型的字符串，默认没有错误nil
    var authErrorDescription: String? = nil // 1. 用于界面上显示错误信息
    
    // MARK: 定义认证主函数
    func authenticiateWithFaceID() {
        // 每次生物识别，都必须实例化一个上下文对象来管理这次认证的生命周期
        let context = LAContext()  // Local Authentication Context 时生物识别的大管家
        var error: NSError?
        
        // 检查设备是否支持生物识别（硬件支持且用户开启了）
        if context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &error) {   //&error
            let reason = "使用FaceID进行认证。"
            
            // 2. 调用具体的识别方法 evaluatePolicy 的真正拉起系统的面容扫描弹窗。回调是在后台子线程执行的
            context.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, localizedReason: reason) { success, _  in
                // DispatchQueue.main.async 强制将内部代码切回主线程执行
//                DispatchQueue.main.async {
//                    if success {
//                        self.isFaceIDAuthenticated = true
//                        print("认证成功")
//                    } else {
//                        self.isFaceIDAuthenticated = false
//                        print("认证失败")
//                    }
//                }
                // 现代代替方案: Task + @MainActor
                Task { @MainActor in
                    if success {
                        self.isFaceIDAuthenticated = true
                        print("认证成功")
                    } else {
                        self.isFaceIDAuthenticated = false
                        print("认证失败")
                    }
                }
            }
        } else {
            // 硬件不支持
            print("没有身份识别")
        }
    }
}
