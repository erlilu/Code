//
//  ViewModel.swift
//  Chapter13
//
//  Created by Jethro Ming on 2026/7/6.
//

import SwiftUI


@Observable
class ViewModel {
    var sentenceModel: [SentenceModel] = []
    
    // 初始化加载数据
    init() {
        
    }
    
    // 添加笔记
    func addNote(sentence:String) {
        let newNote = SentenceModel(sentence: sentence, create_time: getCurrentTime())
        sentenceModel.append(newNote)
        saveData()
    }
    
    // 获取当前时间方法
    func getCurrentTime() -> String {
        let dateFormatter = DateFormatter()
        let currentTime = Date()

        dateFormatter.dateFormat = "yyyy-MM-dd"
        
        let formattedTime = dateFormatter.string(from: currentTime)
        return formattedTime
    }
    
    
    // 存储笔记方法
    func saveData() {
        do {
            let data = try JSONEncoder().encode(sentenceModel)
            if let documentsDirectory = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
                let fileURL = documentsDirectory.appendingPathComponent("sentenceModel.json")
                try data.write(to: fileURL)
            }
        } catch {
            print("保存失败信息：\(error)")
        }
    }
    
    
    // 读取笔记方法
    func loadData() {
        if let documentsDirectory = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
            let fileURL = documentsDirectory.appendingPathComponent("sentenceModel.json")
            do {
                let data = try Data(contentsOf: fileURL)
                sentenceModel = try JSONDecoder().decode([SentenceModel].self, from: data)
            } catch {
                print("读取失败信息：\(error)")
            }
        }
    }
    
    
    // 删除笔记
    func deleteNote(id: UUID) {
        if let index = sentenceModel.firstIndex(where: {$0.id == id}) {
            sentenceModel.remove(at: index)
            saveData()
        }
    }
    
    
    
}
