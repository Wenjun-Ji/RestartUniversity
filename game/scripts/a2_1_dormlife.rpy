# 大学场景
label a_dormlife:
    scene bg dormitory  # 这个是大学校园背景
    with fade

    python:
        scen_desc_1 = """
        时间：大学开学第一天晚  
        地点：宿舍  
        人物：我，室友  
        场景描述：宿舍里四人围坐吃着小吃，聊着各自的兴趣爱好，气氛逐渐融洽。熄灯后，大家还在轻声讨论社团活动，主角默默思考即将到来的新生活。
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
                else:
                    continue

    # 玩家互动选项
    menu:
        "对宿舍生活满意":
            $ plot_history.extend([f"旁白：我对宿舍生活满意"])
            jump a_satisfiedlife
        
        "对宿舍生活不满意":
            $ plot_history.extend([f"旁白：我对宿舍生活不满意"])
            jump a_dissatisfiedlife

label a_satisfiedlife:
    scene bg dormitory  # 这个是家中客厅的背景，你可以根据实际场景设置
    with fade
    
    python:
        # 第一幕情节描述
        scen_desc_1 = """
        时间：大学开学一段时间后
        地点：大学宿舍
        人物：我，室友
        场景描述：在宿舍住了一段时间后，我对宿舍生活感到满意。室友和我相处融洽，共同适应了大学生活的节奏。我们一起学习，一起生活，一起度过了许多美好时光。
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
                elif key == "室友":
                    renpy.show("roommate", at_list=[player_right])
                    renpy.say(roommate, value)
                    renpy.hide("roommate")
                else:
                    continue


        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:+1~+5,A:0~0,B:+3~+5,M:+5~+10,S:+5~+10,F:+0~+0", value_dict)
        
        # 显示属性变化
        #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    # 跳转到大学场景
    jump a_stuorg

label a_dissatisfiedlife:
    scene bg dormitory  # 这个是家中客厅的背景，你可以根据实际场景设置
    with fade
    
    python:
        # 第一幕情节描述
        scen_desc_1 = """
        时间：大学开学一段时间后
        地点：大学宿舍
        人物：我，室友
        场景描述：一段时间的宿舍生活让我感到不适应，我对狭小的空间和室友的夜间噪音感到不满，这影响了我的日常学习和休息。室友似乎并未意识到这些问题，这使我心情低落。
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
                elif key == "室友":
                    renpy.show("roommate", at_list=[player_right])
                    renpy.say(roommate, value)
                    renpy.hide("roommate")
                else:
                    continue

        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:-5~-1,A:-5~-3,B:-5~-3,M:-10~-5,S:-10~-5,F:+0~+0", value_dict)
        
        # # 显示属性变化
        # #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    # 跳转到大学场景
    jump a_stuorg