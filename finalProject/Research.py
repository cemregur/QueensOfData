import pandas as pd
from Src.conf import *
from Src.utils import *

set_display_options()
pd.options.display.float_format = '{:,.5f}'.format

df = pd.read_csv('Datasets/newproducts.csv', sep='\t', low_memory=False)
dfx = df.copy()
df.shape

