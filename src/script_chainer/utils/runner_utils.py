from __future__ import annotations

import os
import sys
from pathlib import Path


def build_runner_command(chain_name: str, script_index: int | None = None) -> tuple[list[str], str | None]:
    """构造 runner 启动命令。

    Args:
        chain_name: 脚本链名称。
        script_index: 调试脚本下标，None 表示运行整个脚本链。

    Returns:
        启动命令及其工作目录。
    """
    if getattr(sys, 'frozen', False):
        command = [
            sys.executable,
            '--onedragon',
            '--chain',
            chain_name,
        ]
        if script_index is not None:
            command.extend(['--debug-index', str(script_index)])
        return command, os.path.dirname(sys.executable) or None
    else: # 源码模式
        command = [
            sys.executable,
            "-m",
            "src.script_chainer.win_exe.launcher",
            "--onedragon",
            "--chain",
            chain_name,
        ]
        if script_index is not None:
            command.extend(["--debug-index", str(script_index)])
        # 根据该文件路径OneDragon-ScriptChainer\\src\\script_chainer\\utils\\runner_utils.py
        # 上跳三级得到仓库根目录 OneDragon-ScriptChainer
        repo_root = str(Path(__file__).resolve().parents[3])
        return command, repo_root