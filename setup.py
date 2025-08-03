import sys
from cx_Freeze import setup, Executable
import datetime
import pytz

base = None
if sys.platform == "win64":
    base = "Win64GUI"

executables = [
        Executable("COMPARADOR_DE_FUSOS.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = ["datetime", "pytz"],
        include_files = [],
        excludes = []
)




setup(
    name = "Comparador de Fusos",
    version = "1.0",
    description = "Faz comparações básicas de fusos de alguns países",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
