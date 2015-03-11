#!/usr/bin/env python
# vim: set fileencoding=utf8

import argparse
import distutils.dir_util
import os.path
import re
import sys
import subprocess

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(THIS_DIR, 'objc_src')
GENERATED_DIRNAME = 'generated'
FILENAME_PLACEHOLDER = '__ALPREFIX__'
UPPER_PLACEHOLDER = '__ALPREFIX_UPPER__'
COMMON_PLACEHOLDER = '__ALPREFIX__'

def build(prefix):
  # first, copy file
  dest_path = os.path.join(THIS_DIR, GENERATED_DIRNAME, prefix)
  distutils.dir_util.copy_tree(SRC_DIR, dest_path)

  # second, modify file name
  for cur, dirs, files in os.walk(dest_path):
    for name in dirs + files:
      if name.find(FILENAME_PLACEHOLDER) != -1:
        os.rename(os.path.join(cur, name), os.path.join(cur, name.replace(FILENAME_PLACEHOLDER, prefix)))

  # last, modify file content
  prefix_upper = prefix.upper()
  for cur, dirs, files in os.walk(dest_path):
    for name in files:
      path = os.path.join(cur, name)
      upper_pattern = 's/%s/%s/g' % (UPPER_PLACEHOLDER, prefix_upper)
      common_pattern = 's/%s/%s/g' % (COMMON_PLACEHOLDER, prefix)
      upper_command = ['sed', '-i', '', upper_pattern, path]
      common_command = ['sed', '-i', '', common_pattern, path]
      ret = subprocess.call(upper_command)
      if ret != 0:
         print >> sys.stderr, 'ERROR: command:%s, return:%d' % (upper_command.__repr__(), ret)
         return
      ret = subprocess.call(common_command)
      if ret != 0:
         print >> sys.stderr, 'ERROR: command:%s, return:%d' % (common_command.__repr__(), ret)
         return

def main():
  description = 'build source code for additional logger.'
  parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument('--prefix', action='store', dest='prefix', help='prefix for AddtionalLogger, like the `NS` in `NSObject`')
  args = parser.parse_args()

  prefix = args.prefix
  if not prefix:
    print 'prefix:',
    prefix = raw_input()

  if not re.match('[a-zA-Z_]\w*', prefix):
    print >> sys.stderr, 'ERROR: prefix must be assembled by [a-zA-Z0-9_], and start by [a-zA-Z_]'

  build(prefix)

if __name__ == '__main__':
  main()

# vim: number list tabstop=2 shiftwidth=2 expandtab
