//
//  Date+Extensions.swift
//  Chapter11
//
//  Created by Jethro Ming on 2026/7/4.
//

import SwiftUI

extension DateFormatter {
    static let yearMonth: DateFormatter = {
        let formatter = DateFormatter()
        formatter.dateFormat = "YYYY年MM月"
        return formatter
    }()
}


extension Date {
    var day: String {
        let calendar = Calendar.current
        return "\(calendar.component(.day, from: self))"
    }
    
    // 选中日期
    func isSameDay(as date: Date) -> Bool {
        let calendar = Calendar.current
        return calendar.isDate(self, inSameDayAs: date)
    }
}
