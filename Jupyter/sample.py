import numpy
# import matplotlib.pyplot as plt
import pandas
import math
import sys
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import ExtraTreesClassifier

activity_removed=int(sys.argv[1])
input_file=sys.argv[2]

# fix random seed for reproducibility
numpy.random.seed(7)

# load the dataset
dataset = numpy.loadtxt(input_file, delimiter="\t")
removed=0
if (activity_removed>=0) and (activity_removed<=12):
	removed=1
	dataset=dataset[dataset[:,23] != activity_removed]
	for i,TP in enumerate(dataset):
		if dataset[i,23]>activity_removed:
			dataset[i,23]=dataset[i,23]-1

# Form sets
original_train_X = dataset[::2,0:23]
activity = [ int(x) for x in dataset[::2,23] ]
activity_total = numpy.zeros(13)
for i in range(1,len(activity)):
	activity_total[activity[i]] = activity_total[activity[i]] + 1
