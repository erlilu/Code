//
//  Note.swift
//  Chapter7App
//
//  Created by Jethro Ming on 2026/5/24.
//

import Foundation
import SwiftUI

//数据模型
struct Note: Identifiable {
    let id = UUID()         //唯一标识符：Universally Unique Identifier
    var noteContent: String //笔记内容
    
    static let notes = [
        Note(noteContent: "水激石则鸣，人激志则宏。"),
        Note(noteContent: "鸟欲高飞先振翅，人求上进先读书。"),
        Note(noteContent: "百败而其志不折，坚持铸就坚韧不拔之魂。"),
        Note(noteContent: "滴水穿石，非一日之功，坚持方能成就非凡。"),
    ]
    
}
