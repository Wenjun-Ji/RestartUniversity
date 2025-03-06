############################################以下为高考考砸了的故事线############################################
#############################################################################################################


### 第一幕
### 主角在期盼中查看录取情况，发现自己并未考上理想的大学。
### 主角感到一阵失落，父母的反应可能会随机不同，有可能是安慰和鼓励，有可能是失望和责备
### 你开始思考下一步的选择，是选择重考，还是去次优的大学？

# 高考考砸了的故事线
label a_gaokao_bad:
    stop music fadeout 1.0
    play music "audio/舒缓低沉.mp3" fadein 1.0 volume 0.5 loop
    # 显示场景
    scene bg home_living_room

    $ quick_menu = True
    call enable_user_interaction from _call_enable_user_interaction
    
    # 定义角色
    # 在script.rpy中定义了角色，这里直接引用
    
    python:
        # 第一幕情节描述
        scen_desc = """
        时间：高考出结果后
        地点：家中
        人物：我，爸爸，妈妈
        场景描述：
        查分后的情绪波动：我发现自己没有考上理想的大学，情绪低落。不同父母得知消息后，表现出的反应会有所不同。
        父母的反应可能是（以下只是示例）：
        - 对结果感到失望，可能会责备你没有努力；
        - 则可能表示安慰和鼓励，让你不要放弃，并可以考虑重考； 
        - 我的内心独白反映他对未来的不确定感，以及对接下来的选择（复读或去次优的大学）的思考。
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
                elif key == "爸爸":
                    renpy.show("father", at_list=[player_right])
                    renpy.say(father, value)  # "爸爸" 的对话
                    renpy.hide("father")
                elif key == "妈妈":
                    renpy.show("mother", at_list=[player_right])
                    renpy.say(mother, value)  # "妈妈" 的对话
                    renpy.hide("mother")
                else:
                    continue  # 如果没有匹配的角色，继续循环

    # 显示选择菜单
    menu:
        "选择复读，决心再战一年":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我选择了复读，决心再战一年，父母对此的反应各不相同。"]) # 强调选择后的情绪和后果
                scen_desc = """
                地点：家中
                人物：我，爸爸，妈妈
                场景描述：
                我选择了复读，决心再战一年，父母对此的反应各不相同。
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
                            renpy.say(p, value) # "我" 的对话
                            renpy.hide("p")
                        elif key == "爸爸":
                            renpy.show("father", at_list=[player_right])
                            renpy.say(father, value)  # "爸爸" 的对话
                            renpy.hide("father")
                        elif key == "妈妈":
                            renpy.show("mother", at_list=[player_right])
                            renpy.say(mother, value)  # "妈妈" 的对话
                            renpy.hide("mother")
                        else:
                            continue  # 如果没有匹配的角色，继续循环
                
                # 调用AI更新属性
                li = value_ai_with_loading_screen(new_plot, "E:-5~-10,A:+0~+0,B:-5~-10,M:+0~+0,S:+0~+0,F:+0~+0", value_dict)  # 根据复读选项更新属性
            
            jump end  # 结束游戏

        "接受现实，选择次优的大学":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我选择了接受现实，准备去次优的大学，内心仍有些许遗憾，但父母最终支持了这个决定。"]) # 强调选择后的情绪和后果
                scen_desc = """
                时间：高考出结果后
                地点：家中
                人物：我，爸爸，妈妈
                场景描述：
                我选择了主角选择了接受现实，准备去次优的大学，内心仍有些许遗憾，但父母最终支持了这个决定。
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
                        elif key == "爸爸":
                            renpy.show("father", at_list=[player_right])
                            renpy.say(father, value)  # "爸爸" 的对话
                            renpy.hide("father")
                        elif key == "妈妈":
                            renpy.show("mother", at_list=[player_right])
                            renpy.say(mother, value)  # "妈妈" 的对话
                            renpy.hide("mother")
                        else:
                            continue  # 如果没有匹配的角色，继续循环
                # 调用AI更新属性
                li = value_ai_with_loading_screen(new_plot, "E:+0~+0,A:+0~+0,B:+0~+0,M:+5~+8,S:+0~+0,F:+0~+0", value_dict)  # 根据选择次优大学更新属性
             
            jump a_plan_summer_bad  # 选择次优大学，进入下一场景



### 第二幕
### 决定选择次优的大学后，这个夜晚主角的心情低落到了极点
### 躺在床上睡不着觉，主角开始思考如何度过这个漫长的暑假

label a_plan_summer_bad:
    # 显示场景
    scene bg bedroom  # 这里可以是卧室睡觉的场景
    with fade
    # 定义角色
    # 在script.rpy中定义了角色，这里直接引用

    python:
        # 第二幕情节描述
        scen_desc = """
        时间：夜里睡觉前
        地点：床上
        人物：我
        场景描述：
            我刚刚决定选择次优的大学，心情跌到了谷底，满脑子都是考试的失误和未来的不确定。
            躺在床上辗转反侧，心情无法平静。我一边懊悔没能考上理想的学校，一边思考如何度过漫长的暑假。
            心里在犹豫：应该彻底放松，玩个痛快？还是为了不再重蹈覆辙，提前准备大学课程？
            **注意该场景只有我一个人，主要是心理活动，并且生成的对话要求不能表明主角已经确定的选择，而是在选项之间再犹豫不决**
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
                elif key == "爸爸":
                    renpy.show("father", at_list=[player_right])
                    renpy.say(father, value)  # "爸爸" 的对话
                    renpy.hide("father")
                elif key == "妈妈":
                    renpy.show("mother", at_list=[player_right])
                    renpy.say(mother, value)  # "妈妈" 的对话
                    renpy.hide("mother")
                else:
                    continue  # 如果没有匹配的角色，继续循环

    # 显示选择菜单
    menu:
        "过去的已然过去，未来的路还很长，先玩再说":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我决定先玩再说，决定彻底放松，享受这个暑假，暂时不去考虑未来。"])
                # 调用AI更新属性
                li = value_ai_with_loading_screen(new_plot, "E:+5~+10,A:-8~-12,B:+0~+0,M:+0~+5,S:+0~+0,F:-5~-10", value_dict)  # 根据选择放松更新属性
            
            # 选择放松，进入下一场景
            jump a_talk_with_parents_bad

        "考的这么差，还是先学点大学课程吧":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我决定提前学习大学课程，想要尽早为即将到来的大学生活做准备。"])
                # 调用AI更新属性
                li = value_ai_with_loading_screen(new_plot, "E:-5~-8,A:+8~+15,B:+0~+0,M:+0~+0,S:+0~+0,F:+0~+0", value_dict)  # 根据选择学习更新属性
             
            # 选择学习，进入下一场景
            jump a_walk_alone_bad

        "迷茫，不知道该怎么办，先睡一觉再说":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我感到迷茫，不知道该怎么办，选择先睡一觉再说。"])
                # 调用AI更新属性
                li = value_ai_with_loading_screen(new_plot, "E:+5~+8,A:+0~+0,B:+2~+5,M:+1~+5,S:+0~+0,F:0~0", value_dict)  # 根据选择睡觉更新属性
            
            # 选择睡觉，进入下一场景
            jump a_talk_with_parents_bad




### 第三幕
### 因为高考的失利，主角彻底迷失自我
### 爸妈建议主角好好规划以下自己的暑假，不能因为一时的失利就丢失自我，人生的路还很长。
### 他们希望你在假期中可以做一些对大学有帮助的事情，在大学重新证明自我，或者提前获得一些技能，比如练车。
### 你感到压力逐渐增加，尽管成绩很好，但未来的路看似更难走。你不得不在享受假期和满足家人的期待中找到平衡。
### 你可以选择听取家长建议，你将获得额外的经验，但可能牺牲个人休闲时间；你也可以与他们沟通，获得自己的空间；也可以完全不听，一直享受放松带来的快乐

label a_talk_with_parents_bad:
    # 显示场景
    scene bg home_living_room  # 这个是家中客厅的背景，你可以根据实际场景设置
    with fade

    # 定义角色
    # 在script.rpy中定义了角色，这里直接引用

    python:
        # 第一幕情节描述
        scen_desc = """
        时间：傍晚
        地点：家中
        人物：我，爸爸，妈妈
        场景描述：
            我彻底放弃自我，经常夜不归宿，爸爸妈妈对此比较担心，决定和我好好聊一番。
            爸妈建议我好好规划以下自己的暑假，不能因为一时的失利就丢失自我，人生的路还很长。
            他们希望我在假期中可以做一些对大学有帮助的事情，在大学重新证明自我，或者提前获得一些技能，比如练车。
            我感到压力逐渐增加
            到底是选择，不知道到底自己该怎样......
            **注意生成的对话要求不能表明主角已经确定的选择，而是在选项之间再犹豫不决**
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
                    renpy.say(p, value)
                    renpy.hide("p")
                elif key == "爸爸":
                    renpy.show("father", at_list=[player_right])
                    renpy.say(father, value)  # "爸爸" 的对话
                    renpy.hide("father")
                elif key == "妈妈":
                    renpy.show("mother", at_list=[player_right])
                    renpy.say(mother, value)  # "妈妈" 的对话
                    renpy.hide("mother")
                else:
                    continue  # 如果没有匹配的角色，继续循环

    # 显示重开按钮
    menu:
        "学车":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我选择听爸妈的，觉得不能再荒废下去了，决定去学开车"])# 这个地方可以人工强调选择的后果，也可让AI自己判断
                # 调用AI更新属性
                li = value_ai_with_loading_screen(new_plot, "E:-1~-5,A:+1~+5,B:-3~+3,M:+-3~+3,S:+1~+5,F:-5~-10", value_dict)
                # 显示属性变化
                # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            
            # 选择学车，进入下一场景
            jump a_walk_alone_bad

        "学习大学的知识":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我选择了听爸妈的，觉得不能再荒废下去了，决定去提前学习大学知识"])
                # 调用AI更新属性
                li = value_ai_with_loading_screen(new_plot, "E:-5~-8,A:+8~+12,B:+0~+0,M:-1~-5,S:+0~+0,F:+0~+0", value_dict)
                # 显示属性变化
                # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
             
            # 选择学习，进入下一场景
            jump a_walk_alone_bad

        "挣点小钱":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我选择暑假打工挣点小钱"])
                # 调用AI更新属性
                li = value_ai_with_loading_screen(new_plot, "E:-5~-8,A:-5~-10,B:+0~+0,M:+3~+5,S:+5~+10,F:+8~+12", value_dict)
                # 显示属性变化
                # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
             
            # 选择打工，进入下一场景
            jump a_walk_alone_bad

        "接着玩":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我选择接着彻底放松"])
                # 调用AI更新属性
                li = value_ai_with_loading_screen(new_plot, "E:+1~+5,A:-8~-12,B:+0~+0,M:+0~+0,S:+0~+0,F:-5~-8", value_dict)
                # 显示属性变化
                # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
             
            # 选择放松，进入下一场景
            jump a_walk_alone_bad    




### 第四幕
### 暑假接近尾声，大学即将开始。漫长假期带来的空虚和面对全新未来的迷茫还有即将告别亲朋好友去外地的不舍交织在心头
### 于是主角一个人去江边散步，展开了有一次丰富的心理活动
### 主角反思这段时间的经历，回顾假期里做出的决定。
### 是选择在继续追逐高考后的轻松生活，还是将注意力集中到即将到来的大学生涯中。
### 未来的学术道路和职业选择已经摆在面前，大学生活的准备是否充分将影响你接下来的经历。

label a_walk_alone_bad:
    # 显示场景
    scene bg riverside  # 这个是江边的日落风景
    with fade
    
    # 定义角色
    # 在script.rpy中定义了角色，这里直接引用

    # AI生成情节
    python:
        # 第一幕情节描述
        scen_desc = """
        时间：黄昏
        地点：湖边
        人物：我
        场景描述：
            暑假接近尾声，大学即将开始。漫长假期带来的空虚和面对全新未来的迷茫还有即将告别亲朋好友去外地的不舍交织在心头。
            高考的失利再次让主角感到心痛和迷茫，不知道未来的路该怎么走。
            难道高考失利这辈子就完了吗？还是应该好好规划自己的大学生活？
            我一个人去江边散步，反思这段时间的经历，回顾假期里做出的决定并对未来的大学生活做了初步的展望，展开了有一次丰富的心理活动。
            **注意该场景只有主角一个人，主要是心理活动**
            **注意生成的对话要求不能表明主角已经确定的选择，而是在选项之间再犹豫不决**
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
                elif key == "爸爸":
                    renpy.show("father", at_list=[player_right])
                    renpy.say(father, value)  # "爸爸" 的对话
                    renpy.hide("father")
                elif key == "妈妈":
                    renpy.show("mother", at_list=[player_right])
                    renpy.say(mother, value)  # "妈妈" 的对话
                    renpy.hide("mother")
                else:
                    continue  # 如果没有匹配的角色，继续循环

    # 显示选择按钮
    menu:
        "我高考失利了，这辈子也就这样了，不想再继续努力了":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我觉得我高考失利了，这辈子也就这样了，我不想再继续努力了"])# 这个地方可以人工强调选择的后果，也可让AI自己判断
                # 调用AI更新属性
                li = value_ai_with_loading_screen(new_plot, "E:+0~+5,A:-10~-15,B:+0~+0,M:-8~-15,S:+0~+0,F:+0~+0", value_dict)
                # 显示属性变化
                # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            
            jump a_leave_home  # 先玩再说

        "我的人生路还长，不能因为一时的失利就放弃，我要在大学重新证明自己":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我觉得我的人生路还长，不能因为一时的失利就放弃，我决定要在大学重新证明自己"])
                # 调用AI更新属性
                li = value_ai_with_loading_screen(new_plot, "E:+0~+0,A:+1~+5,B:+0~+0,M:-5~-10,S:+0~+0,F:+0~+0", value_dict)
                # 显示属性变化
                # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
             
            jump a_leave_home  # 学习大学课程
