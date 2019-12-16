# Simple DDOS Attacks Detector with sliding window

### Prerequisite
```Apache Kafka (Python API)```   
```Python 2.7 or above``` 

### Description
The program is able to identify potential DDOS attack on the fly from a given apache log file input.  
```Producer step```: The log messages are digested and put into Kafka stream.  
```Consumer step```: The log messages are sent to and read by consuming the Kafka stream.  
```Analysis step```: In this process, I kept track of three different datasets:  An array of the last X IP addresses seen (sliding window algorithm), a dictionary/hashmap of the how many times that IP address is in the sliding window array (improved time complexity over spacial complexity), and the list of culprit IP addresses for logging/output.  If any IP address shows up Y times in the last X IP addresses, it is flagged.

### Future steps
Improve detection system
  - Abnormal requests for the same document
  - Rate limiting type style where each IP has a given number of requests in a given time frame
  - Analysis on better default values
  
Improve logging
  - Duration of attack per IP
  - Number of occurances
  - IP addresses that were flagged around the same time (DDOS)
  
Spark
  - Initially was going to do this, but Spark dropped support for Python recently
  
Output result to API
  - Permanent data storage per run

Build UI to show historic runs
