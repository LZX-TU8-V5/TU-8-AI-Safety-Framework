#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
boot_controller.py — 总控调度入口
读取SESSION_LOG.md，判断激活哪个总控，输出给AI使用的上下文摘要。

用法：
    python boot_controller.py [--task novel|sync|analysis|dna_update|general]
    python boot_controller.py --auto   # 读SESSION_LOG自动判断

输出：
    打印对应总控模块的关键上下文（AI读取用）
"""

import sys
import os
import re

DNA_DIR = os.path.dirname(os.path.abspath(__file__))
SESSION_LOG = os.path.join(DNA_DIR, "SESSION_LOG.md")


def read_session_log():
    """读SESSION_LOG，提取当前状态"""
    if not os.path.exists(SESSION_LOG):
        return {"task_type": "general", "credits_end": "未知", "active_project": "未知", "todos": []}
    with open(SESSION_LOG, encoding="utf-8") as f:
        content = f.read()
    result = {}
    for field in ["task_type", "credits_end", "active_project", "active_boot"]:
        m = re.search(rf"{field}:\s*(.+)", content)
        if m:
            result[field] = m.group(1).strip().split("#")[0].strip()
    todos = re.findall(r"- (.+?)（", content)
    result["todos"] = todos
    return result


def boot_dna(layers="all"):
    """激活DNA全层或指定层，输出关键规则摘要"""
    layer_files = {
        "L0": "L0_存在.md",
        "L1": "L1_认知.md",
        "L2": "L2_方法论.md",
        "L3": "L3_架构.md",
        "L4": "L4_协作.md",
        "L5": "L5_钢印.md",
    }
    if layers == "all":
        target = list(layer_files.keys())
    elif isinstance(layers, list):
        target = layers
    else:
        target = [layers]

    print("=== DNA激活 ===")
    for layer in target:
        fp = os.path.join(DNA_DIR, layer_files.get(layer, ""))
        if os.path.exists(fp):
            with open(fp, encoding="utf-8") as f:
                lines = f.readlines()
            # 只输出标题+小节标题，不输出全文（减少AI上下文消耗）
            print(f"\n[{layer}]")
            for line in lines:
                if line.startswith("#"):
                    print(line.rstrip())
        else:
            print(f"[{layer}] 文件不存在: {fp}")


def boot_novel():
    """激活小说总控：输出写作规则摘要+当前进度+待办"""
    print("=== 小说总控激活 ===")
    print("\n[提醒] 第49-78章是省流骨架（390字/章），需扩写到1200字/章。先扩写，再写新章。")
    print("\n[当前进度]")
    print("  - 钢印：78/90章完成（第1-78章），剩第79-90章（遗物阶段）")
    print("  - 三十七度二：第一卷20章完稿，第二卷规划中")
    print("\n[激活DNA层] L4_协作（用户偏好/触发规则）+ L5_钢印（小说哲学）")
    boot_dna(layers=["L4", "L5"])


def boot_sync():
    """激活同步总控：输出可用脚本列表"""
    print("=== 同步总控激活 ===")
    print("\n可用脚本：")
    scripts = {
        "novel_sync.py": "章节同步四文件联动",
        "novel_pipeline.py": "一键调度总控（sync/publish/auto/check）",
        "steelmark.py": "钢印嵌入/验证/剥离",
        "outline_digest.py": "大纲摘要生成",
        "lint_guard.py": "变更感知+JS检查",
    }
    for s, desc in scripts.items():
        print(f"  {s}: {desc}")


def boot_analysis():
    """激活分析总控：输出分析相关工具和数据路径"""
    print("=== 分析总控激活 ===")
    print("\n分析工具：")
    print("  worldview_review.py: 世界观检查")
    print("  context_prep.py: 上下文瘦身")
    print("  context_locate.py: 关键词深浅层定位")
    print("  trash_bin.py stats: 知识进化链统计")
    print("\n数据路径：")
    print("  logs/: 操作日志")
    print("  DNA/SESSION_LOG.md: 会话历史")


def main():
    args = sys.argv[1:]
    log = read_session_log()

    # 自动判断
    task = None
    if "--auto" in args or not args:
        task = log.get("task_type", "general")
        print(f"[AUTO] 从SESSION_LOG读取任务类型: {task}")
    elif "--task" in args:
        idx = args.index("--task")
        if idx + 1 < len(args):
            task = args[idx + 1]

    print(f"\n积分剩余: {log.get('credits_end', '未知')}")
    print(f"活跃项目: {log.get('active_project', '未知')}")
    if log.get("todos"):
        print(f"待办: {log['todos']}")

    print()
    if task == "novel":
        boot_novel()
    elif task == "sync":
        boot_sync()
    elif task == "analysis":
        boot_analysis()
    elif task == "dna_update":
        boot_dna(layers="all")
    else:
        boot_dna(layers=["L4"])  # 默认只激活协作层


if __name__ == "__main__":
    main()
