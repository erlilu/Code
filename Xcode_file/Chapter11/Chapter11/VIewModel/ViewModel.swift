//
//  ViewModel.swift
//  Chapter11
//
//  Created by Jethro Ming on 2026/7/4.
//

import SwiftUI
// import Observation
@Observable
class ViewModel {
    var historyDaily: [HistoryDaily] = []
    
    let dataURL: String = "https://api.npoint.io/6f46087a29cf514de622"
    
    var currentDate: Date = Date()
    var selectedDate: Date = Date()
    
    
    //网络请求
    func fetchTodayInHistory() {
        let session = URLSession(configuration: .default)
        
        let task = session.dataTask(with: URL(string: dataURL)!) { data, response, error in
            if let httpResponse = response as? HTTPURLResponse {
                //获取Http状态码
                let statusCode = httpResponse.statusCode
                
                if statusCode == 200, let data = data {
                    //成功获取图片数据
                    do {
                        let decoder = JSONDecoder()
                        let decodedData = try decoder.decode([HistoryDaily].self, from: data)
                        DispatchQueue.main.async {
                            self.historyDaily = decodedData
                        }
                    } catch {
                        print("Error decoding JSON:\(error)")
                    }
                } else {
                    // 处理状态码错误或数据为空
                    print("HTTP状态码错误：\(statusCode)")
                }
            } else if let error = error {
                // 处理网络请求错误
                print("错误信息：\(error.localizedDescription)")
            } else {
                // 未知错误或数据为空
                print("未知错误")
            }
        }
        task.resume()
    }
    
    
    // 获取日期数组
    func daysOfMonth() -> [Date] {
        let calendar = Calendar.current
        let range = calendar.range(of: .day, in: .month, for: currentDate)!
        let startOfMonth = calendar.date(from: calendar.dateComponents([.year, .month], from: currentDate))!
        
        return (1 ..< range.count + 1).map {
            calendar.date(byAdding: .day, value: $0 - 1, to: startOfMonth)!
        }
    }
    
    // 匹配正确日期
    func firstDayOfWeekForMonth() -> Int {
        let calendar = Calendar.current
        let firstDay = daysOfMonth().first ?? Date()
        return calendar.component(.weekday, from: firstDay) - 1
    }
    
    
}
