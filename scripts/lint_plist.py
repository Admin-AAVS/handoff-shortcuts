#!/usr/bin/env python3
"""Lint Split for Discord shortcut plist. Exit 1 on any failure."""
from __future__ import annotations

import plistlib
import sys
from collections import Counter
from pathlib import Path

EXPECTED_IDS = [
    "is.workflow.actions.getclipboard",
    "is.workflow.actions.gettext",
    "is.workflow.actions.text.split",
    "is.workflow.actions.gettext",
    "is.workflow.actions.setvariable",
    "is.workflow.actions.repeat.each",
    "is.workflow.actions.gettext",
    "is.workflow.actions.count",
    "is.workflow.actions.conditional",
    "is.workflow.actions.appendvariable",
    "is.workflow.actions.setvariable",
    "is.workflow.actions.conditional",
    "is.workflow.actions.setvariable",
    "is.workflow.actions.conditional",
    "is.workflow.actions.repeat.each",
    "is.workflow.actions.appendvariable",
    "is.workflow.actions.count",
    "is.workflow.actions.repeat.each",
    "is.workflow.actions.setclipboard",
    "is.workflow.actions.alert",
    "is.workflow.actions.repeat.each",
    "is.workflow.actions.notification",
]


def fail(msg: str) -> None:
    print(msg)
    sys.exit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: lint_plist.py <plist>")
    path = Path(sys.argv[1])
    if not path.is_file():
        fail(f"missing plist: {path}")
    with path.open("rb") as f:
        try:
            data = plistlib.load(f)
        except Exception as e:
            fail(f"plistlib.load failed: {e}")

    actions = data.get("WFWorkflowActions")
    if not isinstance(actions, list):
        fail("WFWorkflowActions is not an array")

    ids = [a.get("WFWorkflowActionIdentifier") for a in actions]
    if ids != EXPECTED_IDS:
        fail(
            "identifier order mismatch\n"
            f"got:      {ids}\n"
            f"expected: {EXPECTED_IDS}"
        )

    uuids = []
    grouping = []
    for i, a in enumerate(actions):
        params = a.get("WFWorkflowActionParameters") or {}
        u = params.get("UUID")
        if not u:
            fail(f"action {i} {a.get('WFWorkflowActionIdentifier')} missing UUID")
        uuids.append(u)
        g = params.get("GroupingIdentifier")
        if g:
            grouping.append(g)

    dup = [u for u, n in Counter(uuids).items() if n > 1]
    if dup:
        fail(f"duplicate UUID(s): {dup}")

    counts = Counter(grouping)
    if not counts:
        fail("no GroupingIdentifier found")
    for g, n in counts.items():
        if n not in (2, 3):
            fail(f"GroupingIdentifier {g} appears {n} times; want 2 (repeat) or 3 (conditional)")

    repeat_groups = sum(1 for n in counts.values() if n == 2)
    cond_groups = sum(1 for n in counts.values() if n == 3)
    if repeat_groups != 2:
        fail(f"expected 2 repeat groups (count 2), got {repeat_groups}")
    if cond_groups != 1:
        fail(f"expected 1 conditional group (count 3), got {cond_groups}")

    print("PASS")


if __name__ == "__main__":
    main()
