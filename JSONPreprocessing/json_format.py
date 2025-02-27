import json
import os

# 进行词典的章节分割，20 个单词为一个章节
# 读取JSON文件
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [json.loads(line) for line in file]

# 提取需要的字段
def extract_word_definitions(data):
    extracted = []
    for item in data:
        word = item.get('headWord', '')
        usphone = item.get('content', {}).get('word', {}).get('content', {}).get('usphone', '')
        translations = item.get('content', {}).get('word', {}).get('content', {}).get('trans', [])
        definitions = [tran.get('tranCn', '') for tran in translations]
        extracted.append({'word': word, 'usphone': usphone, 'definitions': definitions})
    return extracted

# 分割成章节
def split_into_chapters(words, words_per_chapter=20):
    chapters = []
    for i in range(0, len(words), words_per_chapter):
        chapters.append(words[i:i + words_per_chapter])
    return chapters

# 保存为JSON
def save_chapters(chapters, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for idx, chapter in enumerate(chapters, start=1):
        chapter_file = f'{output_dir}/chapter_{idx}.json'
        with open(chapter_file, 'w', encoding='utf-8') as file:
            json.dump(chapter, file, ensure_ascii=False, indent=4)
        print(f'Saved: {chapter_file}')

# 主函数
def main(input_file, output_dir):
    data = load_json(input_file)
    word_definitions = extract_word_definitions(data)
    chapters = split_into_chapters(word_definitions)
    save_chapters(chapters, output_dir)

# 示例用法
main('KaoYan_3.json', './output')