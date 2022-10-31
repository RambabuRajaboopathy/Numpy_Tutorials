from multiprocessing.sharedctypes import Value
import pandas as pd


d={}
data= pd.read_csv(r"Downloads\dataset.csv",sep=";")
# print(df)
# print("*"*100)

df=pd.DataFrame(data,columns=['date'])
df=df['date'].tolist()
print(df)
print("*"*100)




year_2020=[]
for date in df:
    x=date
    dot_pos=x.rfind(".")
    year=x[dot_pos+1:]
    if(year=='2020'):
        year_2020.append(x)
    
print(year_2020)





