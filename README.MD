# README

## Motivation

在考研备考时发现了[Qwerty Learner](https://qwerty.kaiyi.cool/)，觉得还不错，然后在作者的 GitHub 仓库里面找到了使用的词书的[源 JSON 文件](https://github.com/kajweb/dict/blob/master/book/1521164658897_KaoYan_3.zip)。

![image-20250227140600586](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20250227140600586.png)

为了更好的复习练习后的单词，所以准备编写一个 Web 页面进行展示每个章节的所有单词，包括它的词义和音标。

## Implement

利用 `json_format.py` 对词典 JOSN 进行分割，每章 20 个单词，一共 187 章，使其符合练习 Web 的模式。分割后的 JOSN 如下所示：

![image-20250227090451900](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20250227090451900.png)

发现单词的释义中存在某些 '<'、'A' 及其他非必要符号，所以使用 `json_clean.py` 进行过滤。使用 `json_check.py` 对所有章节进行检查吗，发现一些单词存在释义缺失的情况，然后使用 `json_replenish.py` 对缺失的单词释义进行补充完整。

利用 `HTML` + `CSS` + `JS` 编写了一个简单的词典展示 Web，方便随时选择对应章节进行复习。利用有道英语发音接口实现单词发音，提供单词测试模式，进入测试模式会隐藏单词释义，点击对应单词会重新显示释义。

词典 Web 实现效果如下图所示：

![image-20250301103959601](https://yeyi0003.oss-cn-hangzhou.aliyuncs.com/image-20250301103959601.png)



