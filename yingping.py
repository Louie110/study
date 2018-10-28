# coding:utf-8 
'''
练习内容：
1.抓取豆瓣最受欢迎影评多个字段
2.保存为json文件到本地
'''

#导入相关包
import requests
import json
from bs4 import BeautifulSoup

title_list = []
for i in range(0,60,20):
    url = 'https://movie.douban.com/review/best/?start=' + str(i)
    req = requests.get(url)
    soup = BeautifulSoup(req.content,'lxml') #对网页内容进行解析
    review_list = soup.find_all('div',class_ = 'main review-item')
    #title_list = [] #整合成列表
    for review in review_list:
        review_dic={}  #以字典的形式存储所需的字段内容
        review_dic['reviewer'] = review.find('a',class_ = 'name').text  #找出评论者
        review_dic['movie_name'] = review.find('img')['title']  #找出电影名
        review_dic['review_title'] = review.find('h2').text   #找出评论主题名
        review_dic['support'] = review.find('a',title='有用').text.strip()  #找出对评论者评论内容认可的人员数量
        review_dic['unsupport'] = review.find('a',title='没用').text.strip()   # 找出对评论者评论内容不认可的人员数量
        review_dic['reply'] = review.find('a',class_ = 'reply').text    #找出对评论做出回应的人数
        title_list.append(review_dic)    #将字典内容加入到列表中
        s = json.dumps(title_list,indent = 4,ensure_ascii=False)   #写入json文件
        with open('yingping.json','w',encoding = 'utf-8') as f:
            f.write(s)

#查看保存的json文件中的内容以及内容类型
with open('yingping.json','r',encoding = 'utf-8') as p:
    pf = p.read()
print(pf)
print(type(pf))

'''
对于在学习中遇到的困惑和失误做出总结如下：
1.编写代码要认真仔细，看清楚前后调用的变量 
2.对于个别需要用到的函数不懂时，要及时借助搜索引擎了解函数的使用方法
3.切记浮躁
'''