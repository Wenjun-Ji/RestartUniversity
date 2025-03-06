############################################以下为高考考好的故事线############################################
#############################################################################################################

### 第一幕
### 玩家在经历引子后，选择重开会重新开启大学生活，首先回到高考查分的那一刻
### 高考查分有两种情况，第一种是成绩满意，第二种成绩不满意

# 高考考好的情况
label a_gaokao_good:
    # 显示场景
    stop music fadeout 1.0
    play music "audio/轻松欢快.mp3" fadein 1.0 volume 0.5 loop
    scene bg home_living_room
    
    $ quick_menu = True
    call enable_user_interaction from _call_enable_user_interaction_1
    
    # 定义角色
    # 在script.rpy中定义了角色，这里直接引用

    # AI生成对话
    python:
        # 第一幕情节描述
        scen_desc = """
        时间：高考出分了
        地点：家中
        人物：我，爸爸，妈妈
        场景描述：
        查分激动瞬间：主角和爸妈一起查分，主角发挥地不错，应该能上个理想的大学，一家人都很开心......
        查分后的闲聊：一家人畅想着填报哪个大学、学哪个专业......，聊着聊着最后一家人决定出去吃顿大餐，好好庆祝一下.....
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
                    continue

        # 调用AI更新属性
        # E(精力值)：表示角色的体力和精神状态
        # A(学业进度)：反映学习成果和知识积累
        # B(身体健康状况)：表示整体身体状况
        # M(心理健康状况)：反映心理压力和情绪状态
        # S(社会关系)：代表人际关系网络的广度和深度
        # F(财务状况)：表示经济能力和财务健康
        
        # 属性变化：高考成绩理想，精力增加（E），身体健康稍微提升（B），心理压力缓解（M），家庭关系提升（S）。
        li = value_ai_with_loading_screen(new_plot, "E:+1~+ 5,A:+0~+0,B:+3~+5,M:+5~+8,S:+5~+8,F:+0~+0", value_dict)
              
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    # 跳转到下一个场景
    jump a_plan_summer


### 第二幕
### 一家人在高考查分后都非常满意，出去吃完大餐后，你躺在床上睡不着觉
### 你开始打算一下如何好好度过这个漫长的暑假了
### 你可以选择彻底放松，可以有更多娱乐时间，但可能会对即将到来的大学生活准备不足；
### 亦或提前为大学生活打下基础，但可能会错过放松的机会；
### 你也可以选择在暑假打工，你将获得工作经验和人脉，但可能会感到暑假过于繁忙。

label a_plan_summer:
    # 显示场景
    scene bg bedroom  # 这里可以是卧室睡觉的场景
    with fade
    
    # 定义角色
    # 在script.rpy中定义了角色，这里直接引用

    python:
        # 第一幕情节描述
        scen_desc = """
        时间：夜里睡觉前
        地点：床上
        人物：我
        场景描述：
            主角一家人在高考查分后都非常满意，出去吃大餐欢祝后，主角的心里感到久违的放松。
            主角躺在床上开始畅想自己该如何度过这个漫长的暑假：
            是好好放松，彻底享受暑假
            还是提前学习大学课程，不能懈怠
            还是暑期打工，挣去更多零花钱
            还是......
            **注意该场景只有主角一个人，主要是心理活动，并且生成的对话要求不能表明主角已经确定的选择，而是在选项之间再犹豫不决**
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

    # 显示重开按钮
    menu:
        "管他呢，先玩再说":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我选决定开始放松，彻底享受暑假"])# 这个地方可以人工强调选择的后果，也可让AI自己判断
                # 调用AI更新属性：放松提升精力（E），但学业进度下降（A），身体和心理健康提升（B、M），财务状况下降（F）
                li = value_ai_with_loading_screen(new_plot, "E:+2~+5,A:-5~-8,B:+0~+0,M:+1~+5,S:+0~+0,F:-1~-5", value_dict)
                # 显示属性变化
                # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            
            # 跳转到下一个场景
            jump a_talk_with_parents 

        "只要卷不死，就往死里接着卷":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我决定提前学习大学课程"])
                # 调用AI更新属性：学习增加学业进度（A），但精力和心理健康下降（E、M）
                li = value_ai_with_loading_screen(new_plot, "E:-5~-8,A:+5~+10,B:-1~-3,M:-5~-10,S:+0~+0,F:+0~+0", value_dict)
                # 显示属性变化
                # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
             
            # 跳转到下一个场景
            jump a_walk_alone

        "先挣点小钱儿":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我决定暑假打工挣点钱"])
                # 调用AI更新属性：打工增加财务状况（F）和社交能力（S），但精力下降（E），学业进度下降（A）
                li = value_ai_with_loading_screen(new_plot, "E:-5~-8,A:-1~-3,B:+0~+0,M:+2~+5,S:+7~+10,F:+10~+15", value_dict)
                # 显示属性变化
                # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
             
            # 跳转到下一个场景
            jump a_walk_alone


### 第三幕
### 你彻底放松，玩到没边，经常夜不归宿，兜里的零花钱也快见底，于是找爸妈要零花钱
### 爸妈建议你好好规划以下自己的暑假，他们希望你在假期中可以接触一些和未来职业相关的资源，参与一些实习，或者提前获得一些技能，比如练车。
### 你感到压力逐渐增加，尽管成绩很好，但未来的路看似更难走。你不得不在享受假期和满足家人的期待中找到平衡。
### 你可以选择听取家长建议，你将获得额外的经验，但可能牺牲个人休闲时间；你也可以与他们沟通，获得自己的空间；也可以完全不听，一直享受放松带来的快乐

label a_talk_with_parents:
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
            主角彻底放松，玩到没边，经常夜不归宿，爸爸妈妈对此比较担心，决定和主角好好聊一番
            爸妈建议主角好好规划以下自己的暑假，他们希望你在假期中可以接触一些和未来职业相关的资源，参与一些实习，或者提前获得一些技能，比如练车。
            主角感到压力逐渐增加
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
                    continue

    # 显示重开按钮
    menu:
        "学车":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我听了爸妈的话，决定不能再荒废下去了，决定去学开车"])# 这个地方可以人工强调选择的后果，也可让AI自己判断
                # 调用AI更新属性：学车提升身体健康（B），但消耗精力（E）和财务状况（F）
                li = value_ai_with_loading_screen(new_plot, "E:-1~-5,A:+1~+5,B:-3~+3,M:+-3~+3,S:+1~+5,F:-5~-10", value_dict)
                # 显示属性变化
                # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            
            # 跳转到下一个场景
            jump a_walk_alone

        "学习大学的知识":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我听了爸妈的话，决定不能再荒废下去了，去提前学习大学知识"])
                # 调用AI更新属性：学习提升学业进度（A），但精力和心理健康下降（E、M）
                li = value_ai_with_loading_screen(new_plot, "E:-5~-8,A:+8~+12,B:+0~+0,M:-1~-5,S:+0~+0,F:+0~+0", value_dict)
                # 显示属性变化
                # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
             
            # 跳转到下一个场景
            jump a_walk_alone

        "挣点小钱":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我决定暑假打工挣点小钱"])
                # 调用AI更新属性：打工增加财务状况（F）和社交能力（S），但精力下降（E），学业进度下降（A）
                li = value_ai_with_loading_screen(new_plot, "E:-5~-8,A:-5~-10,B:+0~+0,M:+3~+5,S:+5~+10,F:+8~+12", value_dict)
                # 显示属性变化
                # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
             
            # 跳转到下一个场景
            jump a_walk_alone


        "接着玩":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我决定这个暑假接着玩"])
                # 调用AI更新属性
                li = value_ai_with_loading_screen(new_plot, "E:+1~+5,A:-8~-12,B:+0~+0,M:+0~+0,S:+0~+0,F:-5~-8", value_dict)
                # 显示属性变化
                # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
             
            # 跳转到下一个场景
            jump a_walk_alone    




### 第四幕
### 暑假接近尾声，大学即将开始。漫长假期带来的空虚和面对全新未来的迷茫还有即将告别亲朋好友去外地的不舍交织在心头
### 于是主角一个人去江边散步，展开了有一次丰富的心理活动
### 主角反思这段时间的经历，回顾假期里做出的决定。
### 是选择在继续追逐高考后的轻松生活，还是将注意力集中到即将到来的大学生涯中。
### 未来的学术道路和职业选择已经摆在面前，大学生活的准备是否充分将影响你接下来的经历。

label a_walk_alone:
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
            主角一个人去江边散步，反思这段时间的经历，回顾假期里做出的决定并对未来的大学生活做了初步的展望，展开了有一次丰富的心理活动。
            主角需要选择在大学中继续追逐轻松自由的生活，还是度过一个精心规划的大学生活。
            未来的学术道路和职业选择已经摆在面前，大学生活准备是否充分将影响你接下来的经历。
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

    # 显示选择按钮
    menu:
        "在大学享受自由开始放松":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我决定在大学享受自由开始放松"])# 这个地方可以人工强调选择的后果，也可让AI自己判断
                # 调用AI更新属性
                li = value_ai_with_loading_screen(new_plot, "E:+0~+5,A:-10~-15,B:+0~+0,M:-8~-15,S:+0~+0,F:+0~+0", value_dict)
                # 显示属性变化
                # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            
            # 跳转到下一个场景
            jump a_leave_home

        "度过一个精心规划的大学生涯":
            python:
                # 更新剧情历史
                plot_history.extend(["旁白：我发誓我要度过一个精心规划的大学生涯"])
                # 调用AI更新属性
                li = value_ai_with_loading_screen(new_plot, "E:+0~+0,A:+1~+5,B:+0~+0,M:-5~-10,S:+0~+0,F:+0~+0", value_dict)
                # 显示属性变化
                # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
             
            # 跳转到下一个场景
            jump a_leave_home







