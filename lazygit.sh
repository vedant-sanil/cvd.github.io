#!/bin/bash
python3 modify_html.py
git init
git add .
git commit -m 'Updated scripts for date-wise result generation'
git push "https://$2:$3@github.com/vedant-sanil/cvd.github.io.git"