import os
import time

def create_test_file(file_path, size_in_mb):
    """Create a test file of specified size in MB."""
    with open(file_path, 'wb') as f:
        f.write(os.urandom(size_in_mb * 1024 * 1024))

def measure_write_speed(file_path, size_in_mb):
    """Measure write speed in MB/s."""
    start_time = time.time()
    create_test_file(file_path, size_in_mb)
    end_time = time.time()
    return size_in_mb / (end_time - start_time)

def measure_read_speed(file_path, size_in_mb):
    """Measure read speed in MB/s."""
    start_time = time.time()
    with open(file_path, 'rb') as f:
        while f.read(1024 * 1024):  # Read in chunks of 1MB
            pass
    end_time = time.time()
    return size_in_mb / (end_time - start_time)

def main():
    # Ask the user for the drive letter
    drive_letter = input("Enter the drive letter (e.g., C, D, E) to test: ").strip().upper()
    if not drive_letter:
        print("No drive letter provided. Exiting.")
        return

    # Construct the test file path
    test_file_path = f"{drive_letter}:\\test_file.bin"

    # Configuration
    file_size_mb = 100  # Size of the test file in MB

    try:
        # Measure write speed
        print(f"Testing write speed on drive {drive_letter}:...")
        write_speed = measure_write_speed(test_file_path, file_size_mb)
        print(f"Write Speed: {write_speed:.2f} MB/s")

        # Measure read speed
        print(f"Testing read speed on drive {drive_letter}:...")
        read_speed = measure_read_speed(test_file_path, file_size_mb)
        print(f"Read Speed: {read_speed:.2f} MB/s")

    except PermissionError:
        print(f"Permission denied. Ensure you have write access to drive {drive_letter}:.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up
        if os.path.exists(test_file_path):
            os.remove(test_file_path)
            print("Test file deleted.")

if __name__ == "__main__":
    main()