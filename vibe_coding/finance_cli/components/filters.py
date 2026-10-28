"""复用的筛选下拉组件。"""

import streamlit as st

from config import CATEGORIES
from database import get_distinct_months

_ALL = "全部"


def render_month_filter(key):
    """月份下拉：由已有月份生成，返回选中月份（'全部' 返回 None）。"""
    options = [_ALL] + get_distinct_months()
    selected = st.selectbox("月份", options, key=key)
    return None if selected == _ALL else selected


def render_category_filter(key):
    """分类下拉：预设分类，返回选中分类（'全部' 返回 None）。"""
    options = [_ALL] + CATEGORIES
    selected = st.selectbox("分类", options, key=key)
    return None if selected == _ALL else selected
