# Day 1: Linux Basics & Project Setup

## Commands and What They Do

### Project Structure
- `mkdir -p ~/devops-sre-journey/{app,infra,scripts,logs}`  
  Creates the main project directory and subdirectories for app, infrastructure, scripts, and logs.

- `cd ~/devops-sre-journey`  
  Changes into the project directory.

- `pwd`  
  Prints the current working directory path.

- `ls -la`  
  Lists all files and directories, including hidden ones, with detailed info.

### File Inspection
- `cat logs/sample.log`  
  Prints the entire contents of the log file.

- `grep ERROR logs/sample.log`  
  Filters lines containing the word "ERROR".

- `grep -c ERROR logs/sample.log`  
  Counts the number of lines containing "ERROR".

- `tail -n 2 logs/sample.log`  
  Shows the last 2 lines of the log file.

- `cut -d' ' -f1 logs/sample.log | sort | uniq -c`  
  Extracts the first column (timestamp), sorts it, and counts unique occurrences. Used to see log volume per second.

### Process Management
- `sleep 300 &`  
  Starts a background process that sleeps for 300 seconds.

- `ps -ef | grep sleep`  
  Lists all processes and filters for "sleep".

- `jobs -l`  
  Shows background jobs with their PIDs.

- `kill <PID>`  
  Terminates the process with the given PID.

- `ps -ef | grep sleep | grep -v grep`  
  Verifies the process is gone (excludes the grep command itself).

### System Resources
- `df -h`  
  Shows disk usage of all filesystems in human-readable format.

- `free -h`  
  Shows memory usage (RAM and swap) in human-readable format.

- `uptime`  
  Shows how long the system has been running and the load average.

- `nproc`  
  Prints the number of processing units available.

### Network Inspection
- `ip addr show`  
  Displays IP addresses and network interfaces.

- `ss -tulpn`  
  Shows listening TCP/UDP ports with process names.

- `curl -I https://api.github.com`  
  Sends an HTTP HEAD request and shows response headers.

- `nslookup google.com` / `getent hosts google.com`  
  Resolves a domain name to an IP address.

### Running the App
- `python3 app.py`  
  Starts the REST API server on port 5000.

- In another terminal: `curl http://localhost:5000/health`  
  Returns `{"status": "UP"}`.

- `curl http://localhost:5000/api/v1/message`  
  Returns `{"message": "Hello from QA to DevOps"}`.

## Troubleshooting Exercise
Simulated a slow API with 503 errors. Investigated using:
- `uptime` and `top` to check CPU and load
- `ps aux --sort=-%cpu | head` to find high CPU process
- `free -h` and `df -h` for memory and disk
- `ss -tulpn | grep 5000` to confirm port listening
- `tail -f logs/sample.log` to watch logs

## Key Takeaways
- Linux is the foundation of DevOps.
- Knowing how to inspect files, processes, and system resources is essential for production troubleshooting.
- A structured approach (confirm problem, gather evidence, identify cause) is more important than memorizing commands.
