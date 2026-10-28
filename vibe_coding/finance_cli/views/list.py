"""「查看列表」视图。"""

import pandas as pd
import streamlit as st

from components.filters import render_category_filter, render_month_filter
from database import list_expenses


def render():
    st.subheader("查看列表")
    col1, col2 = st.columns(2)
    with col1:
        month = render_month_filter("list_month")
    with col2:
        category = render_category_filter("list_category")

    rows = list_expenses(month=month, category=category)
    if not rows:
        st.info("暂无记录")
        return

    df = pd.DataFrame(
        [
            {
                "ID": row["id"],
                "日期": row["date"],
                "分类": row["category"],
                "金额（元）": round(row["amount"], 2),
                "备注": row["note"] or "",
            }
            for row in rows
        ]
    )
    st.dataframe(df, width="stretch", hide_index=True)

    total = sum(row["amount"] for row in rows)
    st.markdown(f"**共 {len(rows)} 笔，合计 ¥{total:.2f}**")
