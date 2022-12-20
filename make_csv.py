from load import loaddata
import pandas as pd


###CSV저장 함수(다운로드받고자하는 url, 저장하고자 하는 파일이름, 필터,mergy option 유무)
def make_csv(target_url,save_name,number=0,merge=False):
    if merge == True:
        
        df = loaddata('folder/2.csv',0,number)

        for i in range(3,5):
            df1 = loaddata('folder/'+str(i)+'.csv',0,number)
            pd.concat([df, df1], axis = 0)

    else:    
        df = loaddata(target_url,0,number)
    
    df.to_csv('prodata/'+save_name, index = False)



###traffic2 파일에서 값을 가져와 출발,도착 방향 총교통량이 1000이상인곳을 필터링하여 traffic으로 저장

make_csv('',"merge.csv",100,True)
