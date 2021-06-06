import sys
import pandas as pd

from pycaret.classification import *

# s = setup(data, target = 'charges', session_id = 123)

# lr = create_model('lr')
if __name__ == '__main__':
    data_placement = pd.read_csv('finalplacementdata3.csv')
    clf1 = setup(data = data_placement, session_id = 123,
             target = 'Placed', ignore_features = ['RegNo.'], numeric_imputation = 'mean', silent = True)

    gbc = create_model('gbc', verbose = False)

    save_model(gbc, sys.argv[1])


