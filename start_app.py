# -*- coding: utf-8 -*-
"""
启动 CZSC 前端应用
"""

from czsc.svc import streamlit_run
import os
import sys

# 获取当前目录的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.join(current_dir, "app.py")

# 支持命令行参数指定端口
port = 8501
if len(sys.argv) > 1 and sys.argv[1].startswith('--port='):
    port = int(sys.argv[1].split('=')[1])

print(f"启动 CZSC 前端应用...")
print(f"应用文件: {app_path}")
print(f"访问地址: http://localhost:{port}")

# 启动 Streamlit 应用
streamlit_run(app_path, port=port, host="localhost")