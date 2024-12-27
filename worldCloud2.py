import pandas as pd
from wordcloud import WordCloud

# 读取 Excel 文件
file_path = 'processed_video.xlsx'  # 替换为你的文件路径
df = pd.read_excel(file_path)

# 确保 'title' 列存在
if 'tag' not in df.columns:
    raise ValueError("The Excel file does not have a 'title' column.")

# 拼接所有标题为一个字符串，保留前100个字符
text = ' '.join(df['tag'].dropna().tolist()) # 移除空值并连接为一个字符串，截取前100个字符
import wordcloud

# 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
w = wordcloud.WordCloud(width=1000,height=700,background_color='white',font_path='msyh.ttc')

# 调用词云对象的generate方法，将文本传入
w.generate(text)
# 保存词云图
output_path = 'wordcloud_tag.png'
w.to_file(output_path)

print(f"Word cloud saved to {output_path}")
