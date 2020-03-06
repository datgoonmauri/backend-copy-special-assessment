#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
from testpath import commands

"""Copy Special exercise
"""


def get_special_paths(dir):
  filenames = os.listdir(dir)
  abs_path = os.path.abspath(dir)
  special_paths = []
  for filename in filenames:
    if re.search(r"__\w+__", filename):
      special_paths.append(os.path.join(abs_path, filename))
      print(os.path.join(abs_path, filename))
  return special_paths

def copy_to(paths, dir):
  abs_path = os.path.abspath(dir)
  if not os.path.exists(abs_path):
    os.makedirs(abs_path)
  for path in paths:
    shutil.copy(path, abs_path)

def zip_to(paths, zippath):
  cmd = "zip -j " + zippath + " '" + "' '".join(paths) + "'"
  print("command I'm going to do: " + cmd)
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    raise Exception(output)
    sys.stderr.write(output)
    sys.exit(1)
  print(output)

def main():

  args = sys.argv[1:]
  if not args:
    print( "usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)


  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print ("error: must specify one or more dirs")
    sys.exit(1)


  if todir:
    special_paths = get_special_paths(args[0])
    copy_to(special_paths, todir)
  elif tozip:
    special_paths = get_special_paths(args[0])
    zip_to(special_paths, tozip)
  else:
    print ("output is: " + str(get_special_paths(args[0])))
  
if __name__ == "__main__":
  main()