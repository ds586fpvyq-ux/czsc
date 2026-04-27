# -*- coding: utf-8 -*-
"""
CZSC Plotly 可视化应用

使用 Plotly 展示 CZSC 的各种可视化功能
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from czsc.mock import generate_klines_with_weights, generate_klines
from czsc.utils.plotting.backtest import (
    plot_backtest_stats,
    plot_colored_table,
    plot_long_short_comparison,
    plot_cumulative_returns,
    plot_drawdown_analysis,
    plot_daily_return_distribution,
    plot_monthly_heatmap
)
from czsc.utils.plotting.weight import (
    plot_weight_histogram_kde,
    plot_weight_cdf,
    plot_turnover_overview,
    plot_turnover_cost_analysis,
    plot_weight_time_series
)
from czsc.utils.plotting.kline import (
    plot_czsc_chart
)

# 设置页面配置
st.set_page_config(
    page_title="CZSC Plotly 可视化",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 页面标题
st.title("CZSC Plotly 可视化应用")
st.markdown("使用 Plotly 展示缠中说禅技术分析工具的可视化功能")

# 侧边栏导航
st.sidebar.title("导航")
app_mode = st.sidebar.selectbox(
    "选择可视化功能",
    [
        "📊 权重分布",
        "📈 权重时间序列",
        "📋 回测统计",
        "🔄 多空对比",
        "📉 K线图表",
        "🎨 彩色表格",
        "📄 关于"
    ]
)

if app_mode == "📊 权重分布":
    st.subheader("权重分布分析", divider="rainbow")
    
    # 生成示例数据
    if st.button("生成示例数据"):
        dfw = generate_klines_with_weights(seed=42)
        st.session_state["dfw"] = dfw
        st.success(f"生成了 {len(dfw)} 条数据，包含 {dfw['symbol'].nunique()} 个标的")
    
    if "dfw" in st.session_state:
        dfw = st.session_state["dfw"]
        
        # 绘制权重分布图
        fig = plot_weight_histogram_kde(dfw)
        st.plotly_chart(fig, use_container_width=True)

elif app_mode == "📈 权重时间序列":
    st.subheader("权重时间序列分析", divider="rainbow")
    
    if "dfw" in st.session_state:
        dfw = st.session_state["dfw"]
        
        # 绘制权重时间序列
        fig = plot_turnover_overview(dfw)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("请先在 '权重分布' 页面生成示例数据")

elif app_mode == "📋 回测统计":
    st.subheader("回测统计分析", divider="rainbow")
    
    if "dfw" in st.session_state:
        dfw = st.session_state["dfw"]
        
        # 绘制回测统计图表
        fig = plot_backtest_stats(dfw)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("请先在 '权重分布' 页面生成示例数据")

elif app_mode == "🔄 多空对比":
    st.subheader("多空对比分析", divider="rainbow")
    
    if "dfw" in st.session_state:
        dfw = st.session_state["dfw"]
        
        # 绘制多空对比图表
        fig = plot_long_short_comparison(dfw)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("请先在 '权重分布' 页面生成示例数据")

elif app_mode == "📉 K线图表":
    st.subheader("K线图表分析", divider="rainbow")
    
    # 生成K线数据
    if st.button("生成K线数据"):
        df = generate_klines(seed=42)
        st.session_state["kline_data"] = df
        st.success(f"生成了 {len(df)} 条K线数据，包含 {df['symbol'].nunique()} 个标的")
    
    if "kline_data" in st.session_state:
        df = st.session_state["kline_data"]
        
        # 选择标的
        symbols = df["symbol"].unique()
        selected_symbol = st.selectbox("选择标的", symbols)
        
        # 过滤数据
        df_symbol = df[df["symbol"] == selected_symbol].tail(100)
        
        # 简单的K线图表
        fig = go.Figure(data=[go.Candlestick(
            x=df_symbol['dt'],
            open=df_symbol['open'],
            high=df_symbol['high'],
            low=df_symbol['low'],
            close=df_symbol['close']
        )])
        fig.update_layout(
            title=f"{selected_symbol} K线图表",
            xaxis_title="日期",
            yaxis_title="价格",
            plot_bgcolor="white",
            paper_bgcolor="white"
        )
        st.plotly_chart(fig, use_container_width=True)

elif app_mode == "🎨 彩色表格":
    st.subheader("彩色表格展示", divider="rainbow")
    
    # 创建示例数据
    data = {
        "标的": ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"],
        "收益率": [0.05, -0.02, 0.08, 0.03, -0.01],
        "波动率": [0.2, 0.15, 0.25, 0.18, 0.3],
        "夏普比率": [1.2, 0.8, 1.5, 1.0, 0.6]
    }
    df = pd.DataFrame(data)
    
    # 绘制彩色表格
    fig = plot_colored_table(df)
    st.plotly_chart(fig, use_container_width=True)

elif app_mode == "📄 关于":
    st.subheader("关于 Plotly 可视化", divider="rainbow")
    st.markdown("""
    **CZSC Plotly 可视化应用**
    
    本应用展示了 CZSC 库中基于 Plotly 的可视化功能：
    
    - 📊 权重分布 - 展示不同标的的权重分布情况
    - 📈 权重时间序列 - 展示权重随时间的变化趋势
    - 📋 回测统计 - 展示回测的各项统计指标
    - 🔄 多空对比 - 对比多头和空头的表现
    - 📉 K线图表 - 展示K线和技术指标
    - 🎨 彩色表格 - 展示数据的彩色表格
    
    **技术说明**
    - **可视化库**: Plotly
    - **前端框架**: Streamlit
    - **数据处理**: pandas, numpy
    
    **使用说明**
    1. 在左侧导航栏选择可视化功能
    2. 生成或选择数据
    3. 查看 Plotly 图表
    4. 可以与图表进行交互（缩放、悬停等）
    """)

# 页脚
st.markdown("---")
st.markdown("© 2026 CZSC 缠中说禅技术分析工具")