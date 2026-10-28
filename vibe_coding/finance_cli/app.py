"""记账工具入口：页面配置 + Tab 路由。"""

import streamlit as st

from database import init_db
from views import add, delete, stats
from views import list as list_view

st.set_page_config(page_title="记账工具", page_icon="💰", layout="wide")
st.title("记账工具")

init_db()

tab_add, tab_list, tab_stats, tab_delete = st.tabs(
    ["添加账目", "查看列表", "分类统计", "删除记录"]
)

with tab_add:
    add.render()
with tab_list:
    list_view.render()
with tab_stats:
    stats.render()
with tab_delete:
    delete.render()
