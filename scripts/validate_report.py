from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_HEADINGS = (
    "执行摘要",
    "检索与筛选",
    "已核验论文",
    "候选与待核验",
    "研究启发",
    "Zotero",
    "局限性",
    "AI 辅助披露",
)

PAPER_FIELDS = (
    "期刊或会议",
    "核心价值思想",
    "主要内容",
    "研究 idea",
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a daily/weekly paper report.")
    parser.add_argument("report", type=Path)
    args = parser.parse_args()

    if not args.report.is_file():
        raise SystemExit(f"error: report does not exist: {args.report}")

    text = args.report.read_text(encoding="utf-8")
    missing = [name for name in REQUIRED_HEADINGS if name not in text]

    verified_section = text.partition("已核验论文")[2].partition("候选与待核验")[0]
    if verified_section.strip() and "本期无符合条件的新论文" not in verified_section:
        missing.extend(field for field in PAPER_FIELDS if field not in verified_section)

    if missing:
        print("error_count=" + str(len(missing)))
        for item in missing:
            print(f"missing: {item}")
        return 1

    print("error_count=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

