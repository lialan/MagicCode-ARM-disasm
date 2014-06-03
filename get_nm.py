#!/usr/bin/python

import sys
import pickle
import commands

ARM_NM_NAME = 'arm-none-eabi-nm'

def main():
  if len(sys.argv) == 1:
    print "usage: " + sys.argv[0] + " sofile1.so + sofile2.so\n"
    return

  entries = {}


  for i in range (1, len(sys.argv)):
    name = sys.argv[i]
    libname = name[name.rfind('/')+1:].strip()
    result = commands.getstatusoutput(ARM_NM_NAME + ' -D ' + name)[1].split('\n')
    entries[libname] = []
    for l in result:
      ls = l.split()
      if len(ls) < 3: continue
      if ls[1] != "T": continue
      entries[libname].append((int(ls[0], 16), ls[2]))
    entries[libname].sort(key=lambda tup: tup[0])

  with open("/tmp/sopickle", "wb") as f:
    pickle.dump(entries, f)

if  __name__ =='__main__':
  main()
