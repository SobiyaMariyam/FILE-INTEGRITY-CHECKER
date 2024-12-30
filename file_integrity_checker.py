import hashlib
import os
import json
import time


def calculate_hash(file_path, hash_algorithm='sha256'):
    """
    Calculate the hash value of a file using the specified hash algorithm.
    :param file_path: Path to the file.
    :param hash_algorithm: Hash algorithm to use (default: sha256).
    :return: Hash value as a string or None if an error occurs.
    """
    try:
        hash_func = hashlib.new(hash_algorithm)
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        print(f"Error calculating hash for {file_path}: {e}")
        return None


def monitor_files(directory, hash_file='hashes.json', hash_algorithm='sha256'):
    """
    Monitor files in a directory for changes by comparing hash values.
    :param directory: Directory to monitor.
    :param hash_file: File to store hash data (default: hashes.json).
    :param hash_algorithm: Hash algorithm to use (default: sha256).
    """
    hash_data = {}

    # Load existing hash data if available
    if os.path.exists(hash_file):
        with open(hash_file, 'r') as f:
            hash_data = json.load(f)

    new_hash_data = {}
    changes_detected = False

    print("\n--- Scanning Files ---")
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path, hash_algorithm)

            if file_hash:
                print(f"File: {file_path}, Hash ({hash_algorithm}): {file_hash}")
                new_hash_data[file_path] = file_hash

                # Detect changes
                if file_path in hash_data:
                    if hash_data[file_path] != file_hash:
                        print(f"  [!] Change detected in file: {file_path}")
                        changes_detected = True
                else:
                    print(f"  [+] New file detected: {file_path}")
                    changes_detected = True
            else:
                print(f"  [!] Could not calculate hash for file: {file_path}")

    # Save updated hash data
    with open(hash_file, 'w') as f:
        json.dump(new_hash_data, f, indent=4)

    if not changes_detected:
        print("\nNo changes detected in files.")
    else:
        print("\nChanges detected! Hash data updated.")


def main():
    """
    Main function to run the File Integrity Checker tool.
    """
    print("=== File Integrity Checker ===")
    directory = input("Enter the directory to monitor: ").strip()

    if not os.path.exists(directory):
        print("Error: Directory does not exist.")
        return

    hash_algorithm = input("Enter hash algorithm (default: sha256): ").strip() or 'sha256'
    monitor_interval = int(input("Enter monitoring interval in seconds (default: 60): ").strip() or 1000)

    print("\nStarting File Integrity Checker...\n")
    try:
        while True:
            monitor_files(directory, hash_algorithm=hash_algorithm)
            print(f"\nMonitoring will resume in {monitor_interval} seconds...")
            time.sleep(monitor_interval)
    except KeyboardInterrupt:
        print("\nFile Integrity Checker stopped.")


if __name__ == "__main__":
    main()
