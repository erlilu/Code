//
//  Persistence.swift
//  Chapter14
//
//  官方：创建管理数据文件。 作为一个CoreData配置模板，用于启用应用的数据管理
//  Created by Jethro Ming on 2026/7/8.
//

import CoreData

struct Persistence {
    static let shared = Persistence()
    
    let container: NSPersistentContainer
    
    init(inMemory: Bool = false) {
        container = NSPersistentCloudKitContainer(name: "CoreData")
        
        if inMemory { container.persistentStoreDescriptions.first!.url = URL(fileURLWithPath: "/dev/null")
        }
        
        container.loadPersistentStores(completionHandler: { _, error in
            if let error = error as NSError? {
                fatalError("Unresolved error \(error), \(error.userInfo)")
            }
        })
    }
}
