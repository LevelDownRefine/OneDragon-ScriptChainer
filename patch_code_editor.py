import re

with open('src/one_dragon_qt/widgets/setting_card/code_editor_setting_card.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove __init__ docstring
content = re.sub(
    r'    def __init__\(self, parent=None, title: str = "Python 脚本编辑器",\s+initial_code: str = "", script_path: str = "", script_arguments: str = ""\):\s+"""\s+初始化 Python 代码编辑器弹窗\s+:param parent: 父组件\s+:param title: 弹窗标题\s+:param initial_code: 初始显示的代码内容\s+:param script_path: 脚本的本地路径（用于外部编辑功能）\s+:param script_arguments: 脚本的启动参数\s+"""\s+',
    '    def __init__(self, parent=None, title: str = "Python 脚本编辑器",\n                 initial_code: str = "", script_path: str = "", script_arguments: str = ""):\n        ',
    content
)

# Remove _setup_editor_layout docstring
content = re.sub(
    r'    def _setup_editor_layout\(self\) -> None:\s+"""设置编辑器布局，包括启动参数输入框和代码编辑器"""\s+',
    '    def _setup_editor_layout(self) -> None:\n        ',
    content
)

# Remove _on_external_edit docstring
content = re.sub(
    r'    def _on_external_edit\(self\) -> None:\s+"""处理点击“外部编辑”按钮的事件，将内容保存并用系统默认应用打开该脚本文件"""\s+',
    '    def _on_external_edit(self) -> None:\n        ',
    content
)

# Remove get_code docstring
content = re.sub(
    r'    def get_code\(self\) -> str:\s+"""获取编辑器中的 Python 代码"""\s+',
    '    def get_code(self) -> str:\n        ',
    content
)

with open('src/one_dragon_qt/widgets/setting_card/code_editor_setting_card.py', 'w', encoding='utf-8') as f:
    f.write(content)
