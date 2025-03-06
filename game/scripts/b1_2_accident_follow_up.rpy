# 丢失校园一卡通
#   借钱吃饭
label event_lost_card_borrow_money:
    scene bg cafeteria
    with fade
    python:
        scen_desc = """
        时间：午餐时间
        地点：学校食堂
        人物：我，同学
        场景描述：我选择了借朋友的钱吃饭。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                elif key == "朋友":
                    renpy.show("friend", at_list=[player_right])
                    renpy.say(friend, value)
                    renpy.hide("friend")
                else:
                    continue
    
    return

#   补办
label event_lost_card_replace_card:
    scene bg admin_office
    with fade
    python:
        scen_desc = """
        时间：午餐时间
        地点：学校食堂
        人物：我
        我直接去了学校的行政办公室补办了一张一卡通，虽然解决了问题，但因为饿了一整天，精力明显不足。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                elif key == "朋友":
                    renpy.show("friend", at_list=[player_right])
                    renpy.say(friend, value)
                    renpy.hide("friend")
                else:
                    continue

    return

# 交通事故
#   医院检查
label event_traffic_accident_hospital:
    scene bg hospital
    with fade
    python:
        scen_desc = """
        时间：下午
        地点：医务室
        人物：我,医生
        场景描述：在医务室经过医生的简单检查，发现并无大碍，但还是建议休息几天。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                elif key == "医生":
                    renpy.show("doctor", at_list=[player_right])
                    renpy.say(doctor,value)
                    renpy.hide("doctor")
                else:
                    continue

    return

#   不理会
label event_traffic_accident_ignore:
    scene bg street
    with fade

    python:
        scen_desc = """
        时间：下午
        地点：校外街道
        人物：我
        场景描述：我决定不去医院，继续骑车前行，但是感觉不适感加重。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                else:
                    continue

    return

# 生病
#   去医院
label event_illness_hospital:
    scene bg hospital
    with fade

    python:
        scen_desc = """
        时间：晚上
        地点：医务室
        人物：我，医生
        场景描述：在医务室，医生确认我只是轻微感冒，开了药让我好好休息几天，心情有所缓解。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                elif key == "医生":
                    renpy.show("doctor", at_list=[player_right])
                    renpy.say(doctor,value)
                    renpy.hide("doctor")
                else:
                    continue

    return

#   扛着
label event_illness_self_heal:
    scene bg dorm_room
    with fade

    python:
        scen_desc = """
        时间：晚上
        地点：宿舍
        人物：我
        场景描述：我决定自己扛着不去医务室，但几天后症状加重，精力和情绪都明显下降。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                else:
                    continue

    return


# 网络诈骗
#   报警
label event_scam_report_police:
    scene bg police_station
    with fade

    python:
        scen_desc = """
        时间：第二天白天
        地点：警局
        人物：我，警察
        场景描述：我选择了报警，警察表示他们会尽力追踪骗子。最终成功追回我的财产。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                elif key =="警察":
                    renpy.show("police", at_list=[player_right])
                    renpy.say(police,value) 
                    renpy.hide("police")
                else:
                    continue

    return

#   接受损失
label event_scam_accept_loss:
    scene bg dorm_room
    with fade

    python:
        scen_desc = """
        时间：晚上
        地点：宿舍
        人物：我
        场景描述：我选择接受损失，虽然经济上受到了打击，但渐渐从情绪低落中走出来，开始面对现实。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                else:
                    continue

    return

# 运动手术
#   继续比赛
label event_activity_injury_continue:
    scene bg sports_field
    with fade

    python:
        scen_desc = """
        时间：下午
        地点：操场
        人物：我
        场景描述：尽管受了伤，我还是决定继续比赛，队友们既感动又担心我的情况，但随着比赛的进行，伤势加重，我最终不得不退出。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                else:
                    continue

    return

#   退出比赛
label event_activity_injury_quit:
    scene bg medical_office
    with fade

    python:
        scen_desc = """
        时间：下午
        地点：医务室
        人物：我,医生
        场景描述：我选择退出比赛并去了医务室，医生建议我好好休息几天。我因为没能帮助球队而感到沮丧，但为了避免了更严重的伤势我只能选择退出。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                elif key == "医生":
                    renpy.show("doctor", at_list=[player_right])
                    renpy.say(doctor,value)
                    renpy.hide("doctor")
                else:
                    continue
    return

# 遇到聊得来的朋友
#   加深友谊
label event_meet_friend_deepen_friendship:
    scene bg park
    with fade

    python:
        scen_desc = """
        时间：下午
        地点：户外
        人物：我，新朋友
        场景描述：我选择与这位朋友加深友谊，我们约定了下次一起去参加校园活动，关系变得更近了。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                elif key == "新朋友":
                    renpy.show("new_friend", at_list=[player_right])
                    renpy.say(new_friend, value)
                    renpy.hide("new_friend")
                else:
                    continue
    return

#   不继续交流
label event_meet_friend_polite:
    scene bg park
    with fade

    python:
        scen_desc = """
        时间：下午
        地点：户外
        人物：我，新朋友
        场景描述：虽然我们聊得很愉快，但我决定不加深交往，只是礼貌地道别，然后各自离开。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                elif key == "新朋友":
                    renpy.show("new_friend", at_list=[player_right])
                    renpy.say(new_friend, value)
                    renpy.hide("new_friend")
                else:
                    continue
    return

# 论文被评为优秀作品
#   庆祝
label event_paper_selected_celebrate:
    scene bg restaurant
    with fade

    python:
        scen_desc = """
        时间：晚上
        地点：餐厅
        人物：我,朋友们
        场景描述：我决定好好庆祝自己的成功，和朋友们一起去餐厅吃了一顿丰盛的晚餐，感觉很满足。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                elif key == "朋友们":
                    renpy.show("friends", at_list=[player_right])
                    renpy.say(friends, value)
                    renpy.hide("friends")
                else:
                    continue
    return

#   低调
label event_paper_selected_stay_humble:
    scene bg library
    with fade

    python:
        scen_desc = """
        时间：某日下午
        地点：图书馆
        人物：我
        场景描述：我决定继续保持低调，并没有大肆庆祝，而是静静地享受成功的喜悦，并开始计划下一步的学术工作。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                else:
                    continue
    return
