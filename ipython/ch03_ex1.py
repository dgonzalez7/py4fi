import warnings
warnings.simplefilter('ignore')

V0 = 17.6639
r = 0.01

import pandas as pd
h5 = pd.HDFStore('./source/vstoxx_data_31032014.h5', 'r')        
futures_data = h5['futures_data']  # VSTOXX futures data        
options_data = h5['options_data']  # VSTOXX call option data        
h5.close()

print futures_data

print options_data.info()

print options_data[['DATE', 'MATURITY', 'TTM', 'STRIKE', 'PRICE']].head()

options_data['IMP_VOL'] = 0.0    # new column for implied volatilities

from bsm_functions import *

tol = 0.5  # tolerance level for moneyness
for option in options_data.index:
    # iterating over all option quotes
    forward = futures_data[futures_data['MATURITY'] == \
                options_data.loc[option]['MATURITY']]['PRICE'].values[0]
      # picking the right futures value
    if (forward * (1 - tol) < options_data.loc[option]['STRIKE']
                             < forward * (1 + tol)):
        # only for options with moneyness within tolerance
        imp_vol = bsm_call_imp_vol(
                V0,  # VSTOXX value 
                options_data.loc[option]['STRIKE'],
                options_data.loc[option]['TTM'],
                r,   # short rate
                options_data.loc[option]['PRICE'],
                sigma_est=2.,  # estimate for implied volatility
                it=100)
        options_data['IMP_VOL'].loc[option] = imp_vol

print futures_data['MATURITY']    # select the column with name MATURITY

print options_data.loc[46170]    # select data row for index 46170

print options_data.loc[46170]['STRIKE']    # select only the value in column STRIKE for index 46170

plot_data = options_data[options_data['IMP_VOL'] > 0]

maturities = sorted(set(options_data['MATURITY']))
print maturities

import matplotlib.pyplot as plt         
# %matplotlib inline         
plt.figure(figsize=(8, 6))         
for maturity in maturities:             
	data = plot_data[options_data.MATURITY == maturity]               
	# select data for this maturity             
	plt.plot(data['STRIKE'], data['IMP_VOL'],                      
		label=maturity.date(), lw=1.5)             
	plt.plot(data['STRIKE'], data['IMP_VOL'], 'r.')         
plt.grid(True)         
plt.xlabel('strike')         
plt.ylabel('implied volatility of volatility')         
plt.legend()         
plt.show()

keep = ['PRICE', 'IMP_VOL']         
group_data = plot_data.groupby(['MATURITY', 'STRIKE'])[keep]         
print group_data

group_data = group_data.sum()         
print group_data.head()

print group_data.index.levels