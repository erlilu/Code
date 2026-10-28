//
//  SentenceModel.swift
//  Chapter13
//
//  Created by Jethro Ming on 2026/7/6.
//

import SwiftUI

struct SentenceModel: Identifiable, Codable {
    var id: UUID = UUID()
    var sentence: String
    var create_time: String
}
