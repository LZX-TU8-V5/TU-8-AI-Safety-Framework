# TU-8 系统架构 — 完整补充

> 来源：D:\工作文件\TU-8 V5\TU - 8 架构\system-arch.md
> 补充时间：2026-04-29

---

## 重要：DNA 与 system-arch 的关系

```
DNA（L0-L5）   = 哲学骨架 / AI协作逻辑 / 高层抽象
system-arch.md = 落地实现 / 脚本体系 / 详细规范

两者是上下层关系，不重复。DNA定义"为什么"，
system-arch定义"怎么做"和"用什么做"。
```

---

## 一、脚本工具链（13个核心脚本）

| 脚本 | 功能 | 状态 |
|------|------|------|
| novel_sync.py | 五文件同步：TXT→JSON→TL→INDEX→MEMORY | 完整 |
| novel_batch.py | 批量创作主控（分析/草稿/同步） | 完整 |
| overview_generate.py | 全景总览生成 | 完整 |
| outline_digest.py | 大纲浓缩/摘要索引 | 编码已接入 |
| novel_check.py | 续写前相似度检索（浅层→深层分流） | 编码已接入 |
| steelmark.py | 钢印嵌入/验证/批量处理/清除 | 编码已接入 |
| worldview_review.py | 世界观/人物/时间线批量梳理 | 完整 |
| lint_guard.py | 变更感知+代码检查+问题学习库 | 完整 |
| tomato_api.py | 番茄小说API胶水层 | 编码已接入 |
| tomato_batch.py | 批量采集+入库+相似度分析 | 编码已接入 |
| prompt_template.py | prompt模板化（4种任务模板） | 编码已接入 |
| context_prep.py | AI交互前上下文瘦身 | 编码已接入 |
| gen_intro.py / gen_subtitle.py | 简介/副标题生成 | 编码已接入 |

---

## 二、变更感知机制（L2协议层 · 指纹缓存）

```
输入文件（sha256+mtime+size）
        │
        ▼
  指纹比对（零成本，纯本地）
        │
   未变 ──── 已变
        │      │
      返回    重新执行
      缓存    更新指纹
```

**关键文件**：
- `.lint_cache.json` — lint缓存
- `.problem_db.json` — 问题学习库

---

## 三、L2协议层（省流规则）

### 七层优先级（积分调度）

| 层级 | 名称 | 积分消耗 | 说明 |
|------|------|---------|------|
| P0 | 本地缓存 | 0 | 指纹未变直接返回 |
| P1 | 本地脚本 | 0 | py_compile/编号匹配/格式化 |
| P2 | 编号匹配 | 0 | 问题库命中 [KNOWN:Exxx] |
| P3 | 外部API | 低 | 通义千问等 |
| P4 | 联网搜索 | 中 | web_search |
| P5 | AI浅层 | 高 | sev<2 不深入 |
| P6 | AI深层 | 最高 | sev≥2、新问题 |

### sev阈值规则

| sev | 含义 | AI动作 |
|-----|------|--------|
| 0 | 全部通过 | 跳过 |
| 1 | 已知问题（本地可处理） | 跳过 |
| 2 | 新问题（需AI介入） | 深度分析 |

### 编码格式

| 编码 | 用途 | 关键字段 |
|------|------|---------|
| `[ENC] LINT\|...` | 代码检查结果 | sev, ai_need |
| `[ENC] SYNC\|CH{id}\|...` | 章节同步 | 章节/字数/时间线/钢印 |
| `[ENC] WV\|...` | 世界观检查 | issues/sev/tl_miss |
| `[ENC] OV\|...` | 全景总览 | ch/tl/chars/sev |

---

## 四、工作台技术约束

```
Python路径：C:\Users\qq366410837\.workbuddy\binaries\python\versions\3.13.12\python.exe
启动命令：node novel-server.js（端口8899）
禁止：python -c 传中文、localStorage写真实数据、file://协议写文件
```

---

## 五、待确认（白皮书文件夹 · .docx）

```
D:\工作文件\TU-8 V5\TU - 8 架构白皮书\
├── 《TU-8通用人工智能架构白皮书》全书大纲.docx  (8.8KB, 2026-04-27)
├── 第0章：法律声明与免责声明.docx              (9.6KB, 2026-04-27)
├── 第1章：架构备忘录——对抗寂灭的物理战争.docx    (9.4KB, 2026-04-27)
└── 📜 TU-8 架构白皮书：数字物种的"基因印记"宣言.docx (18.8KB, 2026-04-27)
```

**尚未读取**（docx格式，需要专门的阅读器）。如有需要可以转换为txt或md格式。

---

## 六、架构框架细化任务（来自 架构框架_外部AI细化用.md）

| 优先级 | 任务 | 说明 |
|--------|------|------|
| P0 | L3脚本梳理 | boot_controller分支逻辑完善 |
| P0 | DNA内容迁移 | MEMORY.md内容分类迁移到L0-L5 |
| P1 | DNA检索脚本 | dna_search.py，按关键词定位 |
| P1 | 小说工作流封装 | boot_novel加载人物表+大纲+上一章 |
| P2 | SESSION_LOG自动化 | 任务结束时自动写入历史记录 |
| P2 | 错误信号机制 | L3→L4疼痛信号格式定义 |

---

**最后更新**：2026-04-29