#coding=utf-8
#  实现一个小游戏
import requests
from bs4 import BeautifulSoup
class First_PC(object):
  def __init__(self,url):
    self.url=url

  def start_get(self):
    response=requests.get(self.url)
    response.enconding='utf-8'
    soup = BeautifulSoup(response.text,"html.parser")
    for tag in soup.find_all('dl'):
      title=tag.find('a',class_='title')
      desc=tag.find('div',class_='desc')
      rank_star=tag.find('span',class_='rating_nums')
      if title !=None:
        print "*"*30
        print "书的标题是: ",title.string
        if desc !=None:
          print "书的描述是: ",desc.string
        if rank_star !=None:
          print "书的评分是: ",rank_star.string

first_pc=First_PC('https://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book')
first_pc.start_get()


# 使用python 实现了第一个简单的爬虫
# 学习了 使用 pip install 库名的 安装库的方法
# 学习了 最简单的 requests库的get用法
# 学习了 BeautifulSoup 的 find find_all .string 的用法
# 确实很方便 Life is short , I use python