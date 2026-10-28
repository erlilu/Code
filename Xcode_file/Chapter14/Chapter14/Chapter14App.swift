//
//  Chapter14App.swift
//  Chapter14
//
//  Created by Jethro Ming on 2026/7/8.
//

import SwiftUI

@main
struct Chapter14App: App {
    var body: some Scene {
        WindowGroup {
            ContentView(goalViewModel: GoalViewModel())
        }
    }
}
