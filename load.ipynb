from curses import color_content
import pandas as pd
import matplotlib as plt

###함수설명 (다운로드받고자 하는 경로, 최초유무(재사용시 디폴트 매개변수사용 최초다운시 매개변수 0전달), 필터)

def loaddata(url,k=-1,number=-1):


    if k==0:
      csv_test = pd.read_csv(url, encoding='CP949')
    else:
      csv_test = pd.read_csv(url)

    df = pd.DataFrame(csv_test)

    if k ==0:
      for i in range(1,7):
        col1 = '도착지방향'+str(i)+'종교통량'   
        col2 = '출발지방향'+str(i)+'종교통량' 
        df[col1] = pd.to_numeric(df[col1])
        df[col2] = pd.to_numeric(df[col2])


      df['도착지방향총교통량'] = pd.to_numeric(df['도착지방향총교통량'])
      df['출발지방향총교통량'] = pd.to_numeric(df['출발지방향총교통량'])

    
      df = df[(df['도착지방향총교통량']>=number) & (df['출발지방향총교통량']>=number)]


    return df


