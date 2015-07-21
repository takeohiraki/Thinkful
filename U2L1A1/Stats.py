import pandas as pd
from scipy import stats


# Data
data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.splitlines()
data = [i.split(', ') for i in data]

#Creates pandas data frame
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

# Mean, median, and range for Alcohol
meanA = df['Alcohol'].mean()
medianA = df['Alcohol'].median() 
modeA = stats.mode(df['Alcohol'])

# Mean, median, and range for Tobacco
meanT = df['Tobacco'].mean() 
medianT = df['Tobacco'].median() 
modeT = stats.mode(df['Tobacco']) 

# range, standard deviation, and variance of Alcohol
rangeA = max(df['Alcohol']) - min(df['Alcohol'])
stndA = df['Alcohol'].std() 
varA = df['Alcohol'].var() 

# range, standard deviation, and variance of Tobacco
rangeT = max(df['Tobacco']) - min(df['Tobacco'])
stndT = df['Tobacco'].std()
varT = df['Tobacco'].var()

# Prints data
print ("The mean for the Alcohol and Tobacco dataset is {0} and {1}".format(meanA, meanT))
print ("The median for the Alcohol and Tobacco dataset is {0} and {1}".format(medianA, medianT))
print ("The mode for the Alcohol and Tobacco dataset is {0} and {1}".format(modeA, modeT))
print ("The range for the Alcohol and Tobacco dataset is {0} and {1}".format(rangeA, rangeT))
print ("The stnd deviation for the Alcohol and Tobacco dataset is {0} and {1}".format(stndA, stndT))
print ("The variance for the Alcohol and Tobacco dataset is {0} and {1}".format(varA, varT))