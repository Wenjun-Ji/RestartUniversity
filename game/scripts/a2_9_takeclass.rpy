label a_takeclass:
    scene bg activity_center
    with fade
    
    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：学生活动中心
        人物：我，同学 
        场景描述：阳光透过窗户洒在教室，同学们背着书包，带着笔记本和咖啡，三三两两走进教室。他们找到座位，打开书本，准备迎接即将开始的课程。空气中弥漫着期待和好奇，老师准备课件，一切井然有序。
        """
        
        # 调用AI生成新的大学场景剧情
        new_plot = text_ai_with_loading_screen(scen_desc_1, plot_history, value_dict)

        # 更新剧情历史
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        
        # 显示生成的剧情
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                elif key == "同学":
                    renpy.show("classmate", at_list=[player_right])
                    renpy.say(classmate, value)
                    renpy.hide("classmate")
                else:
                    continue

    $ res = select_ai_with_loading_screen("我即将开始上课", value_dict, plot_history, ["important_class", "group_discussion"])
    if res == "important_class":
        $ plot_history.extend([f"这节课非常重要但无趣"])
        jump a_important_class
    if res == "group_discussion":
        $ plot_history.extend([f"这是一堂小组讨论课"])
        jump a_group_discussion

label a_important_class:
    scene bg classroom
    with fade
    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：教室
        人物：我，同学，老师
        场景描述：这节专业必修课的内容是期末考试的重点，老师正对着PPT一板一眼地讲解着公式推导。教室里很安静，只有投影仪的嗡嗡声和粉笔偶尔敲击黑板的声音。前排几个同学正认真记着笔记，我却感到昏昏欲睡。手机在口袋里震动了一下，可能是收到了新消息。
        """
        
        # 调用AI生成新的场景剧情
        new_plot = text_ai_with_loading_screen(scen_desc_1, plot_history, value_dict)

        # 更新剧情历史
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        
        # 显示生成的剧情
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                elif key == "同学":
                    renpy.show("classmate", at_list=[player_right])
                    renpy.say(classmate, value)
                    renpy.hide("classmate")
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
                else:
                    continue

    # 玩家互动选项
    menu:
        "我选择全神贯注上课":
            $ plot_history.extend(["旁白：我选择全神贯注上课"])
            jump a_class_focus
        
        "我选择一边听课一边玩手机":
            $ plot_history.extend(["旁白：我选择一边听课一边玩手机"])
            jump a_class_distracted

label a_class_focus:
    scene bg classroom
    with fade

    python:
        scen_desc_1 = """
        时间：大学开学后
        地点：教室
        人物：我，同学，老师
        我强迫自己集中注意力，拿起笔开始记录老师讲解的要点。虽然内容枯燥，但确实很重要。慢慢地，我开始理解了一些之前不明白的概念。老师的语气虽然平淡，但讲解的逻辑还是很清晰的。
        """

        new_plot = text_ai_with_loading_screen(scen_desc_1, plot_history, value_dict)

        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                elif key == "同学":
                    renpy.show("classmate", at_list=[player_right])
                    renpy.say(classmate, value)
                    renpy.hide("classmate")
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:-5~-10,A:+10~+15,B:-5~-3,M:-5~-3,S:0~0,F:0~0", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_dormagain

label a_class_distracted:
    python:
        scen_desc_3 = """
        时间：大学开学后
        地点：教室
        人物：我，同学
        我悄悄掏出手机，试图在听课的同时刷一下消息。朋友圈里有新动态，群里的消息也在不断闪动。我时不时抬头看一眼PPT，试图跟上教授的节奏，但注意力总是不自觉地被手机吸引。
        """
        new_plot = text_ai_with_loading_screen(scen_desc_3, plot_history, value_dict)
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                elif key == "同学":
                    renpy.show("classmate", at_list=[player_right])
                    renpy.say(classmate, value)
                    renpy.hide("classmate")
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:-5~-3,A:-1~-5,B:+0~+0,M:-0~-5,S:+0~+2,F:0~0", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_dormagain

label a_group_discussion:
    scene bg classroom
    with fade
    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：教室
        人物：我，同学，老师
        场景描述：课堂上进行小组讨论，我们六个人围坐在一起。老师布置的话题很有趣，讨论逐渐热烈起来。有同学提出了自己的观点，其他人时而点头赞同，时而提出不同意见。桌上摊开的笔记本记录着大家的发言要点，有几位同学正在翻阅参考资料。
        """
        
        # 调用AI生成新的场景剧情
        new_plot = text_ai_with_loading_screen(scen_desc_1, plot_history, value_dict)

        # 更新剧情历史
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        
        # 显示生成的剧情
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                elif key == "同学":
                    renpy.show("classmate", at_list=[player_right])
                    renpy.say(classmate, value)
                    renpy.hide("classmate")
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
                else:
                    continue

    # 玩家互动选项
    menu:
        "我选择积极发言":
            $ plot_history.extend(["我选择积极发言"])
            jump a_discussion_active
        
        "我选择默默倾听":
            $ plot_history.extend(["我选择默默倾听"])
            jump a_discussion_passive

label a_discussion_active:
    scene bg classroom
    with fade
    python:
        scen_desc_1 = """
        时间：大学开学后
        地点：教室
        人物：我，同学
        我积极参与讨论，提出自己的观点，与同学们进行交流。虽然有些紧张，但讨论的氛围很好，大家都很友好。我感到自己的思维得到了锻炼，也学到了一些新的知识。
        """

        new_plot = text_ai_with_loading_screen(scen_desc_1, plot_history, value_dict)

        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                elif key == "同学":
                    renpy.show("classmate", at_list=[player_right])
                    renpy.say(classmate, value)
                    renpy.hide("classmate")
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:-1~-5,A:+5~+10,B:0~0,M:+2~+7,S:+5~+8,F:0~0", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_dormagain

label a_discussion_passive:
    scene bg classroom
    with fade
    python:
        scen_desc_1 = """
        时间：大学开学后
        地点：教室
        人物：我，同学
        我选择默默倾听，聆听同学们的讨论。他们提出的观点和问题让我思考，也学到了一些新的知识。虽然没有发言，但我感到很满足。
        """

        new_plot = text_ai_with_loading_screen(scen_desc_1, plot_history, value_dict)

        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)
                    renpy.hide("p")
                elif key == "同学":
                    renpy.show("classmate", at_list=[player_right])
                    renpy.say(classmate, value)
                    renpy.hide("classmate")
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:-3~-1,A:+5~+8,B:0~0,M:-3~-1,S:-5~-3,F:0~0", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_dormagain
