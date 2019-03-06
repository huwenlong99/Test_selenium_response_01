# import win32file
import pywin32


def getdrives():
    drives = []
    sign = win32.GetLogicalDrives()
    drive_all = ["A:\\", "B:\\", "C:\\", "D:\\", "E:\\", "F:\\", "G:\\", "H:\\", "I:\\",
                 "J:\\", "K:\\", "L:\\", "M:\\", "N:\\", "O:\\", "P:\\", "Q:\\", "R:\\",
                 "S:\\", "T:\\", "U:\\", "V:\\", "W:\\", "X:\\", "Y:\\", "Z:\\"]
    for i in range(25):
        if (sign & 1 << i):
            if win32.GetDriveType(drive_all[i]) == 3:
                drives.append(drive_all[i])
    return drives


def is_UDisk(drives):
    UDisk = []
    for item in drives:
        try:
            free_bytes, total_bytes, total_free_bytes = win32.GetDiskFreeSpaceEx(item)
            if (total_bytes / 1024 / 1024 / 1024) < 17:
                UDisk.append(item)
        except:
            break
    return UDisk


if __name__ == "__main__":
    drives = is_UDisk(getdrives())
    print(drives)
