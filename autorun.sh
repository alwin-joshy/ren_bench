#!/bin/bash

if [ $1 = "--help" ]
then
	echo "Usage $0 benchmark num_runs time_per_run heapsize folder_suffix"
	exit
fi 

if (($# != 5))
then
	echo "Invalid number of args"
	exit
fi

benchmark=$1
runs=$2
time_per_run=$3
heapsize=$4
suffix=$5

if [ -d "${benchmark}_$suffix" ]
then
	echo "folder already exists"
	exit
fi

mkdir ${benchmark}_$suffix

i=0
while [ $i -le $runs ]
do
	java -Xmx$heapsize -jar renaissance-gpl-0.14.2.jar --no-forced-gc --csv \
	     ${benchmark}_$suffix/res$i --operation-run-seconds $time_per_run $benchmark
	((i++))
done


