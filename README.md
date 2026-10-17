# 网络空间安全论文日报与周报

本仓库由 Codex 定时任务维护，覆盖网络空间安全全领域，包括网络与通信、系统与软件、密码学与隐私、硬件、云与供应链、工业互联网及 AI 与感知安全等方向。

自 2026-10-18 起，期刊主清单纳入有可靠证据核验的最新可查中科院一区、二区、三区论文；网络安全顶会论文单列，分区或影响因子未核验的论文进入候选区。首次按扩大后的范围运行时，对新增领域补检近 7 天，详见 `WORKFLOW.md`。

## 目录

- `reports/daily/YYYY/YYYY-MM-DD.md`：每日增量报告
- `reports/weekly/YYYY/YYYY-Www.md`：每周综合报告
- `state/seen_dois.txt`：已经报告的 DOI（用于去重）
- `WORKFLOW.md`：检索、筛选、核验、Zotero 导入与 Git 发布规范
- `scripts/validate_report.py`：报告结构校验器

日报默认每天 18:00（Asia/Shanghai）运行；周报默认每周五 18:30 运行。运行结果同时出现在 Codex 的“仪表盘/任务”中。

