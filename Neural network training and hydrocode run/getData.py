import numpy as np
import pandas as pd
from glob import glob

def getData(filename_root):

	filenames = glob(filename_root+'*')

	dataList = []

	column_names = ['Step', 'Time', 'Volume', 'Temp2d', 'Pxx', 'Pyy', 'Pzz', 'Pxy', 'Pxz', 'Pyz', 'Lz', 'Density', \
'Temp3d', 'Vx', 'Vy', 'Vz', 'displace', 'ddx', 'voidSize', 'S1', 'S2', 'S3']
	for fn in filenames:
	    dataSingle = pd.read_csv(fn, names=column_names, skiprows=1, delimiter=", ")
	    dataSingle['S3'] = dataSingle['S3']*-100000 # Conversion from bar to pascal for relevant values
	    dataSingle['S1'] = dataSingle['S1']*-100000
	    dataSingle['S2'] = dataSingle['S2']*-100000
	    
	    original_vol = dataSingle['Volume'][0]
	    volratio = dataSingle['Volume']/original_vol
	    dataSingle['volratio'] = volratio
	    
	    
	    L0 = dataSingle['Lz'][0]
	    hpicosecond = 0.01e-12
	    strain_rate = -1*(dataSingle['ddx']/(L0*hpicosecond))
	    dataSingle['strain_rate'] = -strain_rate
	    
	    old_S3 = dataSingle['S3'].shift(periods=1)
	    dataSingle['old_S3'] = old_S3
	    dataSingle['old_S3'][0] = dataSingle['S3'][0]

	    dataSingle['P2'] = (dataSingle['S1'] + dataSingle['S2'])/2.0

	    old_S1 = dataSingle['S1'].shift(periods=1)
	    dataSingle['old_S1'] = old_S1
	    dataSingle['old_S1'][0] = dataSingle['S1'][0]

	    old_S1 = dataSingle['S2'].shift(periods=1)
	    dataSingle['old_S2'] = old_S1
	    dataSingle['old_S2'][0] = dataSingle['S2'][0]
	    
	    old_P2 = dataSingle['P2'].shift(periods=1)
	    dataSingle['old_P2'] = old_P2
	    dataSingle['old_P2'][0] = dataSingle['P2'][0]

	    old_Temp2d = dataSingle['Temp2d'].shift(periods=1)
	    dataSingle['old_T'] = old_Temp2d
	    dataSingle['old_T'][0] = dataSingle['Temp2d'][0]

	    dataSingle['dS3'] = dataSingle['S3'] - dataSingle['old_S3']
	    dataSingle['dP2'] = dataSingle['P2'] - dataSingle['old_P2']
	    dataSingle['dS1'] = dataSingle['S1'] - dataSingle['old_S1']
	    dataSingle['dS2'] = dataSingle['S2'] - dataSingle['old_S2']
	    dataSingle['dT'] = dataSingle['Temp2d'] - dataSingle['old_T']


	    dataSingle['dS3dt'] = np.gradient(dataSingle['S3'], 1e-12)
	    dataSingle['dP2dt'] = np.gradient(dataSingle['P2'], 1e-12)
	    dataSingle['dTdt'] = np.gradient(dataSingle['Temp2d'], 1e-12)
	    
	    dataSingle['old_dS3dt'] = np.gradient(dataSingle['old_S3'], 1e-12)
	    dataSingle['old_dP2dt'] = np.gradient(dataSingle['old_P2'], 1e-12)
	    dataSingle['old_dTdt'] = np.gradient(dataSingle['old_T'], 1e-12)
	    
	    
	    dataList.append(dataSingle)
	    
	data = pd.concat(dataList, ignore_index=True)

	return data 



