"""「添加账目」视图。"""

import streamlit as st

from config import CATEGORIES
from database import add_expense


def render():
    st.subheader("添加账目")
    with st.form("add_form", clear_on_submit=True):
        amount = st.number_input("金额（元）", min_value=0.01, step=0.01, format="%.2f")
        category = st.selectbox("分类", CATEGORIES)
        date = st.date_input("日期")
        note = st.text_input("备注", placeholder="可选")
        submitted = st.form_submit_button("添加")
    if submitted:
        add_expense(amount, category, date.isoformat(), note.strip())
        st.success(f"已添加：{category} ¥{amount:.2f}")
