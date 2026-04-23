## Find, and (really)Remove an Application (with all it's hidden junk)

This Python script is designed to help Windows users identify and forcibly remove potentially unwanted or "shady" software and associated files from their system. It performs a comprehensive search across key directories—including Program Files, AppData folders, Windows system paths, and temporary locations—for any files or folders containing a user-specified search term (e.g., "Adobe" for removing Adobe-related bloatware).

## Features

- **Recursive Search**: Scans deeply into subdirectories for matches, including hidden or system-protected areas.
- **Force Deletion**: Uses multiple methods (Python libraries and Windows commands) to delete stubborn files/folders, with permission handling and admin privilege checks.
- **Safety Prompts**: Lists all findings before deletion and requires explicit confirmation to proceed.

## Usage

1. Run the script with Python (preferably as administrator via PowerShell or Command Prompt).
2. Enter "Windows" when prompted for OS.
3. Input the search keyword (e.g., software name like "Adobe").
4. Review the listed matches.
5. Confirm deletion if desired—the script will attempt forceful removal.



---------------------------------------------------------------------------------------------------------------------------
❌❌*BE CAREFUL*❌❌
- *Note:* This tool is powerful and can permanently delete system files. Use with caution and only target unwanted software.
- Always back up important data first. Not responsible for any system damage or data loss.

### You have been warned!
❌❌❌❌❌❌❌❌
