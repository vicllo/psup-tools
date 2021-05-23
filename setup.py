import sys
import os
from cx_Freeze import setup, Executable
from includes import *

# ADD FILES
files = ['QtObjects/house.png']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="QtObjects/house.png"
)

# SETUP CX FREEZE
setup(
    name="Psup-Tools",
    version="1.0",
    description="Tool for Parcoursup",
    author="Victor L",
    options = {"build_exe": {"include_files": files}},
    executables = [target]

)