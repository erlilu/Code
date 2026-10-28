"""数据访问层：建表 + 增删查 + 统计。唯一接触 sqlite3 的模块。"""

import sqlite3
from contextlib import contextmanager

from config import DB_PATH

_SCHEMA = """
CREATE TABLE IF NOT EXISTS expenses (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    amount     REAL    NOT NULL CHECK (amount > 0),
    category   TEXT    NOT NULL,
    date       TEXT    NOT NULL,
    note       TEXT    DEFAULT '',
    created_at TEXT    DEFAULT (datetime('now', 'localtime'))
);
"""


@contextmanager
def get_conn():
    """建立连接，正常退出提交，最终关闭。"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    """建表（幂等）。"""
    with get_conn() as conn:
        conn.execute(_SCHEMA)


def add_expense(amount, category, date, note=""):
    """插入一条记录，返回新记录 ID。"""
    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO expenses (amount, category, date, note) VALUES (?, ?, ?, ?)",
            (amount, category, date, note),
        )
        return cur.lastrowid


def list_expenses(month=None, category=None):
    """按月份（'YYYY-MM'）和分类过滤，按日期降序返回。"""
    query = "SELECT id, amount, category, date, note FROM expenses"
    conditions, params = [], []
    if month:
        conditions.append("substr(date, 1, 7) = ?")
        params.append(month)
    if category:
        conditions.append("category = ?")
        params.append(category)
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    query += " ORDER BY date DESC, id DESC"
    with get_conn() as conn:
        return conn.execute(query, params).fetchall()


def get_distinct_months():
    """返回数据中已有的月份列表（'YYYY-MM'），降序。"""
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT DISTINCT substr(date, 1, 7) AS month FROM expenses ORDER BY month DESC"
        ).fetchall()
        return [row["month"] for row in rows]


def delete_expense(expense_id):
    """按 ID 删除，返回受影响行数（0 表示未命中）。"""
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        return cur.rowcount


def get_category_stats(month=None):
    """按分类汇总（笔数、总金额），按总金额降序返回。"""
    query = "SELECT category, COUNT(*) AS cnt, SUM(amount) AS total FROM expenses"
    params = []
    if month:
        query += " WHERE substr(date, 1, 7) = ?"
        params.append(month)
    query += " GROUP BY category ORDER BY total DESC"
    with get_conn() as conn:
        return conn.execute(query, params).fetchall()
