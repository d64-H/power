import streamlit as st
import json
import os

st.set_page_config(page_title="Nexus", page_icon="🌌", layout="centered")

# 隐藏 Streamlit 自带的顶栏和菜单，让它看起来更像一个独立的 App
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            
            /* 设计图标卡片的样式 */
            .app-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
                gap: 20px;
                padding: 20px 0;
            }
            .app-card {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 15px;
                background: white;
                border-radius: 16px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.05);
                text-decoration: none !important;
                color: #333 !important;
                transition: transform 0.2s, box-shadow 0.2s;
            }
            .app-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            }
            .app-icon {
                font-size: 40px;
                margin-bottom: 10px;
            }
            .app-name {
                font-size: 14px;
                font-weight: 500;
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>🌌 Nexus</h2>", unsafe_allow_html=True)
# 你的所有 App 数据（以后你可以写个页面让 AI 帮你自动生成这个列表）
# 这里的 url 先放百度和你的本地 Streamlit 为例
apps = [
    {"name": "稚荷", "icon": "📝", "url": "https://anthropic-1.streamlit.app/"}, 
    {"name": "记账分析", "icon": "💰", "url": "http://localhost:8502"},
    {"name": "词云生成", "icon": "☁️", "url": "http://localhost:8503"},
    {"name": "百度", "icon": "🔍", "url": "https://www.baidu.com"},
    {"name": "GitHub", "icon": "🐱", "url": "https://github.com"},
    {"name": "待添加...", "icon": "➕", "url": "#"}
]

# 渲染网格（注意：这里的代码千万不要有任何缩进空格）
html_content = '<div class="app-grid">'
for app in apps:
    html_content += f'<a class="app-card" href="{app["url"]}" target="_blank"><div class="app-icon">{app["icon"]}</div><div class="app-name">{app["name"]}</div></a>'
html_content += '</div>'

# 注入到 Streamlit
st.markdown(html_content, unsafe_allow_html=True)