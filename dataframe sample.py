import pandas as pd
import numpy as np
# Create the 'Temp' dataframe
temp_df = pd.DataFrame({'Temp': [1200.0, 1250.0, 1300.0, 1350.0, 1400.0],
                        'Slag': [80.0, 80.0, 80.0, 80.0, 80.0]})
x=[37.24, 27.42, 17.69, 4.08, 1.82, 0.37, 0.94, 1.56, 6.43, 1.15]
# Create the 'Composition' dataframe
composition_array = np.array(x)
composition_df = pd.DataFrame([composition_array]*5, columns=['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10'])

# Concatenate the dataframes along the second axis
result = pd.concat([temp_df, composition_df], axis=1)

composition_array.ndim
result.ndim
temp_df.ndim
print(result)


import numpy as np

# Create three arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])

# Concatenate the arrays
result = np.concatenate((arr1, arr2, arr3),axis=1)

print(result)  # Output: [1 2 3 4 5 6 7 8 9]

