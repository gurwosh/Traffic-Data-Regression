from load import loaddata
import matplotlib.pyplot as plt
import numpy as np

df = loaddata('prodata/cc.csv')

df = df[  ((abs(df['도착지방향총교통량']-df['출발지방향총교통량'])/(df['도착지방향총교통량']+df['출발지방향총교통량']))*100 > 40 )]
df = df.reset_index(drop=True)

line = []
start = []
dest = []



for i in range(0,len(df)):
    
    if df.loc[i]['출발영업소코드'] != 9999:
        word = str(df.loc[i]['출발영업소코드']) +'-' + str(df.loc[i]['도착영업소코드'])
        revesreword = str(df.loc[i]['도착영업소코드']) +'-'+ str(df.loc[i]['출발영업소코드'])
        if word not in line and revesreword not in line: 
            line.append(word)
            start.append(df.loc[i]['출발지방향총교통량'])
            dest.append(df.loc[i]['도착지방향총교통량'])





plt.scatter(start, dest)
plt.show()
