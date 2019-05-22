#!/usr/bin/env python3
import os
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
try:
    pid = subprocess.check_output(["pgrep", "-f", "caf.py"]).decode("utf-8").strip()
    subprocess.Popen(["kill", pid])
    subprocess.Popen(["notify-send", "Computer doesn't stay awake..."])
except:
    subprocess.Popen(["/bin/bash", "-c", script_dir+"/"+"caf.py"])
    subprocess.Popen(["notify-send", "Computer stays awake..."])
