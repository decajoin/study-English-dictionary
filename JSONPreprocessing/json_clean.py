import os
import json
import re

# 过滤释义中的"<"、"A" 及其他非必要符号
# 定义清理函数
def clean_definition(definition):
    # 过滤掉 "<"、"A" 及其他非必要符号
    cleaned_definition = re.sub(r'[A<]', '', definition)
    # 去除多余的空格
    cleaned_definition = re.sub(r'\s+', ' ', cleaned_definition).strip()
    return cleaned_definition

# 读取并清理数据
def clean_data(input_dir, output_dir):
    # 如果输出目录不存在，则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历输入目录中的每个 JSON 文件
    for filename in os.listdir(input_dir):
        if filename.endswith('.json'):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename)

            with open(input_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 清理每个章节的释义
            for entry in data:
                entry['definitions'] = [clean_definition(defn) for defn in entry['definitions']]

            # 将清理后的数据写回新的 JSON 文件
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            print(f"{filename} 清理完成!")

# 设置源目录和目标目录
input_dir = 'Chapters'  # 源目录
output_dir = 'NewChapters'  # 目标目录

# 清理数据并输出
clean_data(input_dir, output_dir)

print("所有章节数据清理完成！")
