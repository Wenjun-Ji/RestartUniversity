# 大学场景
label a_PEclass:
    scene bg gym
    with fade

    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：体育馆 
        人物：我，同学，老师  
        场景描述：体育课上，学生们做着简单的热身，有些人积极参与，也有人动作放缓。操场上既有比赛的呐喊声，也有轻松的交谈。老师适时指导，整体氛围介于放松和专注之间。
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
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
                else:
                    continue

    $ res = select_ai_with_loading_screen("我在上体育课", value_dict, plot_history, ["normal_class", "PE_test","tired"])
    if res == "normal_class":
        $ plot_history.extend([f"体育课正常进行"])
        jump a_normal_class
    if res == "PE_test":
        $ plot_history.extend([f"体育课进行测试"])
        jump a_PE_test
    if res == "tired":
        $ plot_history.extend([f"体育课我感到疲惫"])
        jump a_tired

# 正常体育课场景
label a_normal_class:
    scene bg gym
    with fade

    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：体育馆  
        人物：我，同学，老师  
        场景描述：体育课顺利进行，我按计划完成了热身和各项练习，动作流畅，状态良好。与同学们的配合自然，气氛轻松而有序。整堂课在老师的指导下圆满结束，感觉收获颇丰。
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
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
        
        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:+0~+5,A:+0~+3,B:+5~+10,M:+5~+8,S:+5~+8,F:0~0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_chuanggao

# 体育课测试场景
label a_PE_test:
    scene bg gym
    with fade

    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：体育馆  
        人物：我，同学，老师 
        场景描述：体育课测试按计划展开，学生们依次完成项目，如跑步、立定跳远等。有人表现轻松，有人略显紧张。老师记录成绩，并简短提醒要点。测试过程有序进行。我思考是否认真对待此次体育测试。
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
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
                else:
                    continue
        
    # 玩家互动选项
    menu:
        "认真对待体育测试":
            $ plot_history.extend([f"旁白：我决定认真对待体育测试"])
            jump a_takeitseriously
        
        "对体育测试敷衍了事":
            $ plot_history.extend([f"旁白：我决定对体育测试敷衍了事"])
            jump a_notseriously

# 认真对待体育测试场景
label a_takeitseriously:
    scene bg gym
    with fade

    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：体育馆  
        人物：我，同学，老师  
        场景描述：体育测试中，我全力以赴，认真对待每个项目。从热身到冲刺，努力发挥最佳水平。面对老师记录成绩时，感到充实且自信。测试结束时，心中有一种达成目标的满足感。
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
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
                else:
                    continue
        
        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:-5~-3,A:+0~+5,B:+5~+10,M:+5~+8,S:+1~+3,F:+0~+0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_chuanggao

label a_notseriously:
    scene bg gym
    with fade

    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：体育馆  
        人物：我，同学，老师  
        场景描述：体育测试中，我心不在焉地应付每个项目，跑步放水，动作随意，甚至在等待时玩起手机。老师记录成绩时，我毫无兴趣，测试结束后只是觉得解脱，对结果也毫不关心。
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
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
                else:
                    continue
        
        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:-1~-5,A:-5~-3,B:-5~-10,M:-5~-10,S:-1~-3,F:+0~+0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_chuanggao

# 体育课疲劳场景
label a_tired:
    scene bg gym
    with fade

    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：体育馆  
        人物：我，同学，老师  
        场景描述：体育课上，我感到十分疲劳，每个动作都变得沉重乏力。跑步时呼吸急促，四肢像灌了铅，连站在一旁等待时也只想休息。老师的指令听得模糊，整个过程像是在勉强支撑自己完成。
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
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
                else:
                    continue
        
    # 玩家互动选项
    menu:
        "坚持上课":
            $ plot_history.extend([f"我坚持认真上体育课"])
            jump a_persistPE

        "请假":
            $ plot_history.extend([f"我选择对这次体育课请假"])
            jump a_leavePE

        "逃课去娱乐":
            $ plot_history.extend([f"我选择逃课去娱乐"])
            jump a_playPE

# 体育课坚持上课场景
label a_persistPE:
    scene bg gym
    with fade

    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：体育馆  
        人物：我，同学，老师  
        场景描述：即使感到疲惫，我仍然坚持完成体育课。跑步时步伐变慢，但没停下来，每个项目都尽力去做。虽然身体沉重，但我不断调整呼吸，跟上老师的指令。课程结束时，疲惫和坚持交织，内心带着一丝满足。
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
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
                else:
                    continue
        
        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:-10~-5,A:0~0,B:+5~+8,M:+3~+5,S:+0~+0,F:+0~+0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_chuanggao

label a_leavePE:
    scene bg gym
    with fade

    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：体育馆  
        人物：我，同学，老师  
        场景描述：体育馆内回荡着篮球拍地和运动鞋摩擦地板的声音。我感到一阵阵疲惫袭来，头重脚轻。看着同学们精神抖擞地做着热身运动，我艰难地起身，走到正在布置训练的老师面前，说明身体不适想请假休息。
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
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
                else:
                    continue
        
        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:-1~-5,A:-1~-5,B:-5~-3,M:-5~-3,S:-1~-3,F:0~0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_chuanggao

label a_playPE:
    scene bg gym
    with fade
    
    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：体育馆  
        人物：我，同学，老师  
        场景描述：汗水和橡胶的气味充斥着体育馆。我望着老师示范动作，只觉浑身乏力，实在提不起劲。悄悄收拾好书包，趁老师转身指导其他同学时，我溜向后门。穿过走廊，夹杂着一丝愧疚和期待，我加快脚步奔向街角那家灯光闪烁的游戏厅。
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
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
                else:
                    continue
        
        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:-1~-5,A:-5~-8,B:-1~-5,M:-5~-10,S:-5~-10,F:-5~-10", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_chuanggao