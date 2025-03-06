label a_stuactivity:
    scene bg activity_center
    with fade
    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：学生活动中心
        人物：我，同学 
        场景描述：学生活动中心里人来人往，各种社团活动的宣传音乐此起彼伏。我站在大厅中央，望着墙上琳琅满目的社团海报：舞蹈教室里传来动感的音乐，画室里飘出淡淡的颜料味道，棋牌室里隐约有同学们的谈笑声。阳光透过玻璃穹顶洒进来，给这个充满青春活力的空间镀上一层温暖的光。
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

    $ res = select_ai_with_loading_screen("我来到学生活动中心", value_dict, plot_history, ["club_meeting", "hold_activities","conflict"])
    if res == "club_meeting":
        $ plot_history.extend([f"我参加社团例会"])
        jump a_clubmeeting
    if res == "hold_activities":
        $ plot_history.extend([f"我参加社团活动"])
        jump a_hold_activities
    if res == "conflict":
        $ plot_history.extend([f"我的课程和社团活动冲突"])
        jump a_conflict

label a_clubmeeting:
    scene bg activity_center
    with fade

    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：学生活动中心
        人物：我，同学，社团负责人
        场景描述：科技社例会在五楼的创客实验室里进行。阳光透过满是零件示意图的玻璃窗洒进来，照亮了桌上散落的电路板和工具。社团负责人正站在电子白板前讲着什么，四周的社员们有的敲着笔记本电脑，有的低头研究着手中的元器件。空气中飘着淡淡的松香味，我坐在后排，期待着等会要宣布的新项目。
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
                elif key == "社团负责人":
                    renpy.say(u,value)
                else:
                    continue

    # 玩家互动选项
    menu:
        "我选择积极参与讨论":
            $ plot_history.extend([f"旁白：我选择积极参与讨论"])
            jump a_joindiscussion
        
        "我选择安静聆听":
            $ plot_history.extend([f"旁白：我选择安静聆听"])
            jump a_justlisten

label a_joindiscussion:
    scene bg classroom
    with fade
    python:
        # 第一幕情节描述
        scen_desc_1 = """
        时间：大学开学后
        地点：教室
        人物：我，同学，社团负责人
        场景描述：我举起手，对社团负责人提出的机器人竞赛方案分享自己的想法："我觉得可以在底盘结构上做些改进。"白板前的社长停下笔，其他社员也转过头来听我说话。我打开笔记本电脑，调出前两天研究的设计图，指着屏幕上的几个细节侃侃而谈。会议室里渐渐响起了热烈的讨论声，大家七嘴八舌地出主意，气氛比刚才活跃了许多。
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
                elif key == "同学":
                    renpy.show("classmate", at_list=[player_right])
                    renpy.say(classmate, value)
                    renpy.hide("classmate")
                else:
                    continue
        
        # 更新剧情历史
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])

        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:-1~-5,A:+3~+5,B:+0~+0,M:+5~+10,S:+5~+10,F:0~0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    # 跳转到大学场景
    jump a_takeclass

label a_justlisten:
    scene bg classroom
    with fade
    python:
        # 第一幕情节描述
        scen_desc_1 = """
        时间：大学开学后
        地点：教室
        人物：我，同学，社团负责人
        场景描述：我坐在创客实验室的角落，静静地听着社团负责人介绍本次机器人竞赛的技术要点。电子白板上的框图越画越多，耳边是其他社员热烈的讨论声。我低头快速记着笔记，时不时点点头表示理解。虽然没有发言，但每个新想法都让我暗暗思考，在笔记本上画着自己的构思草图。
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
                elif key == "同学":
                    renpy.show("classmate", at_list=[player_right])
                    renpy.say(classmate, value)
                    renpy.hide("classmate")
                else:
                    continue

        # 更新剧情历史
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])

        # 调用AI更新属性
        li = value_ai_with_loading_screen(new_plot, "E:-3~0,A:+0~+0,B:+0~+0,M:-1~-5,S:0~-3,F:0~0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    # 跳转到大学场景
    jump a_takeclass

label a_hold_activities:
    scene bg activity_center
    with fade

    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：学生活动中心
        人物：我，同学
        场景描述：阳光穿过大厅玻璃，照在活动中心一层的公告栏上。一张新贴上的彩色海报格外醒目："校园文艺晚会筹备组招募中！"海报上详细列出了需要的岗位：舞台总监、场务组长、设备组、宣传组、节目统筹等。旁边写着"加入我们，让你的创意绽放舞台"的标语，底部是负责人的联系方式和报名二维码。几个学生正驻足观看，小声讨论着自己适合什么职位。
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

    # 玩家互动选项
    menu:
        "我选择担任舞台总监":
            $ plot_history.extend([f"我选择担任舞台总监"])
            jump a_beorganizer
        
        "我选择作为晚会观众":
            $ plot_history.extend([f"我选择作为晚会观众"])
            jump a_beaudience

label a_beorganizer:
    scene bg auditorium
    with fade
    python:
        # 第一幕情节描述
        scen_desc_1 = """
        时间：文艺晚会筹备期间
        地点：学校礼堂
        人物：我，演员们，技术人员
        场景描述：我担任了校园文艺晚会的舞台总监一职。这是一个充满挑战的角色，需要协调演员、灯光、音响等多个团队，确保晚会顺利进行。虽然压力很大，但这也是一个展示领导才能和提升组织能力的好机会。
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
                elif key == "演员们":
                    renpy.show("actor", at_list=[player_right])
                    renpy.say(actor, value)
                    renpy.hide("actor")
                elif key == "技术人员":
                    renpy.show("technician", at_list=[player_right])
                    renpy.say(technician, value)
                    renpy.hide("technician")
                else:
                    continue

        # 更新剧情历史
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])

        # 调用AI更新属性
        # E精力值降低较多（工作强度大）
        # A学业略有影响
        # B身体状况略有下降
        # M心理压力增加但也有成就感
        # S社交能力显著提升
        # F财务状况不变
        li = value_ai_with_loading_screen(new_plot, "E:-5~-10,A:-5~-3,B:-2~-5,M:+1~+5,S:+5~+10,F:0~0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    # 跳转到日常生活场景
    jump a_takeclass

label a_beaudience:
    scene bg auditorium
    with fade
    
    python:
        # 第一幕情节描述
        scen_desc_1 = """
        时间：文艺晚会当晚
        地点：学校礼堂观众席
        人物：我，周围的观众，演员
        场景描述：我作为观众参加了学校文艺晚会。在轻松愉快的氛围中欣赏同学们的精彩表演，感受校园文化的魅力。演出节目丰富多彩，有歌曲、舞蹈、话剧等，让我度过了一个愉快的夜晚。
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
                elif key == "观众":
                    renpy.say(audience, value)
                elif key == "演员们":
                    renpy.show("actor", at_list=[player_right])
                    renpy.say(actor, value)
                    renpy.hide("actor")
                else:
                    continue

        # 更新剧情历史
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])

        # 调用AI更新属性
        # E精力值略有消耗（晚上时间）
        # A学业不变
        # B身体状况不变
        # M心理状态略有提升（娱乐放松）
        # S社交状况略有提升（集体活动）
        # F财务状况略降（购票）
        li = value_ai_with_loading_screen(new_plot, "E:-3~-1,A:0~0,B:0~0,M:+3~+5,S:+1~+3,F:-2~-1", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    # 跳转到上课场景
    jump a_takeclass

label a_conflict:
    scene bg classroom
    with fade
    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：教室/社团活动室
        人物：我，同学，社团成员
        场景描述：下午有一节重要的专业课，恰好与科技社的重要项目会议时间冲突。课程内容是期中考试的重点，而社团项目也进入了关键阶段。手机上闪烁着社团群的消息提醒，我握着笔，陷入了选择的困扰。
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
                elif key == "社团负责人":
                    renpy.show("u", at_list=[player_right])
                    renpy.say(u, value)
                    renpy.hide("u")
                else:
                    continue

    # 玩家互动选项
    menu:
        "参加社团活动":
            $ plot_history.extend(["旁白：我选择参加社团活动"])
            jump a_joinclub
        
        "专注课堂学习":
            $ plot_history.extend(["旁白：我选择专注课堂学习"])
            jump a_studyhard
            
        "两个都不去，找个地方放松":
            $ plot_history.extend(["旁白：我选择去娱乐放松"])
            jump a_relax

label a_joinclub:
    scene bg classroom
    with fade
    python:
        # 第一幕情节描述
        scen_desc_1 = """
        时间：学期中
        地点：教室/社团活动室
        人物：我，社团成员，老师
        场景描述：在得知社团重要活动与课程作业截止时间冲突后，我最终选择参加社团活动。虽然这可能影响我的课程成绩，但我认为社团活动带来的经验和人际关系也很重要。这个选择反映了我对个人发展方向的思考和取舍。
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

        # 调用AI更新属性
        # E精力值适度消耗（参加活动）
        # A学业明显下降（错过作业）
        # B身体状况略有提升（活动带来的锻炼）
        # M心理状态有波动（活动快乐但也有压力）
        # S社交状况显著提升
        # F财务状况略降（活动支出）
        li = value_ai_with_loading_screen(new_plot, "E:-8~-5,A:-5~-10,B:+0~+3,M:+1~+5,S:+8~+12,F:-5~-3", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    # 跳转到日常生活场景
    jump a_takeclass

label a_studyhard:
    scene bg library
    with fade
    python:
        # 第一幕情节描述
        scen_desc_1 = """
        时间：学期中
        地点：图书馆/自习室
        人物：我，社团负责人，老师
        场景描述：面对社团活动和课程作业的时间冲突，我最终选择了专注于学习。虽然遗憾错过了社团活动，但我认为当前阶段学业更为重要。我给社团负责人请了假，并全身心投入到作业中。
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
        # E精力值大量消耗（认真学习）
        # A学业显著提升（专注学习）
        # B身体状况略降（久坐学习）
        # M心理状态有波动（压力与成就感）
        # S社交状况下降（错过活动）
        # F财务不变
        li = value_ai_with_loading_screen(new_plot, "E:-5~-8,A:+5~+10,B:-3~-1,M:-3~-1,S:-8~-5,F:0~0", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    # 跳转到上课场景
    jump a_takeclass

label a_relax:
    scene bg dorm
    with fade
    
    python:
        # 第一幕情节描述
        scen_desc_1 = """
        时间：学期中
        地点：宿舍/娱乐场所
        人物：我，社团负责人，老师
        场景描述：面对社团活动和课程作业的时间冲突时，我选择了看综艺放松一下。虽然知道这样可能会影响学习和社团表现，但此时我更想享受轻松的时光。暂时逃避压力的同时，内心也有一丝愧疚。
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
        # E精力值恢复（休息放松）
        # A学业明显下降（耽误学习）
        # B身体状况轻微下降（久坐娱乐）
        # M心理状态起伏（轻松但有负罪感）
        # S社交状况下降（独处娱乐）
        # F财务略降（娱乐消费）
        li = value_ai_with_loading_screen(new_plot, "E:+5~+8,A:-5~-10,B:-2~-1,M:+1~+3,S:-6~-3,F:-5~-3", value_dict)
        
        # 显示属性变化
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    # 跳转到日常生活场景
    jump a_takeclass

    

