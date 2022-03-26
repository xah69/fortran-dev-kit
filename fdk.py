#!/usr/bin/python3

import os
import sys

options = sys.argv[1] 

if options == "i":
 os.system("python3 init.py")
elif options == "r":
 os.system("exit.py")
elif options == "e":
 arg1 = sys.argv[2]
 arg2 = arg1.split(".")
 cmd = "run.sh " + arg1 + " " + arg2[0]
 os.system(cmd)
 cmd2 = "rm " + arg2[0]
 os.system(cmd2)
