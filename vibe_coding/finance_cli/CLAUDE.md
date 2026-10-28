# 记账工具（Streamlit + SQLite）

带 Web 界面的个人记账工具，在浏览器里记录和查看日常开销。

## 技术栈
- Python 3.9+ / Streamlit（Web 界面）
- sqlite3（标准库，零配置）

## 运行
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## 目录结构
```
app.py                 # 入口：页面配置 + Tab 路由（仅组装，不写业务）
config.py              # 常量：DB_PATH、预设分类 CATEGORIES
database.py            # 数据访问层：唯一接触 sqlite3 的模块
components/filters.py  # 复用的月份/分类筛选下拉
views/                 # 4 个 Tab 视图，各导出一个 render()
  add.py     # 添加账目
  list.py    # 查看列表
  stats.py   # 分类统计
  delete.py  # 删除记录
```

## 分层与约定
- 依赖方向：app → views → components → database → config（界面层不直接写 SQL）
- 所有 sqlite3 操作集中在 database.py，通过 `get_conn()` context manager 获取连接
- 预设分类集中在 config.CATEGORIES，新增分类只改这一处
- 表 `expenses` 的 `date` 列存 'YYYY-MM-DD'，月份过滤用 `substr(date,1,7)`
- 金额以「元」为单位，展示保留两位小数

## 注意
- 需求仅含增/查/统计/删，不含编辑功能
- Streamlit 不同 Tab 的 widget 需要不同 key 避免冲突（现有 key 前缀：add_/list_/stats_/delete_）
- `views/list.py` 模块名与内置 `list` 冲突，导入时用 `from views import list as list_view`
