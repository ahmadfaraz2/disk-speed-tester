# Disk/USB Speed Checker Script

This Python script allows you to measure the read and write speeds of a disk or USB drive. It creates a test file on the specified drive, measures the time taken to write and read the file, and calculates the speed in MB/s.

## Features
- Measures **write speed** by creating a test file on the specified drive.
- Measures **read speed** by reading the test file back from the drive.
- Automatically cleans up the test file after the test.
- Works on both Windows and Unix-based systems (Linux/Mac).

## Requirements
- Python 3.x
- Administrative privileges (if testing on a system drive or restricted path)

## Installation
1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/ahmadfaraz2/disk-speed-tester
   cd disk-speed-checker
   ```

2. **Ensure Python 3 is installed**:
   - Check your Python version:
     ```bash
     python --version
     ```
   - If Python 3 is not installed, download and install it from [python.org](https://www.python.org/downloads/).

3. **No additional dependencies** are required, as the script uses only built-in Python modules (`os`, `time`).

## Usage
1. **Run the script**:
   ```bash
   python disk_speed_cherker.py
   ```

2. **Enter the drive letter**:
   - On Windows, enter the drive letter (e.g., `C`, `D`, `E`).
   - On Unix-based systems (Linux/Mac), enter the mount path (e.g., `/Volumes/MyUSB`).

3. **View the results**:
   - The script will display the **write speed** and **read speed** in MB/s.

### Example Output
```
Enter the drive letter (e.g., C, D, E) to test: E
Testing write speed on drive E:...
Write Speed: 45.32 MB/s
Testing read speed on drive E:...
Read Speed: 120.45 MB/s
Test file deleted.
```

## How It Works
1. **Write Speed Test**:
   - A test file of a specified size (default: 100 MB) is created on the drive.
   - The time taken to write the file is measured, and the write speed is calculated.

2. **Read Speed Test**:
   - The test file is read back from the drive.
   - The time taken to read the file is measured, and the read speed is calculated.

3. **Cleanup**:
   - The test file is automatically deleted after the test.

## Customization
- You can change the size of the test file by modifying the `file_size_mb` variable in the script (default: 100 MB).

## Troubleshooting
- **Permission Denied**:
  - Ensure you have write access to the drive.
  - Run the script with administrative privileges if necessary.

- **Invalid Drive Letter/Path**:
  - Ensure the drive letter or path is correct and the drive is properly mounted.

- **Large File Size**:
  - Ensure the drive has enough free space for the test file.


