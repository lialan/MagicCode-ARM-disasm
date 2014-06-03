#!/usr/bin/python

import re
import sys
import pickle

#sys.path.append("./darm")
import darm

def main():
  if (len(sys.argv) < 2):
    print "usage: " + sys.argv[0] + " logcat.txt"
    return

  entries = []

  with open("/tmp/sopickle", "rb") as f:
    entries = pickle.load(f)

  with open(sys.argv[1], "r") as f, open("/tmp/annotated_logcat.txt", "w") as d:
    lines = f.readlines()
    arm_line = re.compile('\<[\w,\.]+\>')
    for l in lines:
      prefix = l[:19]
      l = l[l.find(':')+2:] # there are 19 characters before 
      ls = l.split()
      son = arm_line.findall(l)
      if not son:
        d.write(prefix + l)
        continue
      son = son[0][1:-1]
      entry = entries[son]
      if not entry:
        d.write(prefix + l)
        continue
      address = int(ls[2][:-1], 16)
 
      #find the offset from the name list
      last_entry = (0, "UNKNOWN")
      for e in entry:
        ent_addr = e[0]
        if ent_addr > address:
          break
        else:
          last_entry = e
   
      #call darm to get the ARM disassembly
      dis = darm.disasm_armv7(int(ls[-1], 16))

      d.write(prefix + '<' + last_entry[1] + '+' + str(address-last_entry[0]) + '> ' + ls[1] + ' ' + ls[2] + ' ' + str(dis))
      d.write('\n')


if __name__ == "__main__":
  main()
