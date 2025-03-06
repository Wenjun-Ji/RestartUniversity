# 大学场景
label a_freshtest:
    stop music fadeout 1.0
    play music "audio/freshtest.mp3" fadein 1.0 volume 0.5 loop
    scene bg examhall
    with fade

    python:
        scen_desc_1 = """
        时间：大学开学一个月后
        地点：大学教室
        人物：我，室友，老师
        场景描述：今天是开学考，我感到既紧张又兴奋。室友和老师都鼓励我，提醒我保持冷静，仔细审题。我深吸一口气，准备迎接这次挑战。
        要求：请根据剧情描述，选择考试顺利或考试不理想，然后根据选择跳转到不同的情节。
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
                elif key == "室友":
                    renpy.show("roommate", at_list=[player_right])
                    renpy.say(roommate, value)
                    renpy.hide("roommate")
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
                else:
                    continue

    # 玩家互动选项
    $ res = select_ai_with_loading_screen("", value_dict, plot_history, ["good_result", "bad_result"])
    if res == "good_result":
        jump a_goodresult
    if res == "bad_result":
        jump a_badresult

label a_goodresult:
    scene bg classroom
    with fade

    python:
        # 第一幕情节描述
        scen_desc_1 = """
        时间：大学第一次考试出分后
        地点：大学教室
        人物：我，同学，老师
        场景描述：随着开学第一次考试的顺利结束，我感到一种释然。同学和老师都对我的考试表现表示开心，他们鼓励我继续保持这种学习态度。我对自己的表现也感到自豪，对大学生活更加充满信心。
        """

        # 调用AI生成新剧情
        new_plot = text_ai_with_loading_screen(scen_desc_1, plot_history, value_dict)

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

        # 更新剧情历史
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])

        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:+0~+0,A:+1~+5,B:+0~+0,M:+1~+5,S:+0~+0,F:+0~+0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    # 跳转到大学场景
    jump a_dailylife

label a_badresult:
    scene bg classroom
    with fade
    
    python:
        # 第一幕情节描述
        scen_desc_1 = """
        时间：大学开学第一次考试出分后
        地点：大学教室
        人物：我，同学，老师
        场景描述：开学第一次考试的成绩出炉，我感到有些失望。室友和老师都安慰我，提醒我这只是开始，还有很多机会可以提升。我决定从这次经历中吸取教训，更加努力地准备下一次考试。

        """

        # 调用AI生成新剧情
        new_plot = text_ai_with_loading_screen(scen_desc_1, plot_history, value_dict)

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

        # 更新剧情历史
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])

        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:-5~-3,A:-1~-5,B:-3~-1,M:-1~-5,S:+0~+0,F:+0~+0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    # 跳转到大学场景
    jump a_dailylife