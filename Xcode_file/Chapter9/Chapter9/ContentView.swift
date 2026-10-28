//
//  ContentView.swift
//  Chapter9
//
//  Created by Jethro Ming on 2026/6/15.
//

import SwiftUI
import StoreKit

struct ContentView: View {
    // 参数赋值
//    @State private var isBellSlash: Bool = UserDefaults.standard.bool(forKey: "isBellSlash")
    @AppStorage("isBellSlash") private var isBellSlash: Bool = false
    // 参数声明
//    @State private var isBellSlash: Bool = false
    @State private var isDark: Bool = false
    @State private var selectedColor: Color = .blue
    @State private var selectedLanguage: String = "简体中文"
    @State private var languages = ["简体中文","繁体中文","英文"]
    @State private var selectedNumber: Int = 17
    
    var body: some View {
        NavigationStack {
            Form {
                // 常规设置
                Section {
                    notificationToggleView
                    darkModeToggleView
                } header: {
                    Text("常规设置")
                }
                .padding(.vertical, 3)
                // 个性化
                Section {
                    colorPickerView
                    languagePickerView
                    fontSizeStepperView
                } header: {
                    Text("个性化")
                }
                .padding(.vertical, 6)
                // 关于我们
                Section {
                    feedbackBtnView
                    appReviewBtnView
                    aboutAsBtnView
                } header: {
                    Text("关于我们")
                }
                .padding(.vertical, 8)
            }
            .navigationTitle("应用设置")
            .navigationBarTitleDisplayMode(.inline)
        }

    }
    
    // 消息通知
    private var notificationToggleView: some View {
        Toggle (isOn: $isBellSlash,) {
            HStack {
                Image(systemName: "bell")
                    .font(.system(size: 20))
                Text("消息通知")
            }
        }
        // 监听更新参数值
//        .onChange(of: isBellSlash,) {
//            newValue in UserDefaults.standard.set(newValue, forKey: "isBellSlash")
//        }
    }
    
    
    // 深色模式
    private var darkModeToggleView: some View {
        Toggle(isOn: $isDark,) {
            HStack {
                Image(systemName: "moon.stars")
                    .font(.system(size: 20))
                Text("深色模式")
            }
        }
        .preferredColorScheme(isDark ? .dark : .light)
    }
    
    
    // 主题颜色
    private var colorPickerView: some View {
        ColorPicker(selection: $selectedColor, label: {
            HStack {
                Image(systemName: "paintbrush")
                    .font(.system(size: 20))
                Text("主题颜色")
            }
        })
    }
    
    
    // 系统语言
    private var languagePickerView: some View {
        Picker(selection: $selectedLanguage, label:
            HStack {
                Image(systemName: "waveform")
                    .font(.system(size: 20))
                Text("系统语言")
            }
        ) {
            ForEach(languages, id: \.self) {
                language in Text(language)
            }
        }
    }
    
    // 字体大小
    private var fontSizeStepperView: some View {
        Stepper(value: $selectedNumber, in: 1 ... 48, label: {
            HStack {
                Image(systemName: "a.circle")
                    .font(.system(size: 20))
                Text("字体大小:" + "\(selectedNumber)")
            }
        })
    }
    
    // 意见反馈
    private var feedbackBtnView: some View {
        Button(action: {
            
        }) {
            HStack {
                Image(systemName: "ellipsis.message")
                    .font(.system(size: 20))
                Text("意见反馈")
            }
        }
        .buttonStyle(PlainButtonStyle())  //常规按钮样式
    }
    
    
    // 去app store 评分
    private var appReviewBtnView: some View {
        Button(action: {
            appReview()
        }) {
            HStack {
                Image(systemName: "star")
                    .font(.system(size: 20))
                Text("去App Store评分")
            }
        }
        .buttonStyle(PlainButtonStyle())
    }
    
    // App Store评分方法
    func appReview() {
        if let scene = UIApplication.shared.connectedScenes.first(where: {
            $0.activationState == .foregroundActive
        } ) as? UIWindowScene {
            SKStoreReviewController.requestReview(in: scene)
        }
    }
    
    // 关于应用
    private var aboutAsBtnView: some View {
        Button(action: {
            
        }) {
            HStack {
                Image(systemName: "person")
                    .font(.system(size: 20))
                Text("关于应用")
            }
        }
        .buttonStyle(PlainButtonStyle())
    }
}

#Preview {
    ContentView()
}
