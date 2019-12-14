# Simple DDOS Attacks Detector with sliding window

### Prerequisite
```Apache Kafka (Python API)```   
```Python 2.7 or above``` 

### Purpose
This project is educational purpose. The goal is to learn some basic concepts and to get some hands-on experience on Apache Spark and Kafka. 

### Description
The program is able to identify potential DDOS attack on the fly from a given apache log file input.  
```Producer step```: The log messages are digested and put into Kafka message queue.  
```Consumer step```: The log messages are sent to and read by Spark Streaming.  
```Analysis step```: A very simple logic is used to analyze the log messages and detect the potential DDOS attackers by using MapReduce from Apache Spark.

### Apache log message sample 
```155.156.168.116 - - [25/May/2015:23:11:15 +0000] "GET / HTTP/1.0" 200 3557 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; acc=baadshah; acc=none; freenet DSL 1.1; (none))"```  
For more information, please read the [apache log format](https://httpd.apache.org/docs/2.2/logs.html).

### Note 
The program is not run at scale. It is done with a single node pseudo cluster.  
It is also run in local host. 

### Future steps
Make the program scalable.  
Implement more sophisticated algorithm to detect DDOS attackers. 
