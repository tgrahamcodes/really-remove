###############################################################
###	    Search and find ALL files related to your keyword   ###
###############################################################


def systemFileInfo(os, searchString):

    if os == "1" or os == "Windows":
        import os

        x32 = r"C:\Program Files (x86)"
        x64 = r"C:\Program Files"
        common32 = r"C:\Program Files (x86)\Common Files"
        common64 = r"C:\Program Files\Common Files"
        local = os.getenv("LOCALAPPDATA")
        local_low = os.path.join(os.getenv("USERPROFILE"), "AppData", "LocalLow")
        roaming = os.getenv("APPDATA")
        temp = os.getenv("TEMP")
        program_data = os.getenv("PROGRAMDATA")
        all_users = os.getenv("ALLUSERSPROFILE")
        windows = os.getenv("WINDIR") or r"C:\Windows"
        windows_temp = os.path.join(windows, "Temp")
        installer = os.path.join(windows, "Installer")
        sys32 = os.path.join(windows, "System32")
        syswow64 = os.path.join(windows, "SysWOW64")

        locations = [
            ("Program Files (x86)", x32),
            ("Program Files", x64),
            ("Program Files (x86) Common Files", common32),
            ("Program Files Common Files", common64),
            ("Local AppData", local),
            ("LocalLow AppData", local_low),
            ("Roaming AppData", roaming),
            ("ProgramData", program_data),
            ("All Users Profile", all_users),
            ("Windows", windows),
            ("Windows Temp", windows_temp),
            ("Windows Installer", installer),
            ("System32", sys32),
            ("SysWOW64", syswow64),
            ("Temp", temp),
        ]

        def search_path(label, directory):
            if not directory:
                return []

            matches = []
            try:
                for root, dirs, files in os.walk(directory, topdown=True):
                    for name in dirs + files:
                        if searchString.lower() in name.lower():
                            full_path = os.path.join(root, name)
                            matches.append(full_path)
                            print(f"Found {name} in {label} ({full_path})")
            except (PermissionError, FileNotFoundError):
                pass

            return matches

        print("\nSearch complete. \u2713\n")

        all_matches = []
        for label, directory in locations:
            all_matches.extend(search_path(label, directory))
        if not all_matches:
            print("No matching files or folders found.")
        else:
            # Remove duplicates and sort by path length descending (deepest first)
            all_matches = sorted(set(all_matches), key=len, reverse=True)
            print(f"\nFound {len(all_matches)} unique matching items.")
            response = (
                input("Proceed with delete on all these files/folders? (y/n): ")
                .strip()
                .lower()
            )
            if response == "y":
                import shutil
                import stat
                import subprocess

                deleted_count = 0
                error_count = 0

                def force_remove(path):
                    nonlocal deleted_count, error_count
                    if os.path.isfile(path):
                        # Try Python remove
                        try:
                            os.remove(path)
                            print(f"Deleted file: {path}")
                            deleted_count += 1
                            return
                        except:
                            pass

                        # Try chmod and remove
                        try:
                            os.chmod(path, stat.S_IWRITE)
                            os.remove(path)
                            print(f"Force deleted file: {path}")
                            deleted_count += 1
                            return
                        except:
                            pass

                        # Fallback to cmd del
                        try:
                            subprocess.run(
                                ["cmd", "/c", 'del /f /q "' + path + '"'],
                                shell=True,
                                check=True,
                                capture_output=True,
                            )
                            print(f"Force deleted file via cmd: {path}")
                            deleted_count += 1
                        except:
                            print(f"Failed to delete file: {path}")
                            error_count += 1

                    elif os.path.isdir(path):
                        # Try Python rmtree
                        def onerror(func, p, excinfo):
                            try:
                                os.chmod(p, stat.S_IWRITE)
                                func(p)
                            except:
                                pass

                        try:
                            shutil.rmtree(path, onerror=onerror)
                            print(f"Force deleted folder: {path}")
                            deleted_count += 1
                            return
                        except:
                            pass

                        # Fallback to cmd rd
                        try:
                            subprocess.run(
                                ["cmd", "/c", 'rd /s /q "' + path + '"'],
                                shell=True,
                                check=True,
                                capture_output=True,
                            )
                            print(f"Force deleted folder via cmd: {path}")
                            deleted_count += 1
                        except:
                            print(f"Failed to delete folder: {path}")
                            error_count += 1

                for path in all_matches:
                    force_remove(path)

                print(
                    f"\nDeletion summary: {deleted_count} items deleted, {error_count} errors."
                )
                if error_count > 0:
                    print(
                        "Note: Some items could not be deleted, likely due to permissions (run as admin)"
                    )
            else:
                print("Deletion cancelled. :( )")

        # Old
        # 		if searchString in file:
        # 			#print(f"{file} found in {i}.")
        # 			full_path = os.path.join(i, file)
        # 			print(f"Full path: {full_path}")
        # 			# 	if os.path.isfile(full_path):
        # 			# 		os.remove(full_path)
        # 		print(f"{file} removed successfully. \u2713")
        # 	elif os.path.isdir(full_path):
        # 		import shutil
        # 		shutil.rmtree(full_path)
        # 		print(f"{file} removed successfully. \u2713")
        # except Exception as e:
        # 	print(f"Error removing {file}: {e}")
        # else:
        # return 1

    # input("\nNow lets search the registry for any entries related to {file} and remove them if found.\n (y,n) ")


# if input()== "y" or input() == "Y":
##			import winreg
# try:
##				winreg.CloseKey(registry_key)
# print("Registry key for Adobe found at HKEY_CURRENT_USER\SOFTWARE\Adobe.")
# winreg.DeleteKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Adobe")
# print("Registry key for Adobe removed successfully. \u2713")
# except FileNotFoundError:
# print("Registry key for Adobe not found at HKEY_CURRENT_USER\SOFTWARE\Adobe.")

# elif(os == "Linux"):
# 	import os

# 	find = os.listdir("/")
# 	find_usr = [d for d in find if "usr" in d]
# 	find_bin = [d for d in find if "bin" in d]

# 	# Append the full path to the found directories
# 	find_file_usr = os.path.join("/", "usr")
# 	find_file_bin = os.path.join("/", "bin")

# 	print(f"/usr: {find_usr}")
# 	print(f"/bin: {find_bin}")

# elif ( os == "macOS"):
# 	import os

# 	find = os.listdir("/")
# 	find_app = [d for d in find if "Applications" in d]
# 	find_usr = [d for d in find if "usr" in d]

# 	# Append the full path to the found directories
# 	find_file_app = os.path.join("/", "Applications")
# 	find_file_usr = os.path.join("/", "usr")

# 	print(f"/Applications: {find_app}")
# 	print(f"/usr: {find_usr}")


if __name__ == "__main__":
    print("Select which operating system you are running:")
    # print("1. Linux")
    # print("2. macOS")
    # print("3. Windows")
    answer = input("Enter your os (linux, MacOS, Windows, etc): ")
    if answer.lower() in ["windows", "1"]:
        import ctypes

        def is_admin():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False

        if not is_admin():
            print(
                "Warning: Not running as administrator. If searching system directories, deletion may fail. Consider running as admin."
            )
    searchString = input("Enter the program you are searching for (e.g. Adobe): ")
    systemFileInfo(answer, searchString)

    # if (answer == "1"):
    # 	response = input("You are running Linux. Confirm with (Y/n) ")
    # 	if response == "y" or response == "Y":
    # 		if "Linux" in platform.system():
    # 			do_work("Linux")
    # 	else:
    # 		print("It looks like you are not running Linux. Please run the script again and select the correct operating system.")
    # elif (answer == "2"):
    # 	response = input("You are running macOS. Confirm with (Y/n) ")
    # 	if response == "y" or response == "Y":
    # 		if "macOS" in platform.system():
    # 			do_work("macOS")
    # 	else:
    # 		print("It looks like you are not running macOS. Please run the script again and select the correct operating system.")
# if (answer == "3"):
# 	response = input("You are running Windows. Confirm with (Y/n) ")
# 	if response == "y" or response == "Y":
# 		check_os = platform.system()
# 		if check_os == "Windows":
# 			systemFileInfo("Windows", "")
# 		else:
# 			print("It looks like you are not running Windows. Please run the script again and select the correct operating system.")
# else:
# 	print("Invalid input. Please run the script again and select a valid operating system.")
# 	systemFileInfo("Windows", "Adobe")
