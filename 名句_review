# Memorization for 名句

import random

first_half = [
    "忽如一夜春風來",
    "將軍角弓不得控",
    "瀚海闌干百丈冰",
    "輪台東門送君去",
    "何處望神州",
    "千古興亡多少事",
    "天下英雄誰敵手",
    "辛苦遭逢起一經",
    "山河破碎風飄絮",
    "惶恐灘頭說惶恐",
    "人生自古誰無死"
]
second_half = [
    "千樹萬樹梨花開",
    "都護鐵衣冷難著",
    "愁云慘淡萬里凝",
    "去時雪滿天山路",
    "滿眼風光北固樓",
    "悠悠。不盡長江滾滾流",
    "曹劉。生子當如孫仲謀",
    "干戈寥落四周星",
    "身世浮沉雨打萍",
    "零丁洋裏嘆零丁",
    "留取丹心照汗青"
]

#check


while True:
    f_or_s = random.choice(["first", "second"])
    index = random.randint(0, len(second_half))

    if f_or_s == "first":
        print(second_half[index - 1])
        s = input("前一句是什麽?:  ")
        if s == first_half[index - 1]:
            print("正確！")
        else:
            print("錯，答案是" + first_half[index - 1])
    else:
        print(first_half[index - 1])
        s = input("後一句是什麽?:  ")
        if s == second_half[index - 1]:
            print("正確！")
        else:
            print("錯，答案是" + second_half[index - 1])
