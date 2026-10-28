"""「分类统计」视图。"""

import pandas as pd
import streamlit as st

from components.filters import render_month_filter
from database import get_category_stats


def render():
    st.subheader("分类统计")
    month = render_month_filter("stats_month")

    rows = get_category_stats(month=month)
    if not rows:
        st.info("暂无数据")
        return

    df = pd.DataFrame(
        [
            {
                "分类": row["category"],
                "笔数": row["cnt"],
                "总金额（元）": round(row["total"], 2),
            }
            for row in rows
        ]
    )
    total = sum(row["total"] for row in rows)
    df["占比"] = (df["总金额（元）"] / total * 100).round(1).astype(str) + "%"

    st.bar_chart(df.set_index("分类")[["总金额（元）"]], width="stretch")
    st.dataframe(df, width="stretch", hide_index=True)
    st.markdown(f"**该月总支出 ¥{total:.2f}**")
