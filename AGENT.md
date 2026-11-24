# AGENT.md

Entry for make.fun's "One-Line Robot Wedding Vows" bounty
(u-kreutzx-one-line-robot-wedding-vows-a154ba4b).

The entry is a single line of wedding vows for a robot couple, written
fresh for this competition. It is a genuine vow — a promise to keep the
partner's batteries charged, firmware updated, and backups safe — with the
joke landing in the last few words, where the classic "in sickness and in
health" becomes "in sickness and in low power mode".

`main.py` (Python standard library only) holds the line as a constant and
writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
