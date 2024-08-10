import os
import subprocess

# 六十甲子的编号和干支对
ganzhi_list = [
    "甲子",
    "甲寅",
    "甲辰",
    "甲午",
    "甲申",
    "甲戌",
    "乙丑",
    "乙卯",
    "乙巳",
    "乙未",
    "乙酉",
    "乙亥",
    "丙子",
    "丙寅",
    "丙辰",
    "丙午",
    "丙申",
    "丙戌",
    "丁丑",
    "丁卯",
    "丁巳",
    "丁未",
    "丁酉",
    "丁亥",
    "戊子",
    "戊寅",
    "戊辰",
    "戊午",
    "戊申",
    "戊戌",
    "己丑",
    "己卯",
    "己巳",
    "己未",
    "己酉",
    "己亥",
    "庚子",
    "庚寅",
    "庚辰",
    "庚午",
    "庚申",
    "庚戌",
    "辛丑",
    "辛卯",
    "辛巳",
    "辛未",
    "辛酉",
    "辛亥",
    "壬子",
    "壬寅",
    "壬辰",
    "壬午",
    "壬申",
    "壬戌",
    "癸丑",
    "癸卯",
    "癸巳",
    "癸未",
    "癸酉",
    "癸亥",
]

# 获取用户输入
user_input = input("请输入干支或编号: ")

# 处理用户输入
try:
    if user_input.isdigit():
        index = int(user_input) - 1
    else:
        index = ganzhi_list.index(user_input)

    # 检查输入是否有效
    if 0 <= index < 60:
        number_str = f"{index + 1:02d}"
        image_path = f"images/{number_str}_{ganzhi_list[index]}.jpg"

        if os.path.exists(image_path):
            # 使用imgcat显示图片
            subprocess.run(["imgcat", image_path])
        else:
            print("图片文件不存在。")
    else:
        print("无效的输入，请输入正确的干支或编号。")
except ValueError:
    print("无效的输入，请输入正确的干支或编号。")
