import os
import sys
import winreg
import ctypes

ENV_REG_PATH = r"//////"

def get_user_path():
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, ENV_REG_PATH, 0, winreg.KEY_READ) as key:
        try:
            value, _ = winreg.QueryValueEx(key, "PATH")
        except FileNotFoundError:
            value = ""
    return value


def set_user_path(new_path):
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, ENV_REG_PATH, 0, winreg.KEY_SET_VALUE) as key:
        winreg.SetValueEx(key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path)

    # notify system
    HWND_BROADCAST = 0xFFFF
    WM_SETTINGCHANGE = 0x1A
    ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, "Environment")


def add_to_path(dir_path):
    dir_path = os.path.abspath(dir_path)

    if not os.path.isdir(dir_path):
        print(f" dir not found: {dir_path}")
        return

    current_path = get_user_path()
    paths = current_path.split(";") if current_path else []

    if dir_path in paths:
        print("already in PATH")
        return

    paths.append(dir_path)
    new_path = ";".join(paths)

    set_user_path(new_path)

    print("added to PATH:")
    print(dir_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:")
        print("  python p.py <directory>")
        sys.exit(1)

    add_to_path(sys.argv[1])
