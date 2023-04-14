#!/usr/bin/env python3
"""
This Python script plays a sound file using the playsound module.
"""

import sys
from playsound import playsound

if len(sys.argv) < 2:
    print("Usage: play_sound.py <sound_file>")
    sys.exit(1)

sound_file = sys.argv[1]
playsound(sound_file)
