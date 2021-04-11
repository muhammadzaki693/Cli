#!/usr/bin/env python
import argparse
import os
import sys
import time

parser = argparse.ArgumentParser(description='cool cli.', prog='cliname', usage='%(prog)s [options]')
parser.add_argument('--math','-m',help="mathematics",type=str)
parser.add_argument('--say','-s',help="saying your arg",type=str)
parser.add_argument('--dir','-d',help="list of directory",type=str)
parser.add_argument('--typewriter','-t',help="type writer", type=str)

args = parser.parse_args()
if args.math:
  print(eval(args.math))
elif args.say:
  print(args.say)
elif args.dir:
  for i in os.listdir(args.dir):
    print(i)
elif args.typewriter:
  for message in args.typewriter:
    sys.stdout.write(message)
    sys.stdout.flush()
    
    if message != "\n":
      time.sleep(0.1)
    else:
      time.sleep(1)