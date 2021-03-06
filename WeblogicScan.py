#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from app.main import pentest
from app.platform import Color

version = "1.3.1"

if len(sys.argv) < 2:
    print("Usage: python3 WeblogicScan [IP]:[PORT]")
else:
    a = sys.argv[1].split(":")
    ip = a[0].strip()
    port = int(a[1].strip())
    pentest(ip, port)