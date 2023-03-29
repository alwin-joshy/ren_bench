#!/bin/python3

import sys
import os
import csv
import numpy

def process(directory, warmup):
	num_files = 0
	file_results = []

	for filename in os.listdir(directory):
		f = os.path.join(directory, filename)
		# checking if it is a file
		if not os.path.isfile(f):
			continue

		with open(f, 'r') as file:
			ignore_count = 0;
			reader = csv.reader(file)
			results = []
			for row in reader:
				if (ignore_count == 0 or ignore_count <= int(warmup)):
					ignore_count += 1
					continue
				results.append(float(row[1]) / pow(10, 9))

			print(f"file {f}: Average: {numpy.average(results)}, std-dev: {numpy.std(results)}")
			file_results.append(numpy.average(results));

	print(f"Overall: {numpy.average(file_results)}")
				


if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print("Invalid number of arguments")
		exit(0)

	if (sys.argv[1] == "--help"):
		print(f"Usage: {sys.argv[0]} folder n_warmups")
		exit(0)

	process(sys.argv[1], sys.argv[2])
