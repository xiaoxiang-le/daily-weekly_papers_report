# 网络空间安全、AI、多模态与 Agent 论文日报与周报

论文查找使用 Undermind 插件：日报按四个方向分别检索，周报补检遗漏。论文研究问题、方法、证据边界和研究启发使用 ars-codex 的 academic-research-suite 分析；出版方与会议官方来源用于证据核验。运行前检查 Undermind 的实际连接状态，未连接或检索失败时明确记录受阻并保留待补窗口，详见 `WORKFLOW.md`。

本仓库由 Codex 定时任务维护，覆盖网络空间安全全领域，并独立监测 AI、多模态与 Agent 的基础方法、能力评测、系统与应用研究。新增方向无须具有安全或隐私关联；报告按四个方向分组，交叉论文通过领域标签去重。

自 2026-10-18 起，期刊主清单纳入有可靠证据核验的最新可查中科院一区、二区、三区论文；网络安全及 AI、多模态、Agent 相关顶会论文单列，期刊分区或影响因子未核验的论文进入候选区。首次按扩大后的范围运行时，对新增领域补检近 7 天，详见 `WORKFLOW.md`。

## 目录

- `reports/daily/YYYY/YYYY-MM-DD.md`：每日增量报告
- `reports/weekly/YYYY/YYYY-Www.md`：每周综合报告
- `state/seen_dois.txt`：已经报告的 DOI（用于去重）
- `WORKFLOW.md`：检索、筛选、核验、Zotero 导入与 Git 发布规范
- `scripts/validate_report.py`：报告结构校验器

日报默认每天 18:00（Asia/Shanghai）运行；周报默认每周五 18:30 运行。运行结果同时出现在 Codex 的“仪表盘/任务”中。

