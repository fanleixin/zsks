import requests
import pandas as pd
from sqlalchemy import create_engine


class zsks:
    def __init__(self,url,tablename,engine):
        self.url = url
        self.tablename = tablename
        self.engine = engine

    def getdata(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
        data = requests.get(self.url)
        df = pd.read_json(data.text,encoding = 'UTF-8')
        df.to_sql(self.tablename,self.engine,if_exists='replace',chunksize=1000,index=False)
        print(df)
        
    def readata(self):
        rdata = pd.read_sql(self.tablename,self.engine)
        print(rdata)

url_jhyx = 'https://www.nm.zsks.cn/20gkwb/syjh/gkjh_20_31/data/jhyx.json'
url_jhzy = 'https://www.nm.zsks.cn/20gkwb/syjh/gkjh_20_31/data/jhzy.json'

url_tjyx = 'https://www.nm.zsks.cn/20gkwb/jdtj/gktj_20_31_21/data/tjyx.json'
url_tjzy = 'https://www.nm.zsks.cn/20gkwb/jdtj/gktj_20_31_21/data/tjzy.json'


tablename1 = 'jhyx'
tablename2 = 'jhzy'
tablename3 = 'tjyx'
tablename4 = 'tjzy'

engine = create_engine('mysql+pymysql://zsks:zsks@localhost:3306/zsks')


jhyx = zsks(url_jhyx,tablename1,engine)
jhzy = zsks(url_jhzy,tablename2,engine)
tjyx = zsks(url_tjyx,tablename3,engine)
tjzy = zsks(url_tjzy,tablename4,engine)


jhyx.getdata()
jhzy.getdata()
tjyx.getdata()
tjzy.getdata()
