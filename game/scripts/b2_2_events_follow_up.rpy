# 精力值低事件后休息
label event_low_energy_rest:
    scene bg dormitory
    with fade
    python:
        scen_desc = """
        时间：休息几天后
        地点：宿舍
        人物：我
        场景描述：我经过几天的休息，身体状况明显好转。虽然错过了一些课程和活动，但精力充沛的感觉让你意识到休息的重要性。我开始计划如何安排之后的学习和生活。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)

        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        # 显示剧情
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

# 精力值低事件后继续学习
label event_low_energy_study:
    scene bg classroom
    with fade
    python:
        scen_desc = """
        时间：一周后
        地点：教室
        人物：我
        场景描述：我强撑着继续保持原有作息的结果并不理想。身体状况持续恶化，上课时经常头晕目眩，作业质量也大不如前。最终在一次课堂上晕倒，不得不被送往医院进行更长时间的休养。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        # 显示剧情
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

# 社交关系值低事件后联系朋友
label event_low_social_contact:
    scene bg cafe
    with fade
    python:
        scen_desc = """
        时间：周末下午
        地点：校园咖啡厅
        人物：我，朋友们
        场景描述：我约上几个好朋友在咖啡厅聚会。虽然一开始有些尴尬，但随着聊天的深入，大家渐渐找回了从前的默契。朋友们表示理解我之前忙于学业的状态，也分享了各自的近况。这次聚会让我感受到友情的温暖，决定以后要更好地平衡学习和社交。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)

        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        # 显示剧情
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

# 社交关系值低事件后忽略孤独感
label event_low_social_ignore:
    scene bg dormitory
    with fade
    python:
        scen_desc = """
        时间：一个月后
        地点：宿舍
        人物：我
        场景描述：我继续沉浸在个人世界中，社交圈越来越小。某天收到同学们组织活动的群聊消息，发现自己已经不在邀请的名单中。这一刻，强烈的孤独感和被排除在外的失落感涌上心头。
        """
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)

        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        # 显示剧情
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

# 学习进度低事件后寻求帮助
label event_low_study_help:
    scene bg library
    with fade
    
    python:
        scen_desc = """
        时间：某天下午
        地点：图书馆
        人物：我，学霸同学
        场景描述：我决定向一位成绩优异的同学寻求帮助。他非常热心，愿意给我解释你不懂的知识点，还帮你制定了一个详细的学习计划。我心中的焦虑感有所缓解，感觉有了新的动力。
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
                elif key == "学霸同学":
                    renpy.show("excellent_student", at_list=[player_right])
                    renpy.say(excellent_student, value)
                    renpy.hide("excellent_student")
    return

# 学习进度低事件后独自面对
label event_low_study_self:
    scene bg dormitory_night
    with fade
    
    python:
        scen_desc = """
        时间：深夜
        地点：宿舍
        人物：我
        场景描述：我决定独自面对学习的困境。我熬夜自学，翻阅了大量书籍和资料，但依旧收效甚微。虽然感到疲惫不堪，但我不愿轻易放弃，告诉自己一定能挺过这段艰难时光。
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

# 学习进度低事件后选择躺平
label event_low_study_give_up:
    scene bg dormitory_day
    with fade
    
    python:
        scen_desc = """
        时间：周末
        地点：宿舍
        人物：我
        场景描述：我决定放弃挣扎，不再为学习而焦虑。我开始整日躺在床上，刷剧、打游戏，抛开了学习的压力。这导致期末考试挂科，影响到了我之后的课程安排
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

#心理健康低事件后寻求咨询
label event_low_mental_counsel:
    scene bg counseling_room
    with fade
    
    python:
        scen_desc = """
        时间：几天后
        地点：心理咨询室
        人物：我，心理医生
        场景描述：我来到心理咨询室，与心理医生深入交流。我分享了自己最近的感受和经历，医生给了我一些新的视角和应对策略，让我感到内心的压力有所缓解。
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
                elif key == "心理医生":
                    renpy.show("psychiatrist", at_list=[player_right])
                    renpy.say(psychiatrist, value)
                    renpy.hide("psychiatrist")
                else:
                    continue
    return

#心理健康低事件后忽视情绪
label event_low_mental_ignore:
    scene bg dormitory_day
    with fade
    
    python:
        scen_desc = """
        时间：几天后
        地点：宿舍
        人物：我
        场景描述：我选择忽视内心的情绪，继续忙碌于学习和社交。尽管心中有不安，但我告诉自己要努力，暂时不去想这些问题。然而，内心的焦虑和压力仍在悄悄积累。
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

#心理健康低事件后找朋友倾诉
label event_low_mental_friends:
    scene bg cafe
    with fade
    
    python:
        scen_desc = """
        时间：周末
        地点：咖啡馆
        人物：我，朋友
        场景描述：我决定找朋友倾诉自己的烦恼。在咖啡馆中，我向朋友倾诉了自己的压力和焦虑。他们认真倾听，并给我了一些建议和支持，让你感到温暖和宽慰。
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

#财务状况低时间后找兼职
label event_low_finance_work:
    scene bg cafe
    with fade
    
    python:
        scen_desc = """
        时间：几天后
        地点：咖啡馆
        人物：我，咖啡馆老板
        场景描述：我决定找一份兼职来缓解经济压力。在咖啡馆面试时，老板对我表现出色，愿意雇用我。兼职工作虽然辛苦，学习进度稍微有些落下，但能让我挣到一些额外收入，也让我感到更加充实。
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
                elif key == "咖啡馆老板":
                    renpy.show("cafeboss", at_list=[player_right])
                    renpy.say(cafeboss, value)
                    renpy.hide("cafeboss")
                else:
                    continue
    return

#财务状况低时间后借钱
label event_low_finance_borrow:
    scene bg friends_home
    with fade
    python:
        scen_desc = """
        时间：几天后
        地点：朋友家
        人物：我，朋友
        场景描述：我决定向朋友借钱以度过眼前的困难。朋友很理解我的处境，愿意借给你一些钱，帮助你渡过难关。虽然有些不好意思，但我知道这是暂时的解决方案。
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

#财务状况低时间后申请贷款
label event_low_finance_loan:
    scene bg counselor_office
    with fade
    python:
        scen_desc = """
        时间：几天后
        地点：辅导员办公室
        人物：我，辅导员
        场景描述：我决定向辅导员咨询学生贷款的事宜。辅导员认真倾听我的困惑，并为你详细介绍了申请学生贷款的流程和注意事项。虽然这能帮助我渡过难关，但我对未来的还款依然感到些许不安。
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
                elif key == "辅导员":
                    renpy.show("guider", at_list=[player_right])
                    renpy.say(guider, value)
                    renpy.hide("guider")
                else:
                    continue
    return

#社交关系值过高事件后减少社交
label event_high_social_reduce:
    scene bg dormitory_night
    with fade
    python:
        scen_desc = """
        时间：几天后
        地点：宿舍
        人物：我
        场景描述：我意识到社交活动过于频繁，决定减少社交时间，专注于个人的兴趣和学习。虽然开始时感到有些孤独，但我慢慢享受起独处的时光，反思自己的内心需求。
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

#社交关系值过高事件后维持高社交
label event_high_social_continue:
    scene bg cafe
    with fade
    python:
        scen_desc = """
        时间：几天后
        地点：咖啡馆
        人物：我，朋友
        场景描述：我决定继续维持高频率的社交活动，和朋友们一起聚会、聊天。虽然有时感到疲惫，但和朋友们的互动让你感到充实和快乐，我开始享受这种热闹的生活方式。
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

# 身体健康状况低事件后调整
label event_low_health_adjust:
    scene bg dormitory
    with fade
    python:
        scen_desc = """
        时间：两周后
        地点：宿舍
        人物：我
        场景描述：经过两周的调整，我严格执行了医生的建议，规律作息，均衡饮食，适量运动。虽然花费了一些时间和金钱，但身体状况明显改善，精神也更加充沛。这段经历让我深刻认识到健康的重要性，决定将这些好习惯坚持下去。
        """
        
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        
        # 显示剧情
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

# 身体健康状况低事件后忽视
label event_low_health_ignore:
    scene bg dormitory
    with fade
    python:
        scen_desc = """
        时间：一周后
        地点：宿舍
        人物：我
        场景描述：我没有认真对待身体的警讯，仅仅吃了几天药就放弃了调整。结果身体状况不但没有好转，反而出现了更多的不适症状。这让我开始后悔没有及时重视健康问题，意识到必须改变态度了。
        """
        
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        
        # 显示剧情
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