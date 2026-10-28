//
//  ContentView.swift
//  Hello Xcode
//
//  Created by Jethro Ming on 2026/2/23.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        ZStack {
            LinearGradient(
                colors: [
                    Color.blue, Color.cyan.opacity(0.5), Color.indigo
                ],
                startPoint: .topLeading,
                endPoint: .bottomTrailing
            )
                .ignoresSafeArea()
            
            VStack {
                Image(systemName: "figure.stand.dress.line.vertical.figure")
                    .imageScale(.large)
                    .foregroundStyle(.white)
                
                Text("Welcome to iOS Development !")
                    .font(.largeTitle)
                    .fontWeight(.bold)
                    .multilineTextAlignment(.center)
                
                Text("First App")
                    .font(.title)
                    .fontWeight(.thin)
                    .padding()
                    .background(Color.blue.opacity(0.2))
                
                Text("I Love to Code !")
                
                Text("Please feel free to ask questions, send requests via the courese Q&A or direct message me.")
                    .bold()
                    .foregroundStyle(.red)
                    .multilineTextAlignment(.center)
                    .padding()
                    .font(.title2)
                
                Image(.bdsmTools)
                    .resizable()
                    .frame(width: 200, height: 300)
                    }
            .padding()
        }
    }
}

#Preview {
    ContentView()
}

