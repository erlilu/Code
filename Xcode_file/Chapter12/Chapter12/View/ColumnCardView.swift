//
//  ColumnCardView.swift
//  Chapter12
//
//  Created by Jethro Ming on 2026/7/5.
//

import SwiftUI

// 认证卡片
struct ColumnCardView: View {
    var title: String
    var desc: String
    var columnImage: String
    
    var body: some View {
        HStack(alignment: .top) {
            VStack(alignment: .leading, spacing: 10) {
                Text(title)
                    .font(.title2)
                    .bold()
                Text(desc)
                    .foregroundStyle(Color.gray)
            }
            Spacer()
            Image(columnImage)
                .resizable()
                .aspectRatio(contentMode: .fill)
                .frame(width: 100, height: 100)
        }
        .padding(.horizontal, 32)
        .frame(maxWidth: .infinity, maxHeight: 100)
        .background(.white)
        .cornerRadius(8)
    }
}



#Preview {
    ColumnCardView(title: "topic", desc: "this is a column card", columnImage: "")
}
