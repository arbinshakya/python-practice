import subprocess
import sys
import pyfiglet


cmd = sys.argv[1]

f = pyfiglet.Figlet(font='slant')

try:
    if cmd == "openbash":
        print(f.renderText("OPENING BASH"))
        
        subprocess.Popen(r"C:\Program Files\Git\git-bash.exe")
except Exception as e:
    print(f"Error: {e}")
