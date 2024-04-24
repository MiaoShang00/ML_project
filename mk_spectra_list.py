#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 14:24:04 2023

@author: magz
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from astropy.io import fits
import glob
import tqdm
import pandas as pd
import os

spectralist = sorted(glob.glob('*LJ1.fits'), key=os.path.getmtime)
nframes = len(spectralist)

wav = []
flux = []
err_flux = []
qual = []
flux_noss = []
err_flux_noss = []

for n in range(0,nframes):
    data = fits.open(str(spectralist[n]))
    spec = data[1].data
    wav.append(spec['WAVE'][0])
    flux.append(spec['FLUX'][0])
    err_flux.append(spec['ERR_FLUX'][0])
    qual.append(spec['QUAL'][0])
    flux_noss.append(spec['FLUX_NOSS'][0])
    err_flux_noss.append(spec['ERR_FLUX_NOSS'][0])
    
output_frame = {'WAVE': wav, 'FLUX': flux, 'ERR_FLUX': err_flux, 'QUAL': qual, 'FLUX_NOSS': flux_noss, 'ERR_FLUX_NOSS': err_flux_noss}

output = pd.DataFrame(output_frame)

output.to_pickle('spectra_list.pkl')


'''
data = fits.open('output/l1_data/PAQS_quasar_000005_z4.0_mag18.4_LJ1.fits')
spec = data[1].data

plt.plot(spec['WAVE'][0], spec['FLUX'][0])
'''

'''
data = fits.open('../abs_templates/PAQS_absorber_000090.fits')
spec = data[1].data

plt.plot(spec['LAMBDA'], spec['FLUX_DENSITY'])
'''