# 丢失校园一卡通
label b_accident_lost_card:
    scene bg cafeteria
    with fade

    python:
        scen_desc = """
        时间：午餐时间
        地点：学校食堂
        人物：我，朋友
        场景描述：我和朋友去吃饭，快轮到我们是我发现我不小心丢失了一卡通，无法买饭。焦急之下，我必须决定是借朋友钱吃饭还是去补办学子卡。
        **注意生成的对话要求不能表明主角已经确定的选择，而是在选项之间再犹豫不决**
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

    menu:
        "借钱吃饭":
            python:
                plot_history.extend(["旁白：我选择了借钱吃饭"])
                li = value_ai_with_loading_screen(new_plot, "E:0~0,A:0~0,B:0~0,M:0~0,S:+5~+10,F:-5~-1", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_lost_card_borrow_money

        "不吃饭，直接补办一卡通":
            python:
                plot_history.extend(["旁白：我选择了不吃饭，直接去补办一卡通"])
                li = value_ai_with_loading_screen(new_plot, "E:-10~-5,A:0~0,B:0~0,M:-5~0,S:-5~0,F:0~0", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_lost_card_replace_card

# 交通事故
label b_accident_traffic_accident:
    scene bg street
    with fade
    python:
        scen_desc = """
        时间：下午
        地点：校外街道
        人物：我
        场景描述：骑车时不慎摔倒，受了轻伤。现在我在思考是否要不要去医务室检查。
        **注意生成的对话要求不能表明主角已经确定的选择，而是在选项之间再犹豫不决**
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
                elif key == "爸爸":
                    renpy.show("father", at_list=[player_right])
                    renpy.say(father, value)
                    renpy.hide("father")
                elif key == "妈妈":
                    renpy.show("mother", at_list=[player_right])
                    renpy.say(mother, value)
                    renpy.hide("mother")
                else:
                    continue

    menu:
        "去医院检查":
            python:
                plot_history.extend(["旁白：我选择了去医院检查"])
                li = value_ai_with_loading_screen(new_plot, "E:-10~-5,A:0~0,B:-5~-1,M:-5~0,S:0~0,F:-5~0", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_traffic_accident_hospital

        "不理会，继续前行":
            python:
                plot_history.extend(["旁白：我选择了不理会轻伤，继续前行"])
                li = value_ai_with_loading_screen(new_plot, "E:0~0,A:0~0,B:-10~-15,M:-10~-5,S:0~0,F:0~0", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_traffic_accident_ignore

# 生病
label b_accident_illness:
    scene bg dorm_room
    with fade

    python:
        scen_desc = """
        时间：晚上
        地点：宿舍
        人物：我
        场景描述：因为气候变化，我感冒发烧，身体状况糟糕，需要做出决定去不去医务室。
        **注意生成的对话要求不能表明主角已经确定的选择，而是在选项之间再犹豫不决**
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
                elif key == "爸爸":
                    renpy.show("father", at_list=[player_right])
                    renpy.say(father, value)
                    renpy.hide("father")
                elif key == "妈妈":
                    renpy.show("mother", at_list=[player_right])
                    renpy.say(mother, value)
                    renpy.hide("mother")
                else:
                    continue

    menu:
        "去医务室看病":
            python:
                plot_history.extend(["旁白：我选择了去医院看病"])
                li = value_ai_with_loading_screen(new_plot, "E:-5~-1,A:0~0,B:-5~-1,M:0~0,S:0~0,F:-5~-1", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_illness_hospital

        "自己扛着，不去医务室":
            python:
                plot_history.extend(["旁白：我选择了不去医务室"])
                li = value_ai_with_loading_screen(new_plot, "E:-10~-5,A:0~0,B:-10~-15,M:0~0,S:0~0,F:0~0", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_illness_self_heal

# 网络诈骗
label b_accident_scam:
    scene bg internet
    with fade

    python:
        scen_desc = """
        时间：晚上
        地点：宿舍
        人物：我
        场景描述：我在网络购物时遭遇诈骗，损失了一笔钱，心情十分低落。我在犹豫要不要报警。
        **注意生成的对话要求不能表明主角已经确定的选择，而是在选项之间再犹豫不决**
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
                elif key == "爸爸":
                    renpy.show("father", at_list=[player_right])
                    renpy.say(father, value)
                    renpy.hide("father")
                elif key == "妈妈":
                    renpy.show("mother", at_list=[player_right])
                    renpy.say(mother, value)
                    renpy.hide("mother")
                else:
                    continue

    menu:
        "报警处理":
            python:
                plot_history.extend(["旁白：我选择了报警处理"])
                li = value_ai_with_loading_screen(new_plot, "E:-10~-5,A:0~0,B:0~0,M:+1~+5,S:0~0,F:0~0", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_scam_report_police

        "接受损失":
            python:
                plot_history.extend(["旁白：我选择了接受损失"])
                li = value_ai_with_loading_screen(new_plot, "E:-5~-1,A:0~0,B:0~0,M:-10~-5,S:-5~-1,F:-20~-15", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_scam_accept_loss

# 运动受伤
label b_accident_activity_injury:
    scene bg sports_field
    with fade

    python:
        scen_desc = """
        时间：下午
        地点：操场
        人物：我
        场景描述：我所在的球队在和其他学院的球队打比赛时我不慎受伤，我不想抛下我的队友，但是我也怕我的伤情加重，我在犹豫是否要继续比赛。
        **注意生成的对话要求不能表明主角已经确定的选择，而是在选项之间再犹豫不决**
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
                elif key == "爸爸":
                    renpy.show("father", at_list=[player_right])
                    renpy.say(father, value)
                    renpy.hide("father")
                elif key == "妈妈":
                    renpy.show("mother", at_list=[player_right])
                    renpy.say(mother, value)
                    renpy.hide("mother")
                else:
                    continue

    menu:
        "继续比赛":
            python:
                plot_history.extend(["旁白：我选择了继续比赛"])
                li = value_ai_with_loading_screen(new_plot, "E:-10~-5,A:0~0,B:-10~-15,M:0~0,S:+5~+10,F:0~0", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_activity_injury_continue

        "退出比赛，去医务室":
            python:
                plot_history.extend(["旁白：我选择了退出比赛，去医务室"])
                li = value_ai_with_loading_screen(new_plot, "E:-5~-1,A:0~0,B:-10~-5,M:-5~0,S:0~0,F:-3~-1", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_activity_injury_quit

#遇到聊得来的朋友
label b_accident_meet_friend:
    scene bg hiking_path
    with fade

    python:
        scen_desc = """
        时间：下午
        地点：户外
        人物：我，新朋友
        场景描述：在户外素质提升实践徒步中，遇到了一个聊得来的朋友，感到十分愉快。我想以后与他进一步交流，加深友谊，但我又有点内向，在犹豫是否要保持礼貌，不继续交流了。
        **注意生成的对话要求不能表明主角已经确定的选择，而是在选项之间再犹豫不决**
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
                elif key == "爸爸":
                    renpy.show("father", at_list=[player_right])
                    renpy.say(father, value)
                    renpy.hide("father")
                elif key == "妈妈":
                    renpy.show("mother", at_list=[player_right])
                    renpy.say(mother, value)
                    renpy.hide("mother")
                else:
                    continue

    menu:
        "加深友谊":
            python:
                plot_history.extend(["旁白：我选择了加深友谊"])
                li = value_ai_with_loading_screen(new_plot, "E:0~0,A:0~0,B:0~0,M:+5~+10,S:+10~+15,F:0~0", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_meet_friend_deepen_friendship

        "保持礼貌，但不继续交流":
            python:
                plot_history.extend(["旁白：我选择了保持礼貌，不继续交流"])
                li = value_ai_with_loading_screen(new_plot, "E:0~0,A:0~0,B:0~0,M:0~0,S:-5~-1,F:0~0", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_meet_friend_polite

#论文被评为优秀作品
label b_accident_paper_selected:
    scene bg library
    with fade

    python:
        scen_desc = """
        时间：某日下午
        地点：图书馆
        人物：我，导师
        场景描述：我的一篇课程论文被选为优秀作品，获得发表机会，导师对此表示祝贺。现在我在犹豫要不要去庆祝一下，还是继续保持低调。
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
                elif key == "导师":
                    renpy.show("mentor", at_list=[player_right])
                    renpy.say(mentor, value)
                    renpy.hide("mentor")
                elif key == "爸爸":
                    renpy.show("father", at_list=[player_right])
                    renpy.say(father, value)
                    renpy.hide("father")
                elif key == "妈妈":
                    renpy.show("mother", at_list=[player_right])
                    renpy.say(mother, value)
                    renpy.hide("mother")
                else:
                    continue

    menu:
        "庆祝自己的成功":
            python:
                plot_history.extend(["旁白：我选择了庆祝自己的成功"])
                li = value_ai_with_loading_screen(new_plot, "E:-5~-1,A:+5~+10,B:0~0,M:+5~+10,S:+5~+10,F:-5~-1", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_paper_selected_celebrate

        "继续低调前行":
            python:
                plot_history.extend(["旁白：我选择了继续低调谦虚"])
                li = value_ai_with_loading_screen(new_plot, "E:0~0,A:+10~+15,B:0~0,M:+5~+10,S:0~0,F:0~0", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_paper_selected_stay_humble

