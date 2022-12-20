from load import loaddata
import numpy as np



### 파일 경로 입력하는 부분!! prodata 내의 파일을 불러와서 분석하면된다.
df = loaddata('prodata/cc.csv')


def search(keyword):
    for i in range(0,len(df)):
        if df.loc[i]['출발영업소코드'] == keyword:
            print(df.loc[i]['출발영업소명'])
            return


search(645)
search(648)

