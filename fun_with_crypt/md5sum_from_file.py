#!/usr/bin/env python2.6
import hashlib
import sys

file_name = sys.argv[1]

with open(file_name) as file_to_check:
  # read contents of the file
  data = file_to_check.read()    
  # pipe contents of the file through
  md5_returned = hashlib.md5(data).hexdigest()

print md5_returned
