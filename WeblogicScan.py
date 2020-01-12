#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from app.main import pentest
from app.platform import Color

version = "1.3.1"

if len(sys.argv) < 3:
    print("Usage: python3 WeblogicScan [IP] [PORT]")
else:
    ip = sys.argv[1]
    port = int(sys.argv[2])
    pentest(ip, port)
