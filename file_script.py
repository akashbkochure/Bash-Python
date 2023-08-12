#!/usr/bin/env python

import sys

print("Received files:")

for file in sys.stdin:
    file = file.strip()
    print(file)
    
# ls | python3 file_script.py
