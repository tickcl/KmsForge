import subprocess
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def activate_windows(key, kms_server):
    subprocess.Popen(["slmgr.vbs", "/upk"], shell=True).wait()
    subprocess.Popen(["slmgr.vbs", "/cpky"], shell=True).wait()
    subprocess.Popen(["slmgr.vbs", "/ckms"], shell=True).wait()
    subprocess.Popen(["slmgr", "/ipk", key], shell=True).wait()
    subprocess.Popen(["slmgr", "/skms", kms_server], shell=True).wait()
    subprocess.Popen(["slmgr", "/ato"], shell=True).wait()

def main():
    if not is_admin():
        print("Please run this script as an administrator, we need this to access the Windows KMS and registry.")
        input("Press Enter to exit...")
        sys.exit(1)

    keys = {
        1: ("Windows 11 Pro", "W269N-WFGWX-YVC9B-4J6C9-T83GX"),
        2: ("Windows 11 Pro N", "MH37W-N47XK-V7XM9-C7227-GCQG9"),
        3: ("Windows 11 Pro for Workstations", "NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J"),
        4: ("Windows 11 Pro for Workstations N", "9FNHH-K3HBT-3W4TD-6383H-6XYWF"),
        5: ("Windows 11 Pro Education", "6TP4R-GNPTD-KYYHQ-7B7DP-J447Y"),
        6: ("Windows 11 Pro Education N", "YVWGF-BXNMC-HTQYQ-CPQ99-66QFC"),
        7: ("Windows 11 Education", "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2"),
        8: ("Windows 11 Education N", "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ"),
        9: ("Windows 11 Enterprise", "NPPR9-FWDCX-D2C8J-H872K-2YT43"),
        10: ("Windows 11 Enterprise N", "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4"),
        11: ("Windows 11 Enterprise G", "YYVX9-NTFWV-6MDM3-9PT4T-4M68B"),
        12: ("Windows 11 Enterprise G N", "44RPN-FTY23-9VTTB-MP9BX-T84FV"),
        13: ("Windows 10 Pro", "W269N-WFGWX-YVC9B-4J6C9-T83GX"),
        14: ("Windows 10 Pro N", "MH37W-N47XK-V7XM9-C7227-GCQG9"),
        15: ("Windows 10 Pro for Workstations", "NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J"),
        16: ("Windows 10 Pro for Workstations N", "9FNHH-K3HBT-3W4TD-6383H-6XYWF"),
        17: ("Windows 10 Pro Education", "6TP4R-GNPTD-KYYHQ-7B7DP-J447Y"),
        18: ("Windows 10 Pro Education N", "YVWGF-BXNMC-HTQYQ-CPQ99-66QFC"),
        19: ("Windows 10 Education", "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2"),
        20: ("Windows 10 Education N", "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ"),
        21: ("Windows 10 Enterprise", "NPPR9-FWDCX-D2C8J-H872K-2YT43"),
        22: ("Windows 10 Enterprise N", "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4"),
        23: ("Windows 10 Enterprise G", "YYVX9-NTFWV-6MDM3-9PT4T-4M68B"),
        24: ("Windows 10 Enterprise G N", "44RPN-FTY23-9VTTB-MP9BX-T84FV"),
        25: ("Windows 8.1 Pro", "GCRJD-8NW9H-F2CDX-CCM8D-9D6T9"),
        26: ("Windows 8.1 Pro N", "HMCNV-VVBFX-7HMBH-CTY9B-B4FXY"),
        27: ("Windows 8.1 Enterprise", "MHF9N-XY6XB-WVXMC-BTDCT-MKKG7"),
        28: ("Windows 8.1 Enterprise N", "TT4HM-HN7YT-62K67-RGRQJ-JFFXW"),
        29: ("Windows 8 Pro", "NG4HW-VH26C-733KW-K6F98-J8CK4"),
        30: ("Windows 8 Pro N", "XCVCF-2NXM9-723PB-MHCB7-2RYQQ"),
        31: ("Windows 8 Enterprise", "32JNW-9KQ84-P47T8-D8GGY-CWCK7"),
        32: ("Windows 8 Enterprise N", "JMNMF-RHW7P-DMY6X-RF3DR-X2BQT"),
        33: ("Windows 7 Professional", "FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4"),
        34: ("Windows 7 Professional N", "MRPKT-YTG23-K7D7T-X2JMM-QY7MG"),
        35: ("Windows 7 Professional E", "W82YF-2Q76Y-63HXB-FGJG9-GF7QX"),
        36: ("Windows 7 Enterprise", "33PXH-7Y6KF-2VJC9-XBBR8-HVTHH"),
        37: ("Windows 7 Enterprise N", "YDRBP-3D83W-TY26F-D46B2-XCKRJ"),
        38: ("Windows 7 Enterprise E", "C29WB-22CC8-VJ326-GHFJW-H9DH4"),
        39: ("Windows Vista Business", "YFKBB-PQJJV-G996G-VWGXY-2V3X8"),
        40: ("Windows Vista Business N", "HMBQG-8H2RH-C77VX-27R82-VMQBT"),
        41: ("Windows Vista Enterprise", "VKK3X-68KWM-X2YGT-QR4M6-4BWMV"),
        42: ("Windows Vista Enterprise N", "VTC42-BM838-43QHV-84HX6-XJXKV"),
    }


    print(r"""
 _  ____  __ ____  _____ ___  ____   ____ _____ 
| |/ /  \/  / ___||  ___/ _ \|  _ \ / ___| ____|
| ' /| |\/| \___ \| |_ | | | | |_) | |  _|  _|  
| . \| |  | |___) |  _|| |_| |  _ <| |_| | |___ 
|_|\_\_|  |_|____/|_|   \___/|_| \_\\____|_____|

Welcome to KmsForge - Your Windows Activator!

Visit our repository: https://github.com/somebodyscript/KmsForge/
          
Give please star for this repository :D

Available Windows versions:

""")

    for index, (version, key) in keys.items():
        print(f"{index}. {version}")

    choice = int(input("Choose a Windows version to activate (enter the corresponding number): "))

    if choice not in keys:
        print("Invalid choice. Exiting...")
        sys.exit(1)

    selected_version, key = keys[choice]
    kms_server = "kms8.msguides.com"

    print(f"Activating {selected_version}...")
    print(f"Just click OK buttons.")
    try:
        activate_windows(key, kms_server)
        print("Activation successful! Enjoy your new Windows!")
    except Exception as e:
        print(f"Error during activation: {e}")

if __name__ == "__main__":
    main()
