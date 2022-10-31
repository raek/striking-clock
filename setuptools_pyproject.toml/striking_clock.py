"""Script to be run at each hour to produce the "BONG! BONG! BONG!"."""

from datetime import datetime
from pathlib import Path
from subprocess import run

from appdirs import user_config_dir


def main():
    hour = local_hour()
    script = strike_script_path()
    if script.exists():
        for _ in range(hour):
            run([script], check=True)
    else:
        print(" ".join(hour * ["BONG!"]))


def local_hour():
    return ((datetime.now().hour - 1) % 12) + 1


def strike_script_path():
    return Path(user_config_dir("striking-clock")) / "strike"
