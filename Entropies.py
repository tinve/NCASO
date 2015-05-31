from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cmpy
import cmpy.inference.bayesianem as bayesem
from numpy import average
from scipy.stats.mstats import mquantiles

fname = '2D, T from 1.5 to 3.0.csv'

def sample_entropies(flips):

# takes modelset and symbol string, generates posterior distribution
# and returns list of hmu, Cmu and E, sampled over the posterior

    modelset = bayesem.LibraryGenerator(2, [1, 2, 3, 4])
    num_samples = 2000

    posterior = bayesem.ModelComparisonEM(modelset, flips, beta = 4.0, verbose = True)
    print 'Done.'

    hmu_list = []
    Cmu_list = []
    E_list = []

    for n in range(num_samples):
        (node, machine) = posterior.generate_sample()
        hmu = machine.entropy_rate()
        Cmu = machine.statistical_complexity()
        E = machine.excess_entropy()

        hmu_list += [hmu]
        Cmu_list += [Cmu]
        E_list += [E]

    return hmu_list, Cmu_list, E_list


data = pd.DataFrame.from_csv(fname)

data['flips'] = data['flips'].map(lambda x: list(x))
data = data.reset_index()

flip_list = list(data['flips'])

hmu_samples = []
Cmu_samples = []
E_samples = []

for n, flip in enumerate(flip_list):

     hmu, Cmu, E = sample_entropies(flip)

     hmu_samples += [hmu]
     Cmu_samples += [Cmu]
     E_samples += [E]

     print n

hmu_average = [average(x) for x in hmu_samples]
Cmu_average = [average(x) for x in Cmu_samples]
E_average = [average(x) for x in E_samples]

hmu_CI = [mquantiles(x, prob=[0.025, 1.0 - 0.025], alphap = 1.0, betap = 1.0) for x in hmu_samples]
Cmu_CI = [mquantiles(x, prob=[0.025, 1.0 - 0.025], alphap = 1.0, betap = 1.0) for x in Cmu_samples]
E_CI = [mquantiles(x, prob=[0.025, 1.0 - 0.025], alphap = 1.0, betap = 1.0) for x in E_samples]

hmu_low = [x[0] for x in hmu_CI]
Cmu_low = [x[0] for x in Cmu_CI]
E_low = [x[0] for x in E_CI]

hmu_high = [x[1] for x in hmu_CI]
Cmu_high = [x[1] for x in Cmu_CI]
E_high = [x[1] for x in E_CI]

data['hmu_samples'] = hmu_samples
data['Cmu_samples'] = Cmu_samples
data['E_samples'] = E_samples

data['hmu_average'] = hmu_average
data['Cmu_average'] = Cmu_average
data['E_average'] = E_average

data['hmu_low'] = hmu_low
data['Cmu_low'] = Cmu_low
data['E_low'] = E_low

data['hmu_high'] = hmu_high
data['Cmu_high'] = Cmu_high
data['E_high'] = E_high

data.to_csv(fname[:-4] + ', processed.csv')