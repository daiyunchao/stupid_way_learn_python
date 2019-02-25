try:
   from setuptools import setup
except ImportErrors:
   from distutils.core import setup


config={
  'description':'My Project',
  'author':'Dai YunChao',
  'url':'',
  'download_email':'312931671@qq.com',
  'version':'1.0',
  'install_requests':['nose'],
  'packages':['NAME'],
  'scripts':[],
  'name':'projectname'
}

setup(**config)
