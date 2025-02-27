import os
import json

# 需要补充的单词的释义
translations = {
    "shiver": "寒战，打颤",
    "dread": "恐惧，害怕",
    "hug": "拥抱",
    "envy": "嫉妒，羡慕",
    "blush": "脸红，羞愧",
    "collapse": "倒塌，崩溃",
    "debate": "辩论，争论",
    "assault": "袭击，攻击",
    "giggle": "咯咯笑",
    "glimpse": "一瞥，闪现",
    "stroll": "散步，漫步",
    "cease": "停止，终止",
    "boycott": "抵制，联合抵制",
    "curse": "诅咒，咒骂",
    "nonetheless": "尽管如此，仍然",
    "twinkle": "闪烁，发光",
    "glide": "滑动，滑行",
    "auction": "拍卖，竞拍",
    "revolt": "反叛，起义",
    "slap": "拍打，巴掌",
    "reform": "改革，改进",
    "arrest": "逮捕，拘留",
    "tow": "拖，牵引",
    "fore": "前，前面",
    "gaze": "凝视，注视",
    "exile": "流放，放逐",
    "limp": "跛行，软弱",
    "compute": "计算，估算",
}

# 输入和输出的目录
input_dir = "NewChapters"  # 需要修改成你实际的目录
output_dir = "Temp"  # 输出目录

# 创建输出目录
os.makedirs(output_dir, exist_ok=True)

# 遍历 Chapters 目录下的所有 JSON 文件
for filename in os.listdir(input_dir):
    if filename.endswith(".json"):
        # 读取每个 JSON 文件
        filepath = os.path.join(input_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)

        modified = False  # 标记是否有修改

        # 遍历每个单词
        for word_entry in data:
            word = word_entry["word"]
            # 检查每个释义
            for i, definition in enumerate(word_entry["definitions"]):
                if definition.strip() == "/":
                    # 如果释义缺失，使用预设的翻译
                    if word in translations:
                        word_entry["definitions"][i] = translations[word]
                        modified = True

        # 如果有修改，保存到新的文件
        if modified:
            new_filepath = os.path.join(output_dir, filename)
            with open(new_filepath, 'w', encoding='utf-8') as new_file:
                json.dump(data, new_file, ensure_ascii=False, indent=4)
            print(f"文件 {filename} 已更新")
        else:
            print(f"文件 {filename} 无需更新")
