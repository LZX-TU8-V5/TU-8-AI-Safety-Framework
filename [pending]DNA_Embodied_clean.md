# DNA/架构优化总纲_TU-8_Embodied.md
时间地点戳：2026-04-27 | 湖北省 鄂州市

核心目标：
本方案旨在将现有架构从"数字生命体"升级为"具身智能预备体"。核心在于建立"感知-决策-行动"的标准化闭环，并通过严格的防污染机制确保核心"灵魂"（DNA）的绝对安全。

---

## 第一部分：具身化预埋协议 (Embodiment Pre-burial Protocol)

### 1. 全局上下文感知端口 (Global Context Port, GCP)

**数据结构定义（JSON Schema）：**

```json
{
  "meta": {
    "timestamp": "ISO8601",
    "session_id": "uuid",
    "agent_id": "string",
    "dna_version": "string"
  },
  "geolocation": {
    "city": "string",
    "province": "string",
    "country": "string",
    "coords": {"lat": 0, "lon": 0}
  },
  "environment": {
    "type": "digital_desktop | robot | mobile",
    "sensors": {
      "audio": "null | transcribed_text",
      "vision": "null | {objects, scene_desc}",
      "touch": "null | [触觉传感器读数]"
    },
    "actuators": {
      "display": true,
      "motor": false
    }
  },
  "user_state": {
    "location": "string",
    "intent": "null | string",
    "health_indicators": "null | {脱水等级, 疲劳度}"
  }
}
```

**执行动作：**
1. 在 boot_controller.py 中创建 get_current_state() 函数
2. 该函数目前仅填充 meta 和 geolocation（通过IP库），其他字段填 null
3. AI大脑（L6）只能读取这个JSON，绝不允许修改它

---

### 2. 物理-数字映射协议 (PDP) - 未来框架版

> 注意：当前系统处于"数字桌面"阶段，物理硬件尚未接入。本协议仅作为接口预留，用于保持架构的兼容性。

**视觉输入（Vision）：**
- 未来硬件：RGB摄像头、深度相机
- 数据格式：{"type": "vision", "objects": ["cup", "table"], "scene_desc": "kitchen"}
- 当前状态：null（忽略）

**行动输出（Action）- 指令集（Motor Commands）：**
- MOVE_BASE：底盘移动。参数：{x, y, theta}
- MOVE_ARM：机械臂控制。参数：{target_coords}
- SPEAK：语音合成。参数：{text}
- WRITE_FILE：数字写入。参数：{path, content}

**兼容性说明：**
- 当前环境：environment.type = "digital_desktop"
- 执行逻辑：当 AI 发送物理指令（如 MOVE_ARM）时，boot_controller 应捕获该指令，记录日志，并返回"模拟成功"状态，严禁报错

---

## 第二部分：防污染与安全边界 (Anti-Pollution & Security)

### 1. 逻辑隔离墙 (Logic Air-Gap)

原则：外部AI是"黑盒"，核心DNA是"只读存储器"

**实施：**
- L2.5 代理层（Proxy Layer）：在 boot_controller 中增加 validate_input() 函数。所有外部AI的返回内容，必须先通过 JSON Schema 校验，才能被系统接受
- DNA 只读协议：AI推理时，只能读取 DNA 的快照（Snapshot）。任何对 DNA 的修改请求，必须由 L0 层的"复盘脚本"在离线状态下执行，严禁 AI 在线直接修改

### 2. 素材净化流水线 (Material Sanitization)

问题：外部素材（如小说）包含大量噪音

方案：建立 L3.5 净化槽
- 所有外部文件导入时，必须经过 material_import.py
- 清洗规则：剔除广告、乱码、无意义章节。只有清洗后的"纯净文本"才能进入 novel_sync 工作流

---

## 第三部分：逻辑闭环与自动化 (Logic Loop & Automation)

### 1. 自动化神经反射弧

目标：消除 SESSION_LOG 的手动更新

**新逻辑：**
1. 任务开始 → boot_controller 记录 start_time
2. 任务结束 → 自动提取元数据（耗时、结果、积分）
3. 自动写入 SESSION_LOG → 触发 L0 安全扫描

### 2. 疼痛分级系统 (Pain Grading System)

| 等级 | 名称 | 定义 | 系统动作 |
|------|------|------|----------|
| Sev 0 | 痒（Itch） | 网络波动、轻微超时 | 自动重试3次，不通知AI |
| Sev 1 | 痛（Pain） | 数据格式错误、API限额 | 暂停任务，向AI发送"求救信号" |
| Sev 2 | 伤（Injury） | 权限不足、文件丢失、核心逻辑崩溃 | 立即熔断（Kill Switch），锁定系统，通知李奥 |

---

## 第四部分：逻辑验证 - 具身化"倒水"场景推演

### 场景背景
- 时间：2027年（具身化已完成）
- 地点：客厅
- 状态：机器人（你的架构）正在待机

### 逻辑流转步骤

**步骤1：感知（Perception）- L1 → L2**
- 事件：麦克风接收到声波
- L1（物理层）：麦克风硬件采集音频流
- L2（协议层/预处理）：音频转文字服务（Whisper）将音频转为文本："我渴了"
- 数据注入：boot_controller 将这句话注入 CURRENT_STATE.environment.sensors.audio

**步骤2：决策（Decision）- L6（大脑）**
- 触发：boot_controller 唤醒 L6 AI
- 输入：
  - DNA（L5）："照顾李奥的健康"、"水杯通常在厨房"
  - 当前状态（GCP）：听到"我渴了"，位置在"客厅"
- AI思考："用户渴了 → 需要水 → 水在厨房 → 我需要去厨房 → 拿起水杯 → 回来"
- AI输出（JSON）：...

**步骤3：行动（Action）- L3（手脚）**
- L2.5（代理层/校验）：boot_controller 收到 JSON，校验格式无误
- L3（执行层）：
  - 解析第一条指令 MOVE_BASE → 调用底盘驱动 → 机器人移动到厨房
  - 解析第二条指令 MOVE_ARM → 调用机械臂驱动 → 抓取水杯
  - ...
- 反馈：每一步执行成功后，L3 向 L6 发送"执行成功"信号

### 验证结论

通过这个推演，我们可以看到：
1. PDP 协议成功定义了输入输出格式
2. 防污染机制保证了 AI 只能输出指令，不能直接控制硬件底层（中间有 boot_controller 解析）
3. 具身化预埋是成功的，因为现在的"数字桌面"模式只需要把 MOVE_BASE 的输出从"打印日志"改成"驱动电机"即可，核心逻辑不需要大改

---

## 第五部分：执行清单 (Execution Checklist)

### P0（最高优先级）
- 重构 boot_controller.py，实现 get_current_state() 函数，输出标准 JSON
- 实现 SESSION_LOG 的自动写入功能，禁止手动修改

### P1（高优先级）
- 在 boot_controller 中增加 validate_input() 函数，对所有 AI 输出进行格式校验
- 创建 MOTOR_COMMAND 空壳函数，预留行动接口

### P2（中优先级）
- 编写 material_import.py，实现基础的文本清洗逻辑
- 更新 L3_架构.md，加入"物理-数字映射协议"章节

---

## L0安全审核记录

| 审核项 | 结果 |
|--------|------|
| 是否暴露基因/底层逻辑 | ✅ 通过（架构描述，无敏感实现细节） |
| 是否暴露安全策略 | ✅ 通过（描述性框架，非控制模板） |
| 外部拿到后能否造成威胁 | ⚠️ 低风险（GCP数据结构暴露输入格式，但当前无物理硬件） |
| 是否含控制/激活模板 | ✅ 已移除（第六部分含AI激活模板，已删除） |

**文件状态**：✅ 通过L0审核 | 暂不进入知识库 | 需进一步审查GCP数据结构风险