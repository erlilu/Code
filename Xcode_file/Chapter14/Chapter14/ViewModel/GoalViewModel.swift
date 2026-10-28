//
//  GoalViewModel.swift
//  Chapter14
//
//  Created by Jethro Ming on 2026/7/8.
//

import SwiftUI
import CoreData

@Observable
class GoalViewModel {
    var goals: [Goal] = []
    
    // 加载数据
    func fetchGoals() {
        let context = Persistence.shared.container.viewContext
        let fetchRequest: NSFetchRequest<Goal> = Goal.fetchRequest()
        
        do {
            goals = try context.fetch(fetchRequest)
        } catch {
            print("Failed to fetch goals: \(error.localizedDescription)")
        }
    }
    
    // 新增目标
    func addGoal(goalText: String, targetDate: Date) {
        let context = Persistence.shared.container.viewContext
        let newGoal = Goal(context: context)
        
        newGoal.id = UUID()
        newGoal.goalText = goalText
        newGoal.targetDate = targetDate
        newGoal.currentProgress = 0
        do {
            try context.save()
            fetchGoals()
        } catch {
            print("Failed to save goal: \(error.localizedDescription)")
        }
    }
    
}


