import sys

from pycaret.datasets import get_data
data = get_data('insurance')

from pycaret.regression import *

# s = setup(data, target = 'charges', session_id = 123)

# lr = create_model('lr')

s2 = setup(data, target = 'charges', session_id = 123,
           normalize = True,
           polynomial_features = True, trigonometry_features = True, feature_interaction=True, 
           bin_numeric_features= ['age', 'bmi'], silent = True)

lr = create_model('lr', verbose = False)

save_model(lr, sys.argv[1])


