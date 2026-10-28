# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# 项目名称

## 项目概述
一个书签管理应用（保存、整理、搜索书签）。

> ⚠️ 当前仓库尚未初始化：没有 `package.json`、`src/`、`prisma/` 等任何代码，也还没有 Git 提交。以下技术栈与项目结构是**计划**，不是现状。

## 技术栈
- 前端：Next.js 14 + TypeScript + Tailwind CSS
- 后端：Next.js API Routes
- 数据库：Prisma + SQLite
- 部署：Vercel

## 项目结构
```text
src/
├── app/          # Next.js App Router 页面
│   ├── api/      # API 路由
│   ├── layout.tsx # 全局布局
│   └── page.tsx  # 首页
├── components/   # React 组件
│   ├── ui/       # 通用UI组件
│   └── features/ # 业务组件
├── lib/          # 工具函数和配置
├── prisma/       # 数据库 schema 和迁移
└── types/        # TypeScript 类型定义
```

## 编码规范
- 使用函数式组件 + React Hooks
- 组件文件使用 PascalCase 命名（如 BookmarkCard.tsx）
- 工具函数使用 camelCase 命名
- API 路由返回统一格式：`{ success: boolean, data?: any, error?: string }`
- 所有数据库操作通过 Prisma Client 执行

## 开发命令
尚无 `package.json`，以下为 Next.js + Prisma 脚手架搭建后的预期命令（当前不可运行）：
- 安装依赖：`npm install`
- 开发服务器：`npm run dev`
- 构建：`npm run build`
- Lint：`npm run lint`
- 数据库迁移：`npx prisma migrate dev`

## 当前开发状态
- [ ] 项目脚手架（Next.js + Prisma 初始化）—— 未开始
- [ ] 数据库 Schema 设计
- [ ] 书签 CRUD API
- [ ] 前端页面
- [ ] 搜索功能

## 注意事项
- SQLite 数据库文件在 prisma/dev.db，不要提交到 Git
- 环境变量在 .env 文件中，不要提交到 Git
- 所有新功能先创建 Git 分支再开发
