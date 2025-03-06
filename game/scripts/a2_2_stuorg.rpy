# 大学场景
label a_stuorg:
    scene bg university  # 这个是大学校园背景
    with fade

    python:
        scen_desc_1 = """
        时间：大学开学后
        地点：大学学生组织招新摊位
        人物：我，同学，学生组织成员
        场景描述：随着大学生活逐渐步入正轨，学生组织开始招新。我站在摊位前，浏览着各个组织的介绍，思考着是否要加入。学生组织成员积极地向我们介绍各自的特色和活动，鼓励我们根据自己的兴趣做出选择。我认真考虑着加入学生组织可能带来的新挑战和机遇。
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
                elif key == "学生组织成员":
                    renpy.show("member", at_list=[player_right])
                    renpy.say(member, value)
                    renpy.hide("member")
                else:
                    continue

    # 玩家互动选项
    menu:
        "我选择参加学生组织":
            $ plot_history.extend([f"旁白：我选择参加学生组织"])
            jump a_joinstuorg
        
        "我选择不参加学生组织":
            $ plot_history.extend([f"旁白：我选择不参加学生组织"])
            jump a_notjoinstuorg

label a_joinstuorg:
    scene bg university
    with fade

    python:
        # 第一幕情节描述
        scen_desc_1 = """
        时间：大学开学后
        地点：学生活动中心
        人物：我，同学，学生组织成员
        场景描述：在同学的鼓励下，我决定加入一个学生组织，以提升我的组织能力和团队合作精神。学生组织成员热情地欢迎新成员，向我介绍了组织的宗旨和即将举办的活动。我感到兴奋，期待在组织中结交新朋友并参与有意义的项目。
        """

        # 调用AI生成新剧情
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
                elif key == "学生组织成员":
                    renpy.show("member", at_list=[player_right])
                    renpy.say(member, value)
                    renpy.hide("member")
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
                else:
                    continue

        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:-5~-10,A:-3~0,B:+0~+0,M:+8~+12,S:+5~+10,F:+0~+0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    # 跳转到大学场景
    jump a_community

label a_notjoinstuorg:
    scene bg library
    with fade
    
    python:
        # 第一幕情节描述
        scen_desc_1 = """
        时间：大学开学后
        地点：图书馆
        人物：我，同学，学生组织成员
        场景描述：在同学的鼓励下，我认真考虑了加入学生组织的提议，但最终决定不加入。我需要更多时间来适应大学生活，并且想专注于学业。
        """

        # 调用AI生成新剧情
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
                elif key == "学生组织成员":
                    renpy.show("member", at_list=[player_right])
                    renpy.say(member, value)
                    renpy.hide("member")
                elif key == "老师":
                    renpy.show("teacher", at_list=[player_right])
                    renpy.say(teacher, value)
                    renpy.hide("teacher")
                else:
                    continue

        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:+1~+5,A:0~+2,B:0~0,M:-1~-5,S:-1~-5,F:0~0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    # 跳转到大学场景
    jump a_community