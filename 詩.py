#!/usr/bin/env python3
import random

text = "十年生死两茫茫。不思量，自难忘。千里孤坟，无处话凄凉。纵使相逢应不识，尘满面，鬓如霜。夜来幽梦忽还乡。小轩窗，正梳妆。相顾无言，惟有泪千行。料得年年肠断处，明月夜，短松冈。"
lt = text.split("。")
while True:

    phrase = lt[random.randint(0, len(lt))]
    smaller_phrase = phrase.split("，")

    omit = random.choice(smaller_phrase)
    #print(omit)
    smaller_phrase = list(map(lambda x: x.replace(omit, "_____"), smaller_phrase))

    print(",".join(smaller_phrase))
    s = input("填空：")
    if s == omit:
        print("正確！")
    else:
        print("錯！答案是" + omit)
