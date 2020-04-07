
import requests
from bs4 import BeautifulSoup
class teachers(object):
    def __init__(self):
        self.server = 'http://cs.bit.edu.cn/szdw/jsml/'
        self.target = 'http://cs.bit.edu.cn/szdw/jsml/index.htm'
        self.names = []
        self.urls = []
        self.research =[]

    #获取老师主页地址
    def get_url(self):
        req = requests.get(url=self.target)
    #print(req.encoding)  #查看网页返回的字符集类型
    #print(req.apparent_encoding) #自动判断字符集类型
        req.encoding="utf-8"
        html=req.text
        #print(html)
        bf = BeautifulSoup(html)
        teacher = bf.find_all('div', class_='teacher')
        for i in range(len(teacher)):
            div=teacher[i]
            a_bf=BeautifulSoup(str(div))
            a=a_bf.find_all('a')
            for each in a:
                self.names.append(each.string)
                if str(each.get('href'))[0:4]=='http':
                    self.urls.append(each.get('href'))
                else:
                    self.urls.append(self.server+each.get('href'))
    #获取老师介绍
    def get_contents(self,target):
        req=requests.get(url=target)
        req.encoding="utf-8"
        html=req.text
        bf = BeautifulSoup(html)
        texts=bf.find_all('div', class_='con_teacher')
        if texts==[]:
            return 'None'
        res=texts[0].text.replace('\xa0'*8,'\xa0')
        res=res.replace('\n\n','\n')
        #return res #将所有介绍都返回
        con=texts[0].find_all('div', class_='con01_t')
        for i in range(len(con)):
            research=con[i].find_all('h4', text='科研方向')
            if research !=[]:
                res = con[i].text.replace('\xa0','').replace('\n','').replace('科研方向','')
        return res
    def writer(self, path,name,text):
        write_flag = True
        with open(path,'a',encoding='utf-8') as f:
            f.write(name+'  ')
            f.writelines(text)
            f.write('\n')
if __name__=="__main__":
    t=teachers()
    t.get_url()

    for i in range(len(t.names)):
    #for i in range(3):
        texts=t.get_contents(t.urls[i])
        t.writer('研究方向汇总.txt',t.names[i],texts)

        #print(t.names[i]+'  '+texts)
        #print(t.urls[i])
        #print(texts)
