from CoalClassification import coaltypefind
import pandas as pd

data = pd.read_csv('CoalData_Sample.csv',usecols=['Vdaf','Hdaf','G','Y','b'],dtype=str)
classifiedcoal =  []
for i in range(len(data)):
    type = coaltypefind(data.iloc[i])
    if type is False:
        type = ['Cannot Find']
    classifiedcoal.append(type)
classifiedcoal = pd.DataFrame(classifiedcoal)
print (classifiedcoal)
classifiedcoal.to_csv('Result.csv')
