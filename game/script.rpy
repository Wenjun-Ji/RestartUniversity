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
    zoom 0.7
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

image p = "images/character/男主.png"
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
    import pygame
    import store
    from chatgpt import TextAI, ValueAI, SelectAI, SummaryAI, EndAI
    plot_history = []
    value_dict = {'E': 100, 'A': 100, 'B': 100, 'M': 100, 'S': 100, 'F': 100}
    text_ai = TextAI()
    value_ai = ValueAI()
    select_ai = SelectAI()
    summary_ai = SummaryAI()
    end_ai = EndAI()



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

init python:
    def text_ai_with_loading_screen(scene_desc, plot_history, value_dict, min_display_time=1.0):
        """
        显示加载页面，并阻塞主线程直到 text_ai_with_loading_screen 返回结果。
        """
        # 禁用用户交互
        store.quick_menu = False

        # 显示加载页面
        renpy.show_screen("text_loading_screen")
        renpy.pause(5)

        # 记录加载页面显示的开始时间
        import time
        start_time = time.time()

        try:
            # 调用API生成新剧情
            new_plot = text_ai.invoke(scene_desc, plot_history, value_dict)

            # 确保加载页面至少显示 min_display_time 秒
            elapsed_time = time.time() - start_time
            if elapsed_time < min_display_time:
                renpy.pause(min_display_time - elapsed_time)
        finally:
            # 隐藏加载页面
            renpy.hide_screen("text_loading_screen")

            # 启用用户交互
            store.quick_menu = True

        return new_plot



init python:
    def value_ai_with_loading_screen(new_plot, attribute_changes, value_dict, min_display_time=1.0):
        """
        显示加载页面，并阻塞主线程直到 value_ai_with_loading_screen 返回结果。
        """
        # 禁用用户交互
        store.quick_menu = False

        # 显示加载页面
        renpy.show_screen("value_loading_screen")
        renpy.pause(5)

        # 记录加载页面显示的开始时间
        import time
        start_time = time.time()

        try:
            # 调用API更新属性
            li = value_ai.invoke(new_plot, attribute_changes, value_dict)

            # 确保加载页面至少显示 min_display_time 秒
            elapsed_time = time.time() - start_time
            if elapsed_time < min_display_time:
                renpy.pause(min_display_time - elapsed_time)
        finally:
            # 隐藏加载页面
            renpy.hide_screen("value_loading_screen")

            # 启用用户交互
            store.quick_menu = True

        return li



init python:
    def select_ai_with_loading_screen(prompt, value_dict, plot_history, options, min_display_time=1.0):
        """
        显示加载页面，并阻塞主线程直到 select_ai_with_loading_screen 返回结果。
        """
        # 禁用用户交互
        store.quick_menu = False

        # 显示加载页面
        renpy.show_screen("select_loading_screen")
        renpy.pause(5)

        # 记录加载页面显示的开始时间
        import time
        start_time = time.time()

        try:
            # 调用 select_ai API
            result = select_ai.invoke(prompt, value_dict, plot_history, options)

            # 确保加载页面至少显示 min_display_time 秒
            elapsed_time = time.time() - start_time
            if elapsed_time < min_display_time:
                renpy.pause(min_display_time - elapsed_time)
        finally:
            # 隐藏加载页面
            renpy.hide_screen("select_loading_screen")

            # 启用用户交互
            store.quick_menu = True

        return result


init python:
    def summary_ai_with_loading_screen(scene_desc, plot_history, value_dict, min_display_time=1.0):
        """
        显示加载页面，并阻塞主线程直到 summary_ai_with_loading_screen 返回结果。
        """
        # 禁用用户交互
        store.quick_menu = False

        # 显示加载页面
        renpy.show_screen("summary_loading_screen")
        renpy.pause(0.1)

        # 记录加载页面显示的开始时间
        import time
        start_time = time.time()

        try:
            # 调用 summary_ai API
            new_plot = summary_ai.invoke(scene_desc, plot_history, value_dict)

            # 确保加载页面至少显示 min_display_time 秒
            elapsed_time = time.time() - start_time
            if elapsed_time < min_display_time:
                renpy.pause(min_display_time - elapsed_time)
        finally:
            # 隐藏加载页面
            renpy.hide_screen("summary_loading_screen")

            # 启用用户交互
            store.quick_menu = True

        return new_plot



label disable_user_interaction():
    python:

        ## pygame这个是为了在转场的时候，用户不能和按钮交互

        ## 禁止使用鼠标相关
        pygame.event.set_blocked(pygame.MOUSEWHEEL)
        pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
        pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)

        ## 禁止使用键盘
        pygame.event.set_blocked(pygame.KEYDOWN)
        pygame.event.set_blocked(pygame.KEYUP)

        ## 禁止关闭，因为禁止了鼠标如果用户点了关闭之后会弹框问是否关闭
        ## 但是因为禁止了鼠标，没有办法点，就卡住了。
        pygame.event.set_blocked(pygame.QUIT)

    return

label enable_user_interaction():
    ## 结束禁止交互
    #$ pygame.event.set_blocked(None)
    python:
        pygame.event.set_allowed(pygame.MOUSEWHEEL)
        pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
        pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)

        pygame.event.set_allowed(pygame.KEYDOWN)
        pygame.event.set_allowed(pygame.KEYUP)

        pygame.event.set_allowed(pygame.QUIT)

    return


# 游戏开始
label start:
    # 禁用用户交互
    call disable_user_interaction from _call_disable_user_interaction
    $ quick_menu = False

    # 开场 - 黑色背景，白色文字，神秘的背景音乐
    play music "audio/引子.mp3"  # 播放神秘的背景音乐

    scene black
    with Pause(1)

    show text "时间是什么？" with dissolve
    with Pause(3)

    show text "是我们无法掌控的流逝……" with dissolve
    with Pause(3)

    show text "还是一种悄然消逝的选择……" with dissolve
    with Pause(3)

    show text "时间，像流水一样，一不小心就从指缝里溜走了。还没反应过来，它就已经远去了……" with dissolve
    with Pause(3)

    show text "四年的大学生活，说长不长，说短不短，总有些你来不及抓住的瞬间。" with dissolve
    with Pause(3)

    show text "你是否曾想过，如果有机会重来一次，你会怎么走这段路？" with dissolve
    with Pause(3)

    hide text with dissolve

    show screen start_loading_screen
    with Pause(4)
    hide screen start_loading_screen

    # 使用 renpy.random.choice 随机选择场景
    $ scene_choice = renpy.random.choice(["good", "bad"])
    if scene_choice == "good":
        jump a_gaokao_good
    else:
        jump a_gaokao_bad


label end:
    scene bg university_gate
    python:
        end = end_ai.invoke(plot_history)
        for item in end:
            renpy.say(None,item)