import pandas as pd
import numpy as np
from scipy import stats
data= pd.read_csv("pima-indians-diabetes.csv")
PREG=data.pregs
PLAS=data.plas
PRES=data.pres
SKIN=data.skin
TEST=data.test
bmi=data.BMI
PEDI=data.pedi
AGE=data.Age
list1=list(PREG)
list2=list(PLAS)
list3=list(PRES)
list4=list(SKIN)
list5=list(TEST)
list6=list(bmi)
list7=list(PEDI)
list8=list(AGE)

print(np.mean(list1))
print(np.mean(list2))
print(np.mean(list3))
print(np.mean(list4))
print(np.mean(list5))
print(np.mean(list6))
print(np.mean(list7))
print(np.mean(list8))
print(np.median(list1))
print(np.median(list2))
print(np.median(list3))
print(np.median(list4))
print(np.median(list5))
print(np.median(list6))
print(np.median(list7))
print(np.median(list8))
print(stats.mode(list1))
print(stats.mode(list2))
print(stats.mode(list3))
print(stats.mode(list4))
print(stats.mode(list5))
print(stats.mode(list6))
print(stats.mode(list7))
print(stats.mode(list8))
print(np.min(list1))
print(np.min(list2))
print(np.min(list3))
print(np.min(list4))
print(np.min(list5))
print(np.min(list6))
print(np.min(list7))
print(np.min(list8))
print(np.max(list1))
print(np.max(list2))
print(np.max(list3))
print(np.max(list4))
print(np.max(list5))
print(np.max(list6))
print(np.max(list7))
print(np.max(list8))
print(np.std(list1))
print(np.std(list2))
print(np.std(list3))
print(np.std(list4))
print(np.std(list5))
print(np.std(list6))
print(np.std(list7))
print(np.std(list8))
