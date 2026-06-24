import re

with open('src/script_chainer/win_exe/script_runner.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('        # 重置 sys.argv 并填入脚本路径作为第一个参数\n', '')
content = content.replace('        # 将脚本所在目录添加到系统路径以支持相对导入\n', '')
content = content.replace('        # 切换工作目录到脚本所在目录\n', '')

with open('src/script_chainer/win_exe/script_runner.py', 'w', encoding='utf-8') as f:
    f.write(content)
