from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cmpy
import cmpy.inference.bayesianem as bayesem
from numpy import average
from scipy.stats.mstats import mquantiles
from random import seed
import subprocess
import timeout_decorator

fname = '2.5D, T from 1.0 to 4.0.csv'
machine_states = [1, 2, 3, 4]
T = 1.0
type = '2.5D, 8x8x2 spins'

@timeout_decorator.timeout(10)
def excess_entropy(machine):
    return machine.excess_entropy()

def nan_count(a):
    return sum(np.isnan(x) for x in a)

def drop_nans(a):
    return [x for x in a if not np.isnan(x)]

def sample_entropies(posterior, sequence_number, total):

    # returns list of hmu, Cmu and E, sampled over the posterior

    num_samples = 5000

    hmu_list = []
    Cmu_list = []

    for n in range(num_samples):

        (node, machine) = posterior.generate_sample()

        hmu = machine.entropy_rate()
        Cmu = machine.statistical_complexity()

        hmu_list += [hmu]
        Cmu_list += [Cmu]

        print 'sequence ' + str(sequence_number) + ' of ' + str(total) + ', sample ' + str(n)

    return hmu_list, Cmu_list


data = pd.DataFrame.from_csv(fname)
data = data.reset_index()
data = data[data['type'] == type]

print data.shape
print data.head()

data = data[abs(data['T']- T) < 1e-10]

print data.shape
print data.head()

flip_list = list(data['flips'])
# print flip_list

hmu_samples = []
Cmu_samples = []

for n, flip in enumerate(flip_list):

    modelset = bayesem.LibraryGenerator(2, machine_states)
    posterior = bayesem.ModelComparisonEM(modelset, flip, beta = 4.0, verbose = True)
    print 'Posterior inferred.'

    hmu, Cmu = sample_entropies(posterior, n, len(flip_list))

    hmu_samples += [hmu]
    Cmu_samples += [Cmu]

print hmu_samples
print Cmu_samples

hmu_average = [average(x) for x in hmu_samples]
Cmu_average = [average(x) for x in Cmu_samples]

hmu_CI = [mquantiles(x, prob=[0.025, 1.0 - 0.025], alphap = 1.0, betap = 1.0) for x in hmu_samples]
Cmu_CI = [mquantiles(x, prob=[0.025, 1.0 - 0.025], alphap = 1.0, betap = 1.0) for x in Cmu_samples]

hmu_low = [x[0] for x in hmu_CI]
Cmu_low = [x[0] for x in Cmu_CI]

hmu_high = [x[1] for x in hmu_CI]
Cmu_high = [x[1] for x in Cmu_CI]

hmu_err_low = np.subtract(hmu_average, hmu_low)
Cmu_err_low = np.subtract(Cmu_average, Cmu_low)

hmu_err_high = np.subtract(hmu_high, hmu_average)
Cmu_err_high = np.subtract(Cmu_high, Cmu_average)

data['hmu_samples'] = hmu_samples
data['Cmu_samples'] = Cmu_samples

data['hmu_average'] = hmu_average
data['Cmu_average'] = Cmu_average

data['hmu_err_low'] = hmu_err_low
data['Cmu_err_low'] = Cmu_err_low

data['hmu_low'] = hmu_low
data['Cmu_low'] = Cmu_low

data['hmu_err_high'] = hmu_err_high
data['Cmu_err_high'] = Cmu_err_high

data['hmu_high'] = hmu_high
data['Cmu_high'] = Cmu_high

data.to_csv(fname[:-4] + ', processed for T = ' + str(T) + '.csv')

# subprocess.call(['speech-dispatcher'])        #start speech dispatcher
subprocess.call(['spd-say', '"finished"'])
