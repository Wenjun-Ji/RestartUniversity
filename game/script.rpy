# 定义角色
define p = Character("我")
define father = Character("爸爸")
define mother = Character("妈妈")
define she = Character("她")
define Senior = Character("学长")
define Senior_sister = Character("学姐")

define classmate = Character("同学")
define u = Character("社团负责人")
define roommate = Character("室友")
define rs = Character("其他室友")
define roommates = Character("室友们")
define member = Character("学生组织成员")
define actor = Character("演员们")
define technician = Character("技术人员")
define guider = Character("辅导员")
define aunt = Character("宿管阿姨")

define teacher = Character("老师")

define doctor = Character("医生")
define police = Character("警察")
define friends = Character("朋友们")
define friend = Character("朋友")
define new_friend = Character("新朋友")
define excellent_student = Character("学霸同学")
define psychiatrist = Character("心理医生")
define cafeboss = Character("咖啡馆老板")
define mentor = Character("导师")

transform player_left:
    zoom 0.5
    xalign 0.0
    yalign 1.0

transform player_center:
    zoom 0.5
    xalign 0.5
    yalign 1.0
    
transform player_right:
    zoom 0.5
    xalign 1.0
    yalign 1.0

image p = "images/character/男同学10.png"
image father = "images/character/中年男人2.png"
image mother = "images/character/中年女人5.png"
image she = "images/character/女同学4.png"
image Senior = "images/character/男同学1.png"
image Senior_sister = "images/character/女同学3.png"
image classmate = "images/character/男同学2.png"
image u = "images/character/女同学5.png"
image roommate = "images/character/男同学3.png"
image rs = "images/character/男同学8.png"
image roommates = "images/character/男同学9.png"
image member = "images/character/女同学10.png"
image actor = "images/character/男同学3.png"
image technician = "images/character/中年男人3.png"
image guider = "images/character/中年女人3.png"
image aunt = "images/character/中年女人4.png"
image teacher = "images/character/中年男人4.png"
image doctor = "images/character/医生.png"
image police = "images/character/警察.png"
image friends = "images/character/男同学13.png"
image friend = "images/character/男同学12.png"
image new_friend = "images/character/女同学6.png"
image excellent_student = "images/character/学长3.png"
image psychiatrist = "images/character/医生.png"
image cafeboss = "images/character/咖啡馆老板.png"
image mentor = "images/character/导师2.png"


init python:
    
    from chatgpt import TextAI, ValueAI, SelectAI, SummaryAI
    plot_history = []
    value_dict = {'E': 95, 'A': 100, 'B': 100, 'M': 100, 'S': 100, 'F': 100}
    text_ai = TextAI()
    value_ai = ValueAI()
    select_ai = SelectAI()
    summary_ai = SummaryAI()

image bg activity_center = "images/background/activity_center_resized.png"
image bg student_center = "images/background/activity_center_resized.png"
image bg admin_office = "images/background/admin_office_resized.png"
image bg auditorium = "images/background/auditorium_resized.png"
image bg bedroom = "images/background/bedroom_resized.png"
image bg cafe = "images/background/cafe_resized.png"
image bg cafeteria = "images/background/cafeteria_resized.png"
image bg chechuang = "images/background/chechuang_resized.png"
image bg classroom = "images/background/classroom_resized.png"
image bg company = "images/background/company_resized.png"
image bg competition_scene = "images/background/competition_scene_resized.png"
image bg counseling_room = "images/background/counseling_room_resized.png"
image bg counselor_office = "images/background/counselor_office_resized.png"
image bg dormitory_day = "images/background/dormitory_day_resized.png"
image bg dormitory_night = "images/background/dormitory_night_resized.png"
image bg dormitory = "images/background/dormitory_resized.png"
image bg dorm = "images/background/dormitory_resized.png"
image bg dorm_room = "images/background/dormitory_resized.png"
image bg examhall = "images/background/examhall_resized.png"
image bg farewell = "images/background/farewell_resized.png"
image bg friends_home = "images/background/friends_home_resized.png"
image bg gym = "images/background/gym_resized.png"
image bg hiking_path = "images/background/hiking_path_resized.png"
image bg park = "images/background/hiking_path_resized.png"
image bg home_living_room = "images/background/home_living_room_resized.png"
image bg hospital = "images/background/hospital_resized.png"
image bg medical_office = "images/background/hospital_resized.png"
image bg internet = "images/background/internet_resized.png"
image bg lab_room = "images/background/lab_room_resized.png"
image bg library = "images/background/library_resized.png"
image bg main_menu = "images/background/main_menu_resized.png"
image bg nowhere = "images/background/nowhere_resized.png"
image bg playground = "images/background/playground_resized.png"
image bg sports_field = "images/background/playground_resized.png"
image bg police_station = "images/background/police_station_resized.png"
image bg rainy_playground = "images/background/rainy_playground_resized.png"
image bg restaurant = "images/background/restaurant_resized.png"
image bg riverside = "images/background/riverside_resized.png"
image bg school = "images/background/school_resized.png"
image bg street = "images/background/street_resized.png"
image bg study = "images/background/study_resized.png"
image bg university_gate = "images/background/university_gate_resized.png"
image bg university = "images/background/university_resized.png"


# 游戏开始
label start:
    # 开场 - 黑色背景，白色文字，神秘的背景音乐
    scene black with fade
    play music "audio/intro/intro.WAV"  # 播放神秘的背景音乐

    # 开启自动播放，隐藏对话框
    window hide

    # 旁白开场白
    narrator "时间是什么？" 
    narrator "是我们无法掌控的流逝……" 
    narrator "还是一种悄然消逝的选择？" 
    
    narrator "时间，像流水一样，一不小心就从指缝里溜走了。还没反应过来，它就已经远去了。" 
    narrator "四年的大学生活，说长不长，说短不短，总有些你来不及抓住的瞬间。" 
    narrator "你是否曾想过，如果有机会重来一次，你会怎么走这段路？" 

    # 大学生活的缩影开始
    
    # 场景 1：高考出分
    scene bg intro gaokao  # 显示高考出分的图片
    with dissolve
    narrator "每个人都有那么一个时刻，手心冒汗，屏住呼吸，等着高考分数跳出来。"
    narrator "分数出来了……成败在此一刻定了。说实话，心里还是有点慌，不管好坏，总觉得命运这下锁定了。"
    narrator "我爸妈很激动，但我心里其实挺迷茫的，未来的路，还看不太清。"

    # 场景 2：录取结果出来
    scene bg intro luqu  # 录取成功的图片
    with fade
    narrator "当‘录取成功’弹出来的时候，心里有种说不出的复杂。既兴奋，又有点恍惚，毕竟你知道，这只是个开始。"
    narrator "终于被录取了！其实当时看到的那一刻，有点儿发懵。这是我该高兴的时候，但怎么说呢，内心却感觉空空的。"

    # 场景 3：开学报道
    scene bg intro baodao # 开学报道的图片
    with zoomin
    narrator "第一次站在大学校门口，行李箱在手，前方是你要生活四年的地方。"
    narrator "这是我的大学……校园比我想象中要大，真有点找不着北。大家都挺激动，但我心里既期待又有点紧张。"

    # 场景 4：宿舍生活
    scene bg intro sushe  # 宿舍生活的图片
    with pixellate
    narrator "宿舍，是你接下来四年的‘家’，这里将装下你的欢笑与烦恼。"
    narrator "这就是我的宿舍啊，还挺乱的。大家都忙着收拾东西，我不知道该说什么，但希望能处好。毕竟我们要一起生活四年呢。"

    # 场景 5：社团活动
    scene bg intro jucan  # 社团招新场景图片
    narrator "每个新生都会在社团招新的时候站在摊位前发呆，挑花了眼。其实无所谓，选一个自己喜欢的，体验就从这里开始了。"
    narrator "社团那么多，我到底该选哪个？有点迷茫，怕选错，但不管了，试试吧，反正大学生活需要点不一样的体验。"

    # 场景 6：恋爱交友
    scene bg intro jiaoyou  # 朋友谈笑场景图片
    narrator "大学里，朋友是最让人割舍不下的部分。每一次谈笑，都值得被珍藏。"
    narrator "认识了几位好朋友，没想到这么快就能融入进来。希望接下来的四年我们能一直这样。"

    # 场景 7：学习
    scene bg intro xuexi  # 图书馆学习场景图片
    narrator "大学学习不再是单纯的考试，而是逐渐探索自己的兴趣和能力。既困惑，又充实。"
    narrator "学习和高中不一样，更多的是自己去探索。虽然累，但也有一种特别的充实感。"

    # 场景 8：考试失利
    scene bg intro kaoshi  # 考试成绩不理想图片
    narrator "考试总有失利的时候，但这不代表什么。重要的是，跌倒了，得再爬起来。"
    narrator "这次考得真不怎么样……说实话，我挺努力的，但成绩不理想。是不是我方法不对？有点挫败，但得重新振作。"

    # 场景 9：熟悉大学生活
    scene familiar_campus  # 熟悉校园全景
    narrator "曾经陌生的校园，转眼间已经变得熟悉。大学生活，就是这样不经意间悄悄溜走。"
    narrator "时间过得真快啊，转眼间我已经适应了这里的生活。"

    # 场景 10：比赛/科研成就
    scene bg intro keyan  # 科研比赛获奖图片
    narrator "比赛、科研，这些时刻不仅仅是荣誉，更是对自己的肯定。每一次成就背后，都有无数的汗水。"
    narrator "这次我们终于拿到了奖杯！努力总算没有白费。站在台上，我才感觉到自己的付出得到了认可。"

    # 场景 11：工作实习
    scene bg intro shixi  # 实习场景图片
    narrator "实习让你提前接触了社会，忙碌和压力让人怀念学校的时光。未来，渐渐变得清晰。"
    narrator "实习的节奏很快，和学校生活完全不一样。工作压力大，但也让我提前体验到了社会的真实面貌。"

    # 场景 12：毕业旅行
    scene graduation_trip  # 毕业旅行场景图片
    narrator "旅行，往往是告别的序曲。青春的最后一刻，总是在不经意间到来。"
    narrator "这可能是我们最后一次一起旅行了。大家笑得很开心，但心里却有种淡淡的伤感。"

    # 场景 13：毕业典礼
    scene bg intro biye  # 毕业典礼场景图片
    narrator "毕业典礼，意味着结束，也意味着新的开始。未来的路，等待着你们去走。"
    narrator "毕业了……这就是我们一直期待的时刻，但到了这一刻，我心里却有些失落。"

    # 场景 14：空荡荡的宿舍
    scene bg intro fenbie  # 空荡宿舍图片
    narrator "每个人都有离别的那一刻，大学生活走到了尽头。曾经的喧闹与笑声，现在都成了回忆。"
    narrator "大家都走了……宿舍突然变得安静。平时吵吵闹闹的，现在只剩我一个人。"

    # 进入时间倒流阶段
    narrator "时间像是在倒流，你的大学生活一幕幕重新浮现。那些曾经错过的机会，是否真的不能重来？"

    # 使用内置 move 过渡效果，模拟走马灯效果，倒序展示之前的所有场景
    scene bg intro fenbie at left with move  # 场景 14：空荡宿舍
    scene bg intro biye at left with move  # 场景 13：毕业典礼
    scene graduation_trip at left with move  # 场景 12：毕业旅行
    scene bg intro shixi at left with move  # 场景 11：工作实习
    scene bg intro keyan at left with move  # 场景 10：比赛/科研成就
    scene familiar_campus at left with move  # 场景 9：熟悉校园
    scene bg intro kaoshi at left with move  # 场景 8：考试失利
    scene bg intro xuexi at left with move  # 场景 7：学习
    scene bg intro jiaoyou at left with move  # 场景 6：恋爱交友
    scene bg intro jucan at left with move  # 场景 5：社团活动
    scene bg intro sushe at left with move  # 场景 4：宿舍生活
    scene bg intro baodao at left with move  # 场景 3：开学报道
    scene bg intro luqu at left with move  # 场景 2：录取结果出来
    scene bg intro gaokao at left with move  # 场景 1：高考出分
    
    # 使用 renpy.random.choice 随机选择场景
    $ scene_choice = renpy.random.choice(["good", "bad"])
    # 显示重开按钮
    menu:
        "重开":
            if scene_choice == "good":
                jump a_gaokao_good
            else:
                jump a_gaokao_bad
        "不重开":
            jump end  # 结束游戏

label end:
    "游戏结束"


