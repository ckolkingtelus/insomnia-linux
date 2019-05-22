(copied from https://askubuntu.com/questions/524384/how-can-i-keep-the-computer-awake-depending-on-activity)

How to prevent the computer from falling asleep
If you are looking for a solution to keep your computer awake like Caffeine does (should do), the solution below should work; I tested it on 14.04. It exists of two small scripts that you should store together in one and the same folder. You can switch it of or on (toggle) with a key combination. Once you press it, it will show the current state in a message:

< image > < image >

It basically exists of a small background script that simulates a minor user action (keypress Ctrl) if idle time exceeds a defined amount of time, thus preventing the computer to go asleep or blank the screen. The keypress itself is meaningless and has no effect on playing video in full screen.

How to use
You will need to have xprintidle and xdotool installed:

sudo apt-get install xprintidle xdotool
(inotify-tools should be installed by default on Ubuntu, might not be the case on Xu- or Lubuntu)

The script below is to toggle on/off, copy it into an empty file, save it as insomnia.py (keep the name as it is!) and make it executable(!)

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
The (main) script below is to keep the computer awake, copy the script into an empty file, save it as caf.py (keep the name as it is!) and make it executable(!)
#!/usr/bin/env python3

import subprocess
import time

seconds = 120 # number of seconds to start preventing blank screen / suspend

while True:
    curr_idle = subprocess.check_output(["xprintidle"]).decode("utf-8").strip()
    if int(curr_idle) > seconds*1000:
        subprocess.call(["xdotool", "key", "Control_L"])
    time.sleep(10)
It is important that you keep both scripts in the same folder!

Now add a keyboard shortcut to toggle your Caffeine replacement on and off: "System Settings" > "Keyboard" > "Shortcuts" > "Custom Shortcuts"

Add the command:

/path/to/insomnia.py
To a key combination of your choice

That's it.
