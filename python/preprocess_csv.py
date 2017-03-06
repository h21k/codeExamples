#!/usr/bin/python3
import csv
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser(description = 'process aurix traces')
parser.add_argument('input', help='input CSV trace')
parser.add_argument('--output', help='output file (default: input.preprocessed.csv')
parser.add_argument('--filter-cores', help='comma separated list of cores to filter from results (e.g. c0,c1) (default: None)', default='')
parser.add_argument('--time-source', help='time source for rate (default: first field)', default=0)
parser.add_argument('--numerical-methods-filter', action='store_true', help='scale data to range 1-10')
parser.add_argument('--remove-constant-fields', action='store_true', help='Remove fields with constant value')
params = parser.parse_args()
if params.output is None:
  params.output = params.input.rpartition('.csv')[0] + '.preprocessed.csv'
filter_cores = [x.strip() for x in params.filter_cores.upper().split(',') if x.strip()]
with open(params.input) as f:
  fieldnames = f.readline().strip().split(',')
outfieldnames = [x for x in fieldnames if not any(x.startswith(core) for core in filter_cores)]

if isinstance(params.time_source, int):
  params.time_source = fieldnames[params.time_source]
outdata = []
fields_min = defaultdict(lambda: float('inf'))
fields_max = defaultdict(lambda: float('-inf'))
time_source = params.time_source
current_min = float('inf')
current_max = float('-inf')

with open(params.input, newline='') as f:
  indata = csv.DictReader(f)
  for row in indata:
    outrow = {}
    outdata.append(outrow)
    for key in row:
      if key and not any(key.startswith(core) for core in filter_cores):
        outval = int(row[key]) / int(row[time_source])
        outrow[key] = outval
        if outval < current_min: current_min = outval
        if outval > current_max: current_max = outval
        if outval < fields_min[key]: fields_min[key] = outval
        if outval > fields_max[key]: fields_max[key] = outval

if params.remove_constant_fields:
  for key in fields_min:
    if fields_min[key] == fields_max[key]:
      outfieldnames.remove(key)
      for row in outdata:
        row.pop(key, None)

if params.numerical_methods_filter:
  for row in outdata:
    for key in row:
      row[key] = (((row[key] - current_min) / (current_max - current_min)) * 9 ) + 1

with open(params.output, 'w', newline='') as f:
  writer = csv.DictWriter(f, outfieldnames)
  writer.writeheader()
  writer.writerows(outdata)

