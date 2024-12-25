import json
import os
from bs4 import BeautifulSoup
import re
import pandas as pd

# 指定植物病害文件夹路径
folder_path = "植物病害"  # 修改为你的文件夹路径
processed_list = []

# 遍历文件夹中的所有 JSON 文件
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)

        # 打开并读取每个 JSON 文件
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # 检查并遍历 JSON 中的数据
        if "data" in data and "result" in data["data"] and len(data["data"]["result"]) > 0:
            for i in range(len(data["data"]["result"])):
                # 提取每个视频的字段
                title = data["data"]["result"][i]["title"]
                play = data["data"]["result"][i]["play"]
                review = data["data"]["result"][i]["review"]
                video_review = data["data"]["result"][i]["video_review"]
                tag = data["data"]["result"][i]["tag"]
                favorites = data["data"]["result"][i]["favorites"]
                duration = data["data"]["result"][i]["duration"]
                video_id = data["data"]["result"][i]["id"]  # 添加 id 字段
                arcurl = data["data"]["result"][i]["arcurl"]  # 添加 arcurl 字段

                # 如果标题包含HTML标签，可以使用BeautifulSoup移除HTML标签
                soup = BeautifulSoup(title, "html.parser")
                clean_title = soup.get_text()

                # 使用正则表达式去除指定字符：+、】、【、[、]
                clean_title = re.sub(r"[+\【\】\[\]]", "", clean_title)

                # 将处理后的数据存储到字典中
                video_data = {
                    'id': video_id,         # 添加 id 字段
                    'arcurl': arcurl,       # 添加 arcurl 字段
                    'title': clean_title,   # 处理后的标题
                    'play': play,
                    'review': review,
                    'video_review': video_review,
                    'tag': tag,
                    'favorites': favorites,
                    'duration': duration
                }

                # 将字典添加到结果列表中
                processed_list.append(video_data)

# 将处理后的数据转换为 DataFrame
df = pd.DataFrame(processed_list)

# 去除重复的 id 行
df = df.drop_duplicates(subset='id', keep='first')

# 保存为 Excel 文件
output_file = "processed_video.xlsx"
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"数据已保存到 {output_file}")
