# Demonstration

```bash
cat emailheader.txt | fabric -p analyze_email_headers | tee headers.md

cat aws-flowlog.txt | fabric -p analyze_logs | tee flowlog.md

tcpdump -r dns-remoteshell.pcap -A | fabric -p analyze_logs -m gemini-2.0-flash-exp | tee remoteshell.md

fabric -u https://www.trendmicro.com/en_us/research/19/g/multistage-attack-delivers-billgates-setag-backdoor-can-turn-elasticsearch-databases-into-ddos-botnet-zombies.html | fabric -p analyze_malware -m gemini-2.0-flash-exp | tee malware.md

```

