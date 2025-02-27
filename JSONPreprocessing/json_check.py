import os
import json

# 检查是否存在缺失释义的单词
def check_missing_definitions(input_dir):
    missing_definitions = []

    # 遍历输入目录中的每个 JSON 文件
    for filename in os.listdir(input_dir):
        if filename.endswith('.json'):
            input_file = os.path.join(input_dir, filename)

            with open(input_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 遍历每个单词，检查释义
            for index, entry in enumerate(data):
                for def_index, definition in enumerate(entry['definitions']):
                    if definition.strip() == '/':
                        missing_definitions.append({
                            'file': filename,  # 文件名（章节）
                            'word': entry['word'],  # 单词
                            'definition_index': def_index + 1,  # 释义位置（从 1 开始）
                            'definition': definition  # 缺失的释义内容
                        })

    # 输出所有缺失释义的单词
    if missing_definitions:
        print("以下单词的释义缺失，请手动补充：")
        for item in missing_definitions:
            print(f"文件：{item['file']}, 单词：{item['word']}, 释义位置：{item['definition_index']}, 释义内容：{item['definition']}")
    else:
        print("没有发现缺失的释义。")

# 设置源目录
input_dir = 'Chapters'  # 存储原始 JSON 文件的目录

# 检查缺失的释义
check_missing_definitions(input_dir)
