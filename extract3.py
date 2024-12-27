import json
import os
from bs4 import BeautifulSoup
import re

# 指定植物病害文件夹路径
folder_path = "植物病害"  # 修改为你的文件夹路径
bvid_list = []  # 用于存储所有的 bvid

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
                # 提取每个视频的 bvid
                bvid = data["data"]["result"][i].get("bvid")
                if bvid:  # 如果 bvid 存在，添加到列表中
                    bvid_list.append(bvid)

# 将所有 bvid 写入到 txt 文件
output_file = "bvids.txt"  # 输出文件路径
with open(output_file, "w", encoding="utf-8") as f:
    for bvid in bvid_list:
        f.write(bvid + "\n")

print(f"所有 bvid 已成功保存到 {output_file}")
