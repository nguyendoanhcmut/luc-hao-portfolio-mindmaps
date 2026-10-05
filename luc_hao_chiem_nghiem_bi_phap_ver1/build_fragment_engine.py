#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fragment builder engine for Luc Hao Chiem Nghiem Bi Phap."""

import json
import os
import re
import sys

def read_text(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        return f.read()

def clean_paragraph(p):
    # Remove HTML comments, image links, table rows, horizontal rules
    lines = p.splitlines()
    clean_lines = []
    for l in lines:
        stripped = l.strip()
        if stripped.startswith("<!--") or stripped.endswith("-->"):
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            continue
        if re.match(r"^:?---+:?$", stripped):
            continue
        if re.search(r"!\[.*?\]\(assets/.*?\)", stripped):
            continue
        clean_lines.append(l)
    return "\n".join(clean_lines).strip()

def extract_case_details(paras, fig_lookup):
    # Analyze a case study / example block
    pass

print("Loaded builder helper")
