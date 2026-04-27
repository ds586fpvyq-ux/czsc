# -*- coding: utf-8 -*-
"""
CZSC 前端应用

启动 CZSC 的 Streamlit 前端，展示各种可视化组件
"""

import streamlit as st
import pandas as pd
from czsc.svc import (
    show_comprehensive_weight_backtest,
    show_weight_backtest,
    show_czsc_trader,
    show_multi_backtest,
    show_correlation,
    show_factor_layering,
    show_cumulative_returns
)
from czsc.mock import generate_klines_with_weights, generate_klines

# 设置页面配置
st.set_page_config(
    page_title="CZSC 缠中说禅技术分析工具",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 页面标题
st.title("CZSC 缠中说禅技术分析工具")
st.markdown("基于缠中说禅理论的量化交易研究平台")

# 侧边栏导航
st.sidebar.title("导航")
app_mode = st.sidebar.selectbox(
    "选择功能",
    [
        "📊 权重回测分析",
        "📈 交易策略分析",
        "🔍 相关性分析",
        "📋 因子分析",
        "📄 关于"
    ]
)

if app_mode == "📊 权重回测分析":
    st.subheader("权重回测分析", divider="rainbow")
    
    # 生成示例数据
    if st.button("生成示例数据"):
        dfw = generate_klines_with_weights(seed=42)
        st.session_state["dfw"] = dfw
        st.success(f"生成了 {len(dfw)} 条数据，包含 {dfw['symbol'].nunique()} 个标的")
    
    if "dfw" in st.session_state:
        dfw = st.session_state["dfw"]
        
        # 回测参数
        col1, col2, col3 = st.columns(3)
        with col1:
            fee = st.number_input("单边手续费 (BP)", min_value=0, max_value=100, value=2)
        with col2:
            digits = st.number_input("权重小数位数", min_value=1, max_value=4, value=2)
        with col3:
            yearly_days = st.number_input("年交易天数", min_value=1, max_value=366, value=252)
        
        # 展示回测结果
        if st.button("开始回测"):
            show_comprehensive_weight_backtest(
                dfw,
                fee=fee,
                digits=digits,
                yearly_days=yearly_days
            )

elif app_mode == "📈 交易策略分析":
    st.subheader("交易策略分析", divider="rainbow")
    st.info("此功能正在开发中...")

elif app_mode == "🔍 相关性分析":
    st.subheader("相关性分析", divider="rainbow")
    st.info("此功能正在开发中...")

elif app_mode == "📋 因子分析":
    st.subheader("因子分析", divider="rainbow")
    st.info("此功能正在开发中...")

elif app_mode == "📄 关于":
    st.subheader("关于 CZSC", divider="rainbow")
    st.markdown("""
    **CZSC** - 缠中说禅技术分析工具
    
    基于缠中说禅理论的量化交易研究平台，提供：
    
    - 缠论的 `分型、笔` 的自动识别
    - 定义并实现 `信号-事件-交易` 量化交易逻辑体系
    - 缠论多级别联立决策分析交易
    - Streamlit 量化研究组件库
    
    **版本信息**
    - 当前版本: 0.10.12
    - Python 版本: 3.10+
    
    **使用说明**
    1. 在左侧导航栏选择功能
    2. 生成或上传数据
    3. 设置参数并运行分析
    4. 查看结果和图表
    """)

# 页脚
st.markdown("---")
st.markdown("© 2026 CZSC 缠中说禅技术分析工具")