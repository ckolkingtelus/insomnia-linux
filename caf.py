#!/usr/bin/env python3

import subprocess
import time

seconds = 120 # number of seconds to start preventing blank screen / suspend

while True:
    curr_idle = subprocess.check_output(["xprintidle"]).decode("utf-8").strip()
    if int(curr_idle) > seconds*1000:
        subprocess.call(["xdotool", "key", "Control_L"])
    time.sleep(10)
