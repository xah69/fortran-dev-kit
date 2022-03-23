#!/usr/bin/env bash

#input file
in_file=$1
#output file
out_file=$2

#compiling
gfortran $in_file -o $out_file
#running
./$out_file
