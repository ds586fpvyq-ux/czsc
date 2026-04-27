# -*- coding: utf-8 -*-
"""
CZSC Plotly 演示脚本

直接生成和展示 Plotly 图表，不依赖 Streamlit
"""

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

def main():
    print("CZSC Plotly 演示脚本")
    print("=" * 50)
    
    # 生成示例数据
    print("1. 生成示例数据...")
    dfw = generate_klines_with_weights(seed=42)
    print(f"   生成了 {len(dfw)} 条数据，包含 {dfw['symbol'].nunique()} 个标的")
    
    # 生成K线数据
    df_kline = generate_klines(seed=42)
    print(f"   生成了 {len(df_kline)} 条K线数据")
    
    print("\n2. 生成 Plotly 图表...")
    
    # 1. 权重分布直方图
    print("   - 权重分布直方图")
    fig1 = plot_weight_histogram_kde(dfw)
    fig1.write_html("plotly_weight_distribution.html")
    
    # 2. 权重时间序列
    print("   - 权重时间序列")
    fig2 = plot_turnover_overview(dfw)
    fig2.write_html("plotly_weight_timeseries.html")
    
    # 3. 权重CDF
    print("   - 权重CDF")
    fig3 = plot_weight_cdf(dfw)
    fig3.write_html("plotly_weight_cdf.html")
    
    # 4. 换手成本分析
    print("   - 换手成本分析")
    fig4 = plot_turnover_cost_analysis(dfw)
    fig4.write_html("plotly_turnover_cost.html")
    
    # 5. 彩色表格
    print("   - 彩色表格")
    data = {
        "标的": ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"],
        "收益率": [0.05, -0.02, 0.08, 0.03, -0.01],
        "波动率": [0.2, 0.15, 0.25, 0.18, 0.3],
        "夏普比率": [1.2, 0.8, 1.5, 1.0, 0.6]
    }
    df_table = pd.DataFrame(data)
    fig5 = plot_colored_table(df_table)
    fig5.write_html("plotly_colored_table.html")
    
    # 6. K线图表
    print("   - K线图表")
    df_symbol = df_kline[df_kline["symbol"] == "AAPL"].tail(100)
    fig6 = go.Figure(data=[go.Candlestick(
        x=df_symbol['dt'],
        open=df_symbol['open'],
        high=df_symbol['high'],
        low=df_symbol['low'],
        close=df_symbol['close']
    )])
    fig6.update_layout(
        title="AAPL K线图表",
        xaxis_title="日期",
        yaxis_title="价格",
        plot_bgcolor="white",
        paper_bgcolor="white"
    )
    fig6.write_html("plotly_kline.html")
    
    print("\n3. 图表生成完成！")
    print("   生成的 HTML 文件：")
    print("   - plotly_weight_distribution.html")
    print("   - plotly_weight_timeseries.html")
    print("   - plotly_weight_cdf.html")
    print("   - plotly_turnover_cost.html")
    print("   - plotly_colored_table.html")
    print("   - plotly_kline.html")
    print("\n   请在浏览器中打开这些文件查看图表。")

if __name__ == "__main__":
    main()