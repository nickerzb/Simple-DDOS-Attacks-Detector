from __future__ import print_function
from kafka import KafkaConsumer
import time
from datetime import datetime
import json
import argparse

def get_ip(message):
  obj = json.loads(message.value)
  return obj["remote_host"]

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-rh', '--host', default="127.0.0.1:9092")
  parser.add_argument('-t', '--topic', default='small4')
  parser.add_argument('-w', '--window', default=400)
  parser.add_argument('-x', '--times', default=2)
  args = parser.parse_args()
  print('Starting the process...\n')
  start=datetime.now()
  consumer = KafkaConsumer(args.topic,
                         group_id='my-group',
                         bootstrap_servers=[args.host],
                         auto_offset_reset='earliest',
                         enable_auto_commit=False,
                         consumer_timeout_ms=1000)
  window = []
  kvs = {}
  culprits = set()

  for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    # print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
    #                                       message.offset, message.key,
    #                                       message.value))

    
    ip = get_ip(message)

    # if sliding window is full, remove head, decrement dictionary, remove from dict no value
    if len(window) >= args.window:
      oldIp = window.pop(0)
      kvs[oldIp] = kvs[oldIp] - 1
      if kvs[oldIp] == 0:
        kvs.pop(oldIp)

    # add ip to end of window
    window.append(ip)

    # we need to sync up the dictionary with what's in the window
    if not ip in kvs:
      kvs[ip] = 0
    kvs[ip] = kvs[ip] + 1

    # if the current IP has been recorded x amount of times, report it to unique set
    if kvs[ip] >= args.times:
      if not ip in culprits:
        print('FOUND CULPRIT IP: ', ip)
        culprits.add(ip)

    # logging/debugging
    # print('current ip: ', ip)
    # print(window)
    # print(kvs)
    # print(culprits)
    # print()
    # time.sleep(5)
  print('Process ended.')
  print('Time taken:', datetime.now()-start)
  print('All Culprits:')
  print("\n".join(culprits))

  filename = 'text-run.txt'
  # Clear old contents
  open(filename, 'w').close()
  # Write to file per requirements
  with open(filename, 'w') as f:
    f.write("\n".join(culprits))