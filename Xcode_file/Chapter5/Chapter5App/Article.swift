//
//  Article.swift
//  Chapter5App
//
//  Created by Jethro Ming on 2026/5/23.
//

import Foundation
import SwiftUI

struct Article {
    var image: String
    var title: String
    var articleNum: Int
    var subscriptionNum: Int
    
    
    static let articles = [
        Article(image: "01", title: "《活着》", articleNum: 22, subscriptionNum: 245),
        Article(image: "02", title: "《历史是平的》", articleNum: 37, subscriptionNum: 987),
        Article(image: "03", title: "《书信集》", articleNum: 42, subscriptionNum: 231),
    ]
}
