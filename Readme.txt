Log Monitoring and Analysing Script for WebServer

Overview
This Python script monitors a log file in real-time, counts HTTP requests, and saves the results upon termination using Ctrl+C. It also logs error messages and handles exceptions during the monitoring process.

Requirements

1. Python 3.x installed on your system
                 or 
   install on ubuntu using "apt install python3"
2. Access to the log file you want to monitor
3. Access to error logs directory (if applicable)

Installation and Usage

1. Open a terminal or command prompt.
2. Clone the repository your local machine.
   git clone https://github.com/ABHIMANYU43/Projectlog.git
3. Modify the script (log_monitor.py) to specify the path to your log file (LOG_FILE_PATH variable) and error pattern (ERROR_PATTERN variable).
4. Optionally, set the directory for error logs (ERROR_LOG_DIR variable) if error logs are stored separately.
5. Run the script using the command:

   python3 log_monitor.py

6. The script will start monitoring the specified log file in real-time.
7. View the total count of HTTP requests (excluding errors) displayed on the screen.
8. Press Ctrl+C to stop the script.
9. Upon stopping, the script will save the HTTP request counts to http_request_counts.txt in the current directory.

Script Details

Real-Time Monitoring: The script uses the tail command to monitor a log file and processes new log entries as they appear.

Error Detection: It identifies and logs error messages based on a specified error pattern (e.g., "ERROR", "Exception", "Failed").

HTTP Request Counting: The script extracts and counts HTTP status codes from log entries to track HTTP requests.

Summary Report: Upon termination (Ctrl+C), the script displays a summary report with total errors and HTTP status code counts.

Logging: The script utilizes Python's logging module to log monitoring details and error messages to a log file (log_monitor.log).
