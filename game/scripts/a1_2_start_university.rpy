

######################################以下为暑假结束去开学的路上的故事线#######################################
#############################################################################################################

### 本段为去新生报道的路上
### 这是一个过渡的场景，用于连接暑假结束和新学期开始的故事线
### 大致包含 和家人分别、走进大学校门、新生报道等情节


### 第一幕 出发踏上去大学的路途 与家人分别

label a_leave_home:
    # 显示场景
    scene bg farewell  # 在车站和爸妈分别的场景
    with fade
    # 定义角色
    # 在script.rpy中定义了角色，这里直接引用

    # AI生成对话
    python:
        # 第一幕情节描述
        scen_desc = """
        时间：清晨
        地点：车站
        人物：我，爸爸，妈妈
        场景描述：结束了人生中最长的暑假,我即将踏上去大学的路途。一大清早，车站的人群熙熙攘攘，我和爸爸妈妈站在一起，等待着火车的到来。爸爸妈妈看着我，眼中充满了不舍和期待。我心中有一丝悸动，即将迎来新的生活，但也不舍得离开家人。
        """

        # 调用AI生成新剧情
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
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

    # 跳转到大学场景
    jump a_train_journey


### 第二幕 我一个人望着火车的窗外，心中有些许不舍，但也充满了期待

label a_train_journey:
    # 显示场景
    scene bg chechuang  # 火车窗外的风景
    with fade
    # 定义角色
    # 在script.rpy中定义了角色，这里直接引用
    # AI生成对话
    python:
        # 第一幕情节描述
        scen_desc = """
        时间：上午
        地点：火车上
        人物：我
        场景描述：
        火车缓缓驶出车站，我一个人坐在车厢里，望着窗外飞驰的景色。心中有些许不舍，但更多的是期待。我即将踏上新的旅程，迎接新的生活，这是我人生中的一个新的开始。
        **注意该场景只有主角一个人，主要是心理活动**
        """

        # 调用AI生成新剧情
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        # 更新剧情历史
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        # 显示生成的剧情
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)  # 显示旁白
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)  # "我" 的对话
                    renpy.hide("p")
                else:
                    continue

    # 跳转到大学场景
    jump a_registration

### 第三幕 你来到大学的校门口，迎接你的是新的生活
label a_registration:
    stop music fadeout 1.0
    play music "audio/轻柔平和.mp3" fadein 1.0 volume 0.5 loop
    # 显示场景
    scene bg university_gate  # 大学校门口
    with fade
    # 定义角色
    # 在script.rpy中定义了角色，这里直接引用
    # AI生成对话
    python:
        # 第一幕情节描述
        scen_desc = """
        时间：上午
        地点：大学校门口
        人物：我，学长，学姐
        场景描述：
        经过一路的颠簸，我终于来到了大学校门口。
        拖着沉重的行李，我走进了大学校门，迎接我的是一群热情的学长学姐志愿者。他们热情地招呼着我，帮我搬行李，带我熟悉校园。我心中充满了期待和激动，新的生活即将开始。
        """

        # 调用AI生成新剧情
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)
        # 更新剧情历史
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        # 显示生成的剧情
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)  # 显示旁白
                elif key == "我":
                    renpy.show("p", at_list=[player_left])
                    renpy.say(p, value)  # "我" 的对话
                    renpy.hide("p")
                elif key == "学长":
                    renpy.show("Senior", at_list=[player_right])
                    renpy.say(Senior, value)
                    renpy.hide("Senior")
                elif key == "学姐":
                    renpy.show("Senior_sister", at_list=[player_right])
                    renpy.say(Senior_sister, value)
                    renpy.hide("Senior_sister")
                else:
                    continue

    # 跳转到大学场景
    # 进入a2
    jump a_dormlife

