from load import loaddata
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split



### 파일 경로 입력하는 부분!! prodata 내의 파일을 불러와서 분석하면된다.
df = loaddata('prodata/traffic.csv')

line = []
start = []
dest = []


for i in range(0,len(df)):
    
    if df.loc[i]['출발영업소코드'] != 9999:
        word = str(df.loc[i]['출발영업소코드']) +'-'+ str(df.loc[i]['도착영업소코드'])
        revesreword = str(df.loc[i]['도착영업소코드']) +'-'+ str(df.loc[i]['출발영업소코드'])
        if word not in line and revesreword not in line: 
            line.append(word)
            start.append(df.loc[i]['출발지방향총교통량'])
            dest.append(df.loc[i]['도착지방향총교통량'])


x = np.array(start)
y = np.array(dest)

train_input, test_input, train_target, test_target = train_test_split(x,y,random_state =42)


train_input = train_input.reshape(-1,1)
test_input = test_input.reshape(-1,1)


lr = LinearRegression()

lr.fit(train_input, train_target)


print(lr.score(test_input,test_target))


xNDArray  = np.arange(min(x),max(x))
yNDArray  = lr.coef_ * xNDArray + lr.intercept_


print(lr.coef_)

plt.plot(xNDArray, yNDArray, ls = "dashed", lw = 3, color = "b", label = "original")

plt.scatter(start, dest)
plt.show()


