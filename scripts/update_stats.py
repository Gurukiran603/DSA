import os

base_path = "./"

easy = medium = hard = total = 0

for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith(".py"):
            total += 1
            name = file.lower()
            if "easy" in name:
                easy += 1
            elif "medium" in name:
                medium += 1
            elif "hard" in name:
                hard += 1

with open("README.md", "r") as f:
    content = f.read()

def replace(text, start, end, value):
    return text.split(start)[0] + start + str(value) + end + text.split(end)[1]

content = replace(content, "<!--TOTAL_START-->", "<!--TOTAL_END-->", total)
content = replace(content, "<!--EASY_START-->", "<!--EASY_END-->", easy)
content = replace(content, "<!--MEDIUM_START-->", "<!--MEDIUM_END-->", medium)
content = replace(content, "<!--HARD_START-->", "<!--HARD_END-->", hard)

with open("README.md", "w") as f:
    f.write(content)
