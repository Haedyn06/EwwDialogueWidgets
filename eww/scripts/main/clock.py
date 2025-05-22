#!/usr/bin/env python3
from datetime import datetime
from datetime import date
import sys

arg = sys.argv[1] if len(sys.argv) > 1 else None

if arg == "--clock":
    print(datetime.now().strftime("%I:%M:%S %p"))
elif arg == "--date":
    print(f"[ {datetime.today().strftime("%A")}, {date.today()} ]")

# print(datetime.now().strftime("%I:%M:%S %p"))
# print(f"{datetime.today().strftime("%A")}, {date.today()}")