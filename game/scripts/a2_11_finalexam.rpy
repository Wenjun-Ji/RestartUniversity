label a_finalexam:
    stop music fadeout 1.0
    play music "audio/紧张.mp3" fadein 1.0 volume 0.5 loop
    scene bg study
    with fade
    python:
        scen_desc_1 = """
        时间：期末考试前两周
        地点：校园
        人物：我，同学
        场景描述：期末考试临近，校园里处处可见复习的身影。图书馆座位一位难求，自习室里安静得能听见翻书声。手机上的复习群里不断有同学讨论难题，分享复习资料。考试的压力和紧张感在空气中弥漫，我需要为自己制定一个合适的复习计划。
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
                else:
                    continue

    # 玩家互动选项
    menu:
        "在图书馆泡一整天":
            $ plot_history.extend(["旁白：我选择在图书馆复习"])
            jump a_study_library

        "在宿舍复习":
            $ plot_history.extend(["旁白：我选择在宿舍复习"])
            jump a_study_dorm

        "参加学校组织的辅导班":
            $ plot_history.extend(["旁白：我选择参加辅导班"])
            jump a_study_class

        "在教室找角落，戴耳机听轻音乐":
            $ plot_history.extend(["旁白：我选择在教室听音乐复习"])
            jump a_study_classroom

        "在咖啡馆找角落复习":
            $ plot_history.extend(["旁白：我选择在咖啡馆复习"])
            jump a_study_cafe

# 图书馆复习场景
label a_study_library:
    scene bg library
    with fade
    python:
        scen_desc_2 = """
        时间：一整天
        地点：图书馆
        人物：我
        场景描述：我一大早就赶到图书馆占座。身边都是认真学习的同学，这种氛围让人不自觉地也专注起来。中午简单吃了个便当，继续投入复习。虽然一天下来有些疲惫，但完成了预定的复习计划，感觉很充实。
        """
        
        # 调用AI生成新的场景剧情
        new_plot = text_ai_with_loading_screen(scen_desc_2, plot_history, value_dict)

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
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:-5~-10,A:+10~+15,B:-1~-5,M:+1~+5,S:+0~+0,F:-1~-3", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_examination

# 宿舍复习场景
label a_study_dorm:
    scene bg dorm
    with fade
    python:
        scen_desc_3 = """
        时间：一整天
        地点：宿舍
        人物：我
        场景描述：选择在熟悉的宿舍环境复习。虽然时不时会被室友的动静分散注意力，但省去了来回奔波的时间。整理出一块自己的专注空间，戴上降噪耳机，按照计划稳步推进复习进度。
        """
        
        # 调用AI生成新的场景剧情
        new_plot = text_ai_with_loading_screen(scen_desc_3, plot_history, value_dict)

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
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:-10~-5,A:+10~+15,B:-3~-1,M:+3~+5,S:0~0,F:0~0", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
        
    jump a_examination

# 辅导班复习场景
label a_study_class:
    scene bg classroom
    with fade
    python:
        scen_desc_4 = """
        时间：晚上
        地点：教室
        人物：我，老师
        场景描述：参加学校组织的辅导班，老师讲解复习重点和难点。和同学们一起讨论问题，解答疑惑。虽然时间不长，但老师的讲解和同学的讨论让我受益匪浅，对考试内容有了更深的理解。
        """
        
        # 调用AI生成新的场景剧情
        new_plot = text_ai_with_loading_screen(scen_desc_4, plot_history, value_dict)

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
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:-5~-10,A:+10~+15,B:-1~-3,M:+5~+8,S:+5~+8,F:+0~+0", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_examination

# 教室复习场景
label a_study_classroom:
    scene bg classroom
    with fade
    python:
        scen_desc_5 = """
        时间：一整天
        地点：教室
        人物：我
        场景描述：找到一间僻静的空教室，戴上耳机放着轻音乐。音乐让紧张的心情逐渐平静，周围的环境也很适合专注。偶尔抬头望向窗外，阳光温柔地洒在书本上，营造出舒适的学习氛围。
        """
        
        # 调用AI生成新的场景剧情
        new_plot = text_ai_with_loading_screen(scen_desc_5, plot_history, value_dict)

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
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:-5~-8,A:+8~+12,B:-3~-1,M:+5~+10,S:0~0,F:-2~-1", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_examination

# 咖啡馆复习场景
label a_study_cafe:
    scene bg cafe
    with fade
    python:
        scen_desc_6 = """
        时间：一整天
        地点：咖啡馆
        人物：我
        场景描述：选择在咖啡馆复习，环境轻松，咖啡香气扑鼻。点了一杯喜欢的咖啡，搭配一份小点心，让复习的时间变得更加惬意。虽然偶尔会被周围的谈笑声分散注意力，但总体效率还不错。
        """
        
        # 调用AI生成新的场景剧情
        new_plot = text_ai_with_loading_screen(scen_desc_6, plot_history, value_dict)

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
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:-8~-5,A:+8~+12,B:-5~-3,M:+5~+10,S:+3~+5,F:-15~-10", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_examination

        
