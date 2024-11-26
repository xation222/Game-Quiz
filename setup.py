import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["pygame"], "includes": ["json"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Puzzle Game",
    version="0.1",
    description="simple puzzle game",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)