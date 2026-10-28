//
//  Date+Extensions.swift
//  Chapter14
//
//  Created by Jethro Ming on 2026/7/8.
//

import SwiftUI

extension Date {
    func toString() -> String {
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "YYYY年MM月DD日"
        return dateFormatter.string(from: self)
    }
}


extension Date {
    func daysUntilDate(_ targetDate: Date) -> Int {
        let calendar = Calendar.current
        let components = calendar.dateComponents([.day], from: self, to: targetDate)
        return components.day ?? 0
    }
}
