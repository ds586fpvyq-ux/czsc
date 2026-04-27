# -*- coding: utf-8 -*-
"""
启动 CZSC 前端应用
"""

from czsc.svc import streamlit_run
import os

# 获取当前目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.join(current_dir, "app.py")

print(f"启动 CZSC 前端应用...")
print(f"应用文件: {app_path}")
print(f"访问地址: http://localhost:8501")

# 启动 Streamlit 应用
streamlit_run(app_path, port=8501, host="localhost")