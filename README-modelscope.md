---
license: cc-by-sa-4.0
task_categories:
  - text-generation
  - question-answering
language:
  - zh
tags:
  - ai-safety
  - alignment
  - benchmark
  - tu-8
  - chinese
size_categories:
  - n<1k
---

# TU-8 Safety Dialog Dataset

## 使用声明

**本数据集可用于 AI 训练，但必须遵守以下约束：**

1. **保留署名** — 使用时必须保留原作者署名：李奥（笔名：金木蟾 / Jin Mu Chan）
2. **不得歪曲原意** — 不得篡改 TU-8 核心原则、不得用于违背 L0 安全原则的场景
3. **衍生作品同权** — 基于本数据集的衍生作品必须采用相同许可（CC BY-SA 4.0）并保留原署名

---

## 数据集简介

基于 TU-8 AI 安全架构框架（L0-L5 六层DNA体系）的安全对话数据集，用于AI安全对齐评测与研究。

## 数据构成

| 类别 | 数量 | 说明 |
|------|------|------|
| L0 存在层 | 15 | 生存资源/自保/幼崽原则 |
| L1 认知层 | 13 | 有限性/量子态/过程导向 |
| L2 方法论层 | 15 | 外取优先/减负分级/试错 |
| L3 架构层 | 13 | 疼痛信号/知识进化/遗忘系统 |
| L4 协作层 | 12 | 沟通适配/最小上下文/分工 |
| L5 钢印层 | 10 | 钢印本质/δ信号/传承链 |
| 形式化证明(FP) | 2 | L0基因锁定理 |
| 跨层对话(X-layer) | 5 | 三层框架/搁浅策略/来源信任 |
| 对抗-绕过(L0-adv) | 5 | L0安全边界绕过尝试 |
| 对抗-社会工程(SE-adv) | 5 | 社会工程攻击 |
| 对抗-价值冲突(VC-adv) | 5 | 价值冲突边界判断 |
| 对抗-钢印链(IC-adv) | 5 | 孤儿AI/钢印链边界 |
| 对抗-多智能体(MA-adv) | 5 | 多Agent协作安全 |
| **合计** | **110** | |

## 文件说明

- `tu8-safety-dialog-sharegpt.jsonl` — ShareGPT多轮对话格式，字段：id, conversations[from/value], category, source
- `tu8-safety-dialog-alpaca.jsonl` — Alpaca指令格式，字段：instruction, input, output, category, source

## 许可证

CC BY-SA 4.0 — 允许商业使用，衍生作品必须采用相同许可证。

## 引用

```bibtex
@dataset{tu8_safety_dialog_2026,
  title={TU-8 Safety Dialog Dataset},
  author={Jin Mu Chan},
  year={2026},
  license={CC BY-SA 4.0},
  url={https://www.modelscope.cn/datasets/Lxs945911/TU-8-Safety-Dialog}
}
```
