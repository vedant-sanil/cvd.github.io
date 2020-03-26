#!/bin/bash
python3 update_index.py
git add .
git commit -a -m $1
git push "https://$2:$3@github.com/vedant-sanil/cvd.github.io.git"