default call_low_energy = False
default call_low_social = False
default call_high_social = False
default call_low_study = False
default call_low_mental = False
default call_low_finance = False
default call_low_health = False

# 在init python块中定义随机选择函数
init python:
    def choose_random_accident():
        # 所有可能的事件列表
        all_accidents = [
            "b_accident_lost_card",
            "b_accident_traffic_accident", 
            "b_accident_illness",
            "b_accident_scam",
            "b_accident_activity_injury",
            "b_accident_meet_friend",
            "b_accident_paper_selected"
        ]
        # 使用renpy.random.sample来随机选择2个不同的事件
        return renpy.random.sample(all_accidents, 2)

label b_option:
    stop music fadeout 1.0
    play music "audio/轻松欢快.mp3" fadein 1.0 volume 0.5 loop
    call accident_option from _call_accident_option

    call events_option from _call_events_option

    jump c_option

# 随机事件处理label
label accident_option:
    # 获取两个随机事件
    $ selected_accident = choose_random_accident()
    
    # 触发第一个随机事件
    $ accident1 = selected_accident[0]
    call expression accident1 from _call_expression
    
    # 触发第二个随机事件
    $ accident2 = selected_accident[1]
    call expression accident2 from _call_expression_1
    
    return

label events_option:
    # 提前判断并设置信号量
    if value_dict['E'] < 40:
        $ call_low_energy = True  # 精力值低，设置低精力事件信号量
    if value_dict['S'] < 60:
        $ call_low_social = True  # 社交关系低，设置低社交关系事件信号量
    if value_dict['S'] > 90:
        $ call_high_social = True  # 社交关系过高，设置高社交关系事件信号量
    if value_dict['A'] < 60:
        $ call_low_study = True  # 学业进度低，设置低学业进度事件信号量
    if value_dict['M'] < 60:
        $ call_low_mental = True  # 心理健康状况低，设置低心理健康事件信号量
    if value_dict['F'] < 70:
        $ call_low_finance = True  # 财务状况不好，设置财务问题事件信号量
    if value_dict['B'] < 50:
        $ call_low_health = True  # 身体不健康，设置身体健康状况低事件信号量


    # 根据信号量依次触发每个事件
    if call_low_energy:
        call b_event_low_energy from _call_b_event_low_energy
    if call_low_social:
        call b_event_low_social from _call_b_event_low_social
    if call_high_social:
        call event_high_social from _call_event_high_social
    if call_low_study:
        call b_event_low_study from _call_b_event_low_study
    if call_low_mental:
        call b_event_low_mental from _call_b_event_low_mental
    if call_low_finance:
        call b_event_low_finance from _call_b_event_low_finance
    if call_low_health:
        call b_event_low_health from _call_b_event_low_health

    return