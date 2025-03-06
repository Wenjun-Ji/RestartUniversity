# 大学场景
label a_community:
    scene bg university
    with fade

    python:
        scen_desc_1 = """
        时间：大学开学一个月后
        地点：大学校园
        人物：我，同学，社团负责人
        场景描述：我参加了社团的迎新活动，这是一个充满活力的场合。社团负责人热情地介绍各种社团活动，我被各种有趣的项目所吸引，开始考虑加入哪个社团来丰富我的大学生活。
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
                elif key == "社团负责人":
                    renpy.show("u", at_list=[player_right])
                    renpy.say(u, value)
                    renpy.hide("u")
                elif key == "同学":
                    renpy.show("classmate", at_list=[player_right])
                    renpy.say(classmate, value)
                    renpy.hide("classmate")
                else:
                    continue;

    # 玩家互动选项
    menu:
        "我选择参加社团":
            $ plot_history.extend([f"旁白：我选择参加社团"])
            jump a_joincommunity
        
        "我选择不参加社团":
            $ plot_history.extend([f"旁白：我选择不参加社团"])
            jump a_notjoincommunity

label a_joincommunity:
    scene bg university
    with fade

    python:
        # 第一幕情节描述
        scen_desc_1 = """
        时间：大学开学后
        地点：学生活动中心
        人物：我，同学，社团负责人
        场景描述：在同学的鼓励下，我决定加入一个社团，以拓宽我的社交圈并发展个人兴趣。社团负责人热情地欢迎新成员，向我介绍了社团的宗旨和即将举办的活动。我感到兴奋，期待在社团中结交新朋友并参与有趣的项目。
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
                elif key == "社团负责人":
                    renpy.show("u", at_list=[player_right])
                    renpy.say(u, value)
                    renpy.hide("u")
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
                else:
                    continue

        # 更新剧情历史
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])

        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:-10~-5,A:-3~0,B:+0~+0,M:+5~+10,S:+5~+10,F:-3~0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    # 跳转到大学场景
    jump a_freshtest

label a_notjoincommunity:
    scene bg university
    with fade
    
    python:
        # 第一幕情节描述
        scen_desc_1 = """
        时间：大学开学后
        地点：学生活动中心
        人物：我，同学，社团负责人
        场景描述：尽管室友和社团负责人热情地邀请我加入社团，我决定暂时不参加任何社团。我需要更多时间来适应大学生活，并且想专注于学业。我感谢他们的邀请，并表示将来有机会再加入。
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
                elif key == "社团负责人":
                    renpy.show("u", at_list=[player_right])
                    renpy.say(u, value)
                    renpy.hide("u")
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
                else:
                    continue

        # 更新剧情历史
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])

        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:+1~+5,A:0~+2,B:0~0,M:+0~+0,S:-1~-5,F:0~0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    # 跳转到大学场景
    jump a_freshtest