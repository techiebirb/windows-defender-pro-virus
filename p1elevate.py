import ctypes,sys
from tkinter import *
from tkinter import messagebox

def elevate_and_run_command(command):
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", "/c " + command, None, 1)
    except:
        print("Error elevating privilege or running command")

root = Tk()
root.withdraw()

result = messagebox.askyesnocancel(title="WARNING", message="""This program is MALWARE and is for educational purposes only. The creator isn't responsible for any damage.\n
DO NOT run this program if you don't know what this is, and IMMEDIATELY PRESS NO or CANCEL. If you know what you are doing, go ahead at your own risk.\n
CONTINUE?""")
if not result:
    sys.exit()

result = messagebox.askyesnocancel(title="WARNING", message="""AGAIN! This program is MALWARE and is for educational purposes only. The creator isn't responsible for any damage.\n
DO NOT run this program if you don't know what this is, and IMMEDIATELY PRESS NO or CANCEL. If you know what you are doing, go ahead at your own risk.\n
CONTINUE?""")
if not result:
    sys.exit()



elevate_and_run_command("python && pause")
