# Security Professional's CLI Toolkit

## Essential Tools & Examples

- **Log Analysis**
  ```bash
  grep 'ERROR' auth.log | awk '{print $1,$2}' | sort | uniq -c
  ```

- **Network Monitoring**
  ```bash
  tcpdump -i eth0 'port 443' -w capture.pcap
  ```
  
- **Incident Response**
  ```bash
  # Quick filesystem changes check
  find / -mtime -1 -ls
  ```

- **Process Investigation**
  ```bash
  # Check for suspicious processes
  ps aux | grep -i '[d]aemon\|[s]erver' | sort -rk 3,3
  ```

- **File Integrity**
  ```bash
  # Generate & compare checksums
  find /etc -type f -exec md5sum {} \; > current_sums.txt
  diff current_sums.txt baseline_sums.txt
  ```
---