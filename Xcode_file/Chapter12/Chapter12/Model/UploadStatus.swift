//
//  UploadStatus.swift
//  Chapter12
//
//  Created by Jethro Ming on 2026/7/6.
//

import SwiftUI
import PhotosUI

// MARK: - 1. 上传状态枚举
enum UploadStatus: Equatable {
    case idle
    case uploading(progress: Double)
    case success
    case failed(error: String)
}
