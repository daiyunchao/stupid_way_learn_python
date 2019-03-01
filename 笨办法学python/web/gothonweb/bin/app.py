# -*- coding:utf-8 -*-  
import web
from map import *
import pdb
urls=(
        '/game','GameEngine',
        '/','Index',
)

app=web.application(urls,globals())
if web.config.get('_session') is None:
        store = web.session.DiskStore('sessions')
        session = web.session.Session(app,store,initializer={'room':None,'count':0})
        web.config._session = session
else:
        session = web.config._session
render=web.template.render('templates/',base="layout")

class Index(object):
        def GET(self):
                session.room = START
                #输入错误密码次数初始化
                session.count = 0 
                web.seeother("/game")

class GameEngine(object):
        def GET(self):
            if session.room:
                return render.show_room(room=session.room)
            else:
                #场景为None，则跳转到death界面
                return render.you_died()
    
        def POST(self):
                form = web.input(action=None)
                if session.room and form.action:
                        result = session.room.go(form.action)
#                       pdb.set_trace()
                        #如果你输错10次，炸弹将永远被锁住无法取出
                        if session.room.name=='Laser Weapon Armory' and (result==None or result.name=='death') and session.count<10:
                                #输入错误密码次数累计
                                session.count=session.count+1
                        else:
                                session.room = result
                web.seeother("/game")

if __name__=="__main__":
        app.run()