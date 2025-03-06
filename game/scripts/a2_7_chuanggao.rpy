label a_chuanggao:
    scene bg dormitory
    with fade

    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：宿舍
        人物：我，同学，室友
        场景描述：我躺在宿舍床上，望着手机里未完成的跑步任务提醒。窗外夜色渐浓，寒风拍打着窗户。"要不明天再跑？"我翻了个身，但想到App里显示的完成率和可能的惩罚措施，还是烦躁地坐了起来。室友们有的已经去了操场，有的也在床上犹豫。我叹了口气，慢慢穿上运动鞋，思考着到底要不要在这个寒冷的夜晚出门。
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
                elif key == "室友":
                    renpy.show("roommate", at_list=[player_right])
                    renpy.say(roommate, value)
                    renpy.hide("roommate")
                else:
                    continue

    $ res = select_ai_with_loading_screen("我思考是否去操场跑步", value_dict, plot_history, ["normal_run", "rainy_day","lazy_run"])
    if res == "normal_run":
        $ plot_history.extend([f"我按时去操场完成跑步任务"])
        jump a_normal_run
    if res == "rainy_day":
        $ plot_history.extend([f"我因为外面下雨没有去操场跑步"])
        jump a_rainy_day
    if res == "lazy_run":
        $ plot_history.extend([f"我因为懒惰没有去操场跑步"])
        jump a_lazy_run

# 正常跑步场景
label a_normal_run:
    scene bg playground
    with fade

    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：操场  
        人物：我，同学
        场景描述：夜幕降临，操场的灯光明亮如昼。寒风中，我系紧运动鞋带，调整好手机里的运动APP。"反正每天都要跑，早跑完早轻松。"我轻声自语，迈出了第一步。跑道上三三两两都是匆匆赶来完成任务的同学，大家互相点头致意，在寒风中坚持着日常的两公里。运动数据在手机里稳步增长，熟悉的夜跑又开始了。
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
        
        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:-5~-3,A:0~0,B:+5~+10,M:+5~+10,S:+1~+5,F:0~0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_stuactivity

# 下雨天场景
label a_rainy_day:
    scene bg rainy_playground
    with fade
    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：下雨的操场  
        人物：我，同学
        场景描述：窗外雨声淅沥，天空阴沉沉的毫无放晴迹象。我焦虑地盯着手机里未完成的跑步任务，室友们都窝在床上刷手机，谁都不想在这种天气出门。我看了看自己连续打卡的记录，遗憾地意识到今天可能要中断了。
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
        
        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:+0~+0,A:0~0,B:-3~0,M:-3~0,S:0~0,F:0~0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_stuactivity

# 懒惰跑步场景
label a_lazy_run:
    scene bg dormitory
    with fade
    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：下雨的操场  
        人物：我，同学
        场景描述：手机屏幕上的运动任务提醒亮了又暗。我裹着被子，室友喊我一起去操场，我随便找了个肚子疼的借口搪塞过去。运动记录里的进度条停在0%，但此刻只想在床上躺平，管它什么任务不任务。
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
        
        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:+1~+5,A:0~0,B:-1~-5,M:-3~0,S:-3~0,F:0~0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_stuactivity