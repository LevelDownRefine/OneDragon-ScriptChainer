import re

with open('src/script_chainer/gui/page/script_setting_cards.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('            # 保存编辑器中的代码\n', '')

with open('src/script_chainer/gui/page/script_setting_cards.py', 'w', encoding='utf-8') as f:
    f.write(content)
