# -*- coding:utf-8 -*-                                                                                                                                  
class Room(object):
        def __init__(self, name, description): 
                self.name = name 
                self.description = description 
                self.paths = {}  
    
        def go(self, direction): 
                return self.paths.get(direction, None) 
    
        def add_paths(self, paths): 
                self.paths.update(paths)

central_corridor = Room("Central Corridor",
"""
#25外星战机入侵了你的飞船，并且摧毁了你的部队。你是最后一个幸存者，你的最终任务是从武器室拿到炸弹，将炸弹放在驾驶舱，跳进分离仓之后，炸掉飞船。
你现在正在往武器室跑去，这时，一个外星人跳了出来，可怕的红色皮肤，暗淡肮脏的牙齿，丑陋的服装围绕着他那充满憎恶的身体。他正在关闭通往武器室的大门，并且掏
出武器对准了你。
"""
)

laser_weapon_armory=Room("Laser Weapon Armory",
"""
幸运的是你知道外星人是由意念组成的。
你讲了一个你知道的外星笑话。
&$%@#$#%#@*&^$%$@#^&@%~$@%%!@~^^@#
外星人停止了动作，试着不发出笑声，最终禁不住大笑起来，并且停不下来。
当他笑的时候，你跑上前去，一枪命中他的眉心，将他放倒。然后跳进武器室。
你一个前空翻进入武器室，仔细地检查武器室是否藏有更多的外星人。死一般的寂静，太安静了。
你站起来，跑向武器室的角落，在盒子里找到了炸弹。盒子上有一个键盘，你需要输入密码才能将炸弹取出来。如果你输错10次，炸弹将永远被锁住无法取出。密码是4位数>字。
"""
)

the_bridge=Room("The Bridge",
"""
盒子咔哒一声打开了，密封破裂，毒气逸出。
你一把抓起炸弹，尽可能快递跑向驾驶舱，你必须把炸弹安置在合适的地点。
你闯入驾驶舱，手臂下夹着炸弹，惊奇地发现有5个外星人正在试图控制飞船。他们中的每一个都比上一个拥有更加丑陋的服装。他们没有拿出武器，因为他们看见了你手臂>下的炸弹，并且不希望引爆它。
"""
)

escape_pod=Room("Escape Pod",
"""
你拉出手臂下炸弹的导火线，外星人们举起手来，开始流汗。
你缓慢地退向门口，打开门，然后小心翼翼地把炸弹放在地上，拉出导火线。然后跳出驾驶舱，按下关闭按钮，门锁住了，外星人们无法逃出去。
现在炸弹已经安放好了，你跑向逃生通道。
你不顾一切地冲过飞船，以确保在整个飞船爆炸之前到达分离仓。看起来没有外星人在船上了，所以几乎没有遇到任何阻碍。你成功到达分离仓，然后你需要选择一个。他们
中的一些已经被摧毁了，但是你没有时间去检查。总共有5个分离仓，你将选择哪一个呢？
"""
)

the_end_winner=Room("The End",
"""
你跳进了2号分离舱 ，按下发动按钮。分离舱很容易地向下方的地球滑去。当它飞向地球时，你往回看，发现你的飞船像一颗明亮的星星一样炸开了，同时炸掉了恶灵的飞船
。你赢了！
"""
)

the_end_loser=Room("The End",
"""
你随便跳进一个分离舱，按下发动按钮。分离舱逃向未知的空间，然后因为外壳破裂而爆炸，把你的身体压成肉酱。
"""
)


escape_pod.add_paths({
        '2':the_end_winner,
        '*':the_end_loser
})

generic_death=Room("death","You died.")

the_bridge.add_paths({
        'throw the bomb':generic_death,
        'slowly place the bomb':escape_pod
})

laser_weapon_armory.add_paths({
        '0132':the_bridge,
        '*':generic_death
})

central_corridor.add_paths({
        'shoot!':generic_death,
        'dodge!':generic_death,
        'tell a joke':laser_weapon_armory
})

START=central_corridor
