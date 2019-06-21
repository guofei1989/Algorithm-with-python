"""
利用ahocorasick库展示AC自动机的基本功能
"""
import ahocorasick

words = ["好人", "我们", "学习", "我","自由", "梦想", "鼓励", "好梦", "哪里？", "自己"]

actree = ahocorasick.Automaton()

for index, word in enumerate(words):
    actree.add_word(word, (index, word))

actree.make_automaton()


wd_ix = []
for i in actree.iter("我是个好人，我想要好好学习！"):
    wd = i[1][1]
    wd_ix.append(wd)

print(wd_ix)

