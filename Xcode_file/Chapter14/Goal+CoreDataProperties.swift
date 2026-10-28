//
//  Goal+CoreDataProperties.swift
//  Chapter14
//
//  Created by Jethro Ming on 2026/7/8.
//
//

import Foundation
import CoreData


//public typealias GoalCoreDataPropertiesSet = NSSet

extension Goal {

    @nonobjc public class func fetchRequest() -> NSFetchRequest<Goal> {
        return NSFetchRequest<Goal>(entityName: "Goal")
    }

    @NSManaged public var currentProgress: Int64
    @NSManaged public var goalText: String?
    @NSManaged public var id: UUID?
    @NSManaged public var targetDate: Date?

}

extension Goal : Identifiable {

}
