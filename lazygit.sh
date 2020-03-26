#!/bin/bash
python3 modify_html.py
git init
git add .
git commit -m "$1"
git push "https://$2:$3@github.com/vedant-sanil/cvd.github.io.git"