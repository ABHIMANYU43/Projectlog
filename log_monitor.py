import subprocess
import re
import time
import logging
from collections import Counter

LOG_FILE_PATH = "/var/log/apache2/access.log"
ERROR_LOG_DIR = "/var/log/apache2"
ERROR_PATTERN = r"ERROR|Exception|Failed"  # Customize error pattern as needed
HTTP_STATUS_CODE_PATTERN = r'\b\d{3}\b'    # Pattern to match HTTP status codes

# Configure logging to a file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def monitor_log_file(log_file_path, error_pattern, http_status_code_pattern):
    try:
        logging.info(f"Monitoring log file: {log_file_path}")

        # Open the log file and move to the end
        tail_process = subprocess.Popen(['tail', '-F', log_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Initialize keyword counters
        http_status_code_counter = Counter()

        try:
            while True:
                line = tail_process.stdout.readline().strip()
                if line:
                    logging.info(f"New log entry: {line}")

                    # Extract and count specific HTTP status codes
                    http_status_codes = re.findall(http_status_code_pattern, line)
                    http_status_code_counter.update(http_status_codes)

                    # Calculate total HTTP requests (excluding errors)
                    total_http_requests = sum(count for code, count in http_status_code_counter.items() if not code.startswith('5'))
                    print(f"Total HTTP Requests (excluding errors): {total_http_requests}", end='\r')

        except KeyboardInterrupt:
            logging.info("Log monitoring stopped by user.")

            # Save HTTP request counts to a file
            save_http_request_counts(http_status_code_counter)

    except Exception as e:
        logging.error(f"Error occurred during log file monitoring: {e}")

def save_http_request_counts(http_status_code_counter):
    try:
        http_request_counts_file = 'http_request_counts.txt'
        with open(http_request_counts_file, 'w') as f:
            f.write("HTTP Request Counts:\n")
            for status_code, count in http_status_code_counter.items():
                f.write(f"{status_code}: {count}\n")

        logging.info(f"HTTP request counts saved to: {http_request_counts_file}")

    except Exception as e:
        logging.error(f"Error occurred while saving HTTP request counts: {e}")

if __name__ == "__main__":
    try:
        monitor_log_file(LOG_FILE_PATH, ERROR_PATTERN, HTTP_STATUS_CODE_PATTERN)
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")

