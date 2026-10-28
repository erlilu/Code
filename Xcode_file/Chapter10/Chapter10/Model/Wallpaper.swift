//
//  Wallpaper.swift
//  Chapter10
//
//  Created by Jethro Ming on 2026/7/3.
//


import SwiftUI

struct Wallpaper: Codable {
    let id: String
    let urls: UnsplashPhotoUrls
}

struct UnsplashPhotoUrls: Codable {
    let small: String
}

// MARK: Unsplash获得开发者权限，得到Access Key. 在Postman等接口测试工具看返回到JSON数据。
