import pandas as pd
data = pd.read_csv('Python-exercise-file2 .csv', delimiter=(';'))
#print(data)
data1 = data
data1['familyname'] = data['lastname']
print(data)