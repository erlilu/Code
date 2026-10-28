"""「删除记录」视图。"""

import streamlit as st

from database import delete_expense


def render():
    st.subheader("删除记录")
    st.caption("输入要删除的记录 ID（可在「查看列表」中看到）")

    # 显示上一次操作的结果提示（放在 rerun 后仍能保留）
    if "flash_success" in st.session_state:
        st.success(st.session_state.pop("flash_success"))
    if "flash_warning" in st.session_state:
        st.warning(st.session_state.pop("flash_warning"))

    expense_id = st.number_input("记录 ID", min_value=1, step=1, key="delete_id")
    if st.button("删除"):
        affected = delete_expense(int(expense_id))
        if affected:
            st.session_state["flash_success"] = f"已删除 ID={int(expense_id)} 的记录"
        else:
            st.session_state["flash_warning"] = f"未找到 ID={int(expense_id)} 的记录"
        st.rerun()
