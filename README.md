# FILE-INTEGRITY-CHECKER

***COMPANY***: CDETECH IT SOLUTION

***NAME***: Sobiya vhora

***INTERN ID***: CT08GRD

***DOMAIN***: Cyber Security & Ethical Hacking

***BATCH DURATION***: December 25th, 2024 to January 25th, 2025

***MENTOR NAME***: Neela Santhosh

***DESCRIPTION OF TASK-1***
# File Integrity Checker

## Objective
A Python script designed to monitor and verify the integrity of files within a specified directory. By utilizing hashing algorithms, it ensures that any changes, additions, or deletions in files are detected and logged.

## Features

- **Hash Calculation**: Computes hash values of files using customizable algorithms (default: `sha256`).
- **Change Detection**: Detects modifications to existing files, new file additions, and deleted files.
- **Recursive Monitoring**: Scans directories recursively to ensure all files are monitored.
- **Periodic Monitoring**: Allows continuous monitoring with user-defined intervals.
- **Customizable**: Supports multiple hashing algorithms and configurable monitoring intervals.

## How It Works

The script operates in three main steps:

1. **Hash Calculation**:
   - Reads the file in chunks to handle large files efficiently.
   - Generates a hash value using a specified algorithm to uniquely identify file content.

2. **File Monitoring**:
   - Loads previously saved hash data from a JSON file (`hashes.json`).
   - Compares the current file hashes with stored hashes to detect changes.
   - Logs detected changes, including:
     - Modified files.
     - Newly added files.
     - Deleted or inaccessible files.

3. **Continuous Monitoring**:
   - Runs the monitoring process repeatedly at user-defined intervals.
   - Supports termination via keyboard interrupt (Ctrl+C).

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/file-integrity-checker.git
   ```
2. Navigate to the directory:
   ```bash
   cd file-integrity-checker
   ```
3. Ensure Python 3.8 or higher is installed.

## Usage

Run the script:
```bash
python file_integrity_checker.py
```

### User Inputs
- **Directory to Monitor**: Specify the directory path for monitoring.
- **Hash Algorithm**: Choose from supported algorithms (default: `sha256`).
- **Monitoring Interval**: Set the time in seconds between scans (default: 60 seconds).

### Example Output
```plaintext
=== File Integrity Checker ===
Enter the directory to monitor: /path/to/directory
Enter hash algorithm (default: sha256): sha256
Enter monitoring interval in seconds (default: 60): 120

--- Scanning Files ---
File: /path/to/file1.txt, Hash (sha256): abc123...
  [!] Change detected in file: /path/to/file1.txt

Changes detected! Hash data updated.
Monitoring will resume in 120 seconds...
```

## Error Handling
- Handles file access issues gracefully.
- Displays errors for invalid directory paths or inaccessible files.
- Provides fallback defaults for user inputs to ensure smooth operation.

## Applications
- **File Security**: Detect unauthorized file modifications.
- **Backup Validation**: Ensure backup files remain unchanged.
- **System Administration**: Monitor critical directories for changes.

## Customization
- **Hash Algorithm**: Use any supported hashing algorithm (e.g., `sha256`, `md5`).
- **Monitoring Interval**: Configure via user input for flexibility.
- **Hash Storage**: Stored in a JSON file (`hashes.json`) for easy management.





