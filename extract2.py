import json
from bs4 import BeautifulSoup

# 读取 JSON 文件
file_path = "植物病害/植物病害_ 1.json"  # 修改为你的文件路径
with open(file_path, "r", encoding="utf-8") as f:
    
    data = json.load(f)

print(data["data"]["result"][0])
