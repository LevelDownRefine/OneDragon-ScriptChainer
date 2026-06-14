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
    common_args = ["--onedragon", "--chain", chain_name]
    if script_index is not None:
        common_args.extend(["--debug-index", str(script_index)])

    # 可执行文件模式
    if getattr(sys, 'frozen', False):
        command = [sys.executable, *common_args]
        return command, os.path.dirname(sys.executable) or None
    else: # 源码模式
        file_path = Path(__file__).resolve()
        if len(file_path.parents) < 4:
            raise RuntimeError(f"无法确定仓库根目录: {file_path}")

        # 根据该文件路径OneDragon-ScriptChainer\\src\\script_chainer\\utils\\runner_utils.py
        # 上跳三级得到仓库根目录 OneDragon-ScriptChainer
        repo_root = str(file_path.parents[3])
        launcher_path = str(Path(repo_root) / "src" / "script_chainer" / "win_exe" / "launcher.py")
        command = [
            sys.executable,
            launcher_path,
            *common_args,
        ]
        return command, repo_root
