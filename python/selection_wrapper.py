#!/usr/bin/python3
#TODO Run commands, do not print them
import argparse
import glob
import pathlib
import subprocess
import sys

collection_script = 'scripts/trace_collect.py'
MCNT_CONFIGURATIONS = ['003.000.000', '113.111.111', '223.222.222', '333.333.333']

parser = argparse.ArgumentParser(description = 'Select inter-core interference relevant performance monitoring counters')
parser.add_argument('--output', '-o',  help='Output traces and files prefix')
parser.add_argument('--runs', '-c',  help='Number of runs to collect', type=int, default=2000)
parser.add_argument('--contention-on', '-s',  help='Set contention against specified core', type=int, choices=[0, 1, 2], default=0)
parser.add_argument('--randomise', '-x',  help='Active static software-randomisation', action='store_true')
parser.add_argument('--seed',  help='Seed for software randomisation, use run id per default', type=int)
parser.add_argument('--root-id',  help='Analysed task root id', type=int)
parser.add_argument('ude_configuration',  help='UDE platform configuation')
parameters = parser.parse_args()

if not pathlib.Path(parameters.ude_configuration).is_file():
    raise ValueError("UDE platform configuration '%s' does not exist" % (parameters.ude_configuration))

assert parameters.runs > 0
assert parameters.output

collection_flags = []
collection_flags.append(parameters.ude_configuration)
collection_flags.extend(['--runs', str(parameters.runs)])
collection_flags.extend(['--contention-on', str(parameters.contention_on)])

if parameters.randomise:
    collection_flags.extend(['--randomise'])
    if parameters.seed is not None:
        collection_flags.extend(['--seed', str(parameters.seed)])

# Collect runs for each mcnt
for mcnt in MCNT_CONFIGURATIONS:
    command = [collection_script]
    command.extend(collection_flags)
    command.extend(['--output', '%s.mcnt%s' % (parameters.output, mcnt)])
    command.extend(['--mcnt', mcnt])

    status = subprocess.call(command)
    assert pathlib.Path('%s.mcnt%s.run0.C%d.csv' % (parameters.output, mcnt, parameters.contention_on)).is_file(), "Missing demuxed trace file"

# Merge results accross MCNT
analysed_runs = []
for run in range(0, 1 if not parameters.randomise else parameters.runs):
    for core in range(0,3):
        output_file = '%s.run%d.C%d.csv' % (parameters.output, run, core)
        command = ['scripts/trace_combine.py']
        command.extend(['--output', output_file])
        command.extend(['%s.mcnt%s.run%d.C%d.csv' % (parameters.output, mcnt, run, core) for mcnt in MCNT_CONFIGURATIONS])

        status = subprocess.call(command)
        print(command)
        #assert pathlib.Path(output_file), "Missing merged trace file '%s'" % (output_file)
        
        if core == parameters.contention_on:
            analysed_runs.append(output_file)

# Extract runs timings from trace
rvds = glob.glob('build/output/core%d.rvd' % (parameters.contention_on), recursive=True)
assert rvds, "Analysed core rvd could not be found"

command = ['scripts/trace_to_runs.py']
command.extend(['--rvd', rvds[0]])
if parameters.root_id:
    command.extend(['--root-id', str(parameters.root_id)])
command.extend(analysed_runs)
#TODO Redirect output to OUTPUT_runs.csv
print(command)
with open('%s_runs.csv' % parameters.output, mode='wb') as ofile :
    status = subprocess.call(command, stdout=ofile)

# Select relevant factors
#TODO Integrate R analysis script and factor selection
print('Rscript < %s_runs.csv > %s_loadings.csv' % (parameters.output, parameters.output))
print('Selection < %s_loadings.csv > %s_mcnt.txt' % (parameters.output, parameters.output))
