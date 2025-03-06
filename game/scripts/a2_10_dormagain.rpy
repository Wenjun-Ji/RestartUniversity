label a_dormagain:
    scene bg dormitory
    with fade
    python:
        scen_desc_1 = """
        时间：大一期间  
        地点：宿舍
        人物：我，室友 
        场景描述：结束了一天的忙碌，我拖着沉重的步伐回到了宿舍。房间内昏黄的灯光温暖而宁静，空气中弥漫着室友们留下的温馨气息。我轻手轻脚地放下书包，换上柔软的拖鞋，坐在床边，深吸一口气，感受着从紧张状态中逐渐放松的身心。
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

    $ res = select_ai_with_loading_screen("我回到了宿舍", value_dict, plot_history, ["dorm_party", "dorm_quarrel","dorm_clean"])
    if res == "dorm_party":
        $ plot_history.extend([f"室友邀请我参加宿舍聚会"])
        jump a_dorm_party
    if res == "dorm_quarrel":
        $ plot_history.extend([f"我在宿舍内和室友发生了争吵"])
        jump a_dorm_quarrel
    if res == "dorm_clean":
        $ plot_history.extend([f"宿管来检查宿舍卫生"])
        jump a_dorm_clean

label a_dorm_party:
    scene bg dormitory
    with fade
    python:
        scen_desc_1 = """
        时间：晚上11点
        地点：宿舍
        人物：我，室友
        场景描述：室友们正在准备一场深夜聚会，桌上摆满了零食和饮料。有人已经打开了游戏机，有人在整理电影清单。欢快的气氛在房间里流淌，但我看了看明天的课程表，又瞄了眼手机显示的时间。室友热情地向我招手："来吧，难得大家都有空！"
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
                elif key == "室友":
                    renpy.show("roommate", at_list=[player_right])
                    renpy.say(roommate, value)
                    renpy.hide("roommate")
                else:
                    continue

    # 玩家互动选项
    menu:
        "参加聚会":
            $ plot_history.extend(["旁白：我选择参加聚会"])
            jump a_party_join
        
        "拒绝参加选择早睡":
            $ plot_history.extend(["旁白：我选择拒绝参加选择早睡"])
            jump a_party_sleep

        "参加但控制时间":
            $ plot_history.extend(["旁白：我选择参加但控制时间"])
            jump a_party_moderate

label a_party_join:
    scene bg dormitory
    with fade
    python:
        scen_desc_1 = """
        时间：凌晨1点
        地点：宿舍
        人物：我，室友
        场景描述：聚会进行到深夜，室友们的笑声和音乐声在宿舍里回荡。我和室友们玩得不亦乐乎，分享着彼此的趣事和心情。时间一分一秒过去，我感到这是一次珍贵的经历，也是一次难忘的夜晚。
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
                elif key == "室友":
                    renpy.show("roommate", at_list=[player_right])
                    renpy.say(roommate, value)
                    renpy.hide("roommate")
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:-5~-10,A:-5~-10,B:-5~-10,M:+5~+10,S:+5~+10,F:-5~-3", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
    
    jump a_finalexam

label a_party_sleep:
    scene bg dormitory
    with fade
    python:
        scen_desc_1 = """
        时间：凌晨1点
        地点：宿舍
        人物：我，室友
        场景描述：我婉拒了室友的邀请，解释说明天课程比较重要。虽然隔壁传来欢声笑语，但我戴上耳机，按照平常的时间早早休息了。也许错过了一些快乐，但至少为明天的课程保持了充沛的精力。
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
                elif key == "室友":
                    renpy.show("roommate", at_list=[player_right])
                    renpy.say(roommate, value)
                    renpy.hide("roommate")
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:+3~+8,A:+5~+10,B:+5~+10,M:-5~-3,S:-10~-5,F:0~0", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
    
    jump a_finalexam

label a_party_moderate:
    scene bg dormitory
    with fade
    python:
        scen_desc_1 = """
        时间：凌晨1点
        地点：宿舍
        人物：我，室友
        场景描述：我适度参与了聚会，和室友们聊得开心，玩得愉快。但在一定时间后，我提出了离开的请求，回到自己的床上，享受着宁静的夜晚。虽然没有参与到最后，但这段时间的快乐和放松让我感到满足。
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
                elif key == "室友":
                    renpy.show("roommate", at_list=[player_right])
                    renpy.say(roommate, value)
                    renpy.hide("roommate")
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:-5~-3,A:0~0,B:-3~-1,M:+5~+10,S:+10~+15,F:-3~-1", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_finalexam

label a_dorm_quarrel:
    stop music fadeout 1.0
    play music "audio/quarrel.mp3" fadein 1.0 volume 0.5 loop
    scene bg dormitory
    with fade
    python:
        scen_desc_1 = """
        时间：晚上
        地点：宿舍
        人物：我，室友，其他室友
        场景描述：因为空调温度设置、打游戏的声音等生活琐事，宿舍里的矛盾逐渐积累。今天终于爆发了争吵，气氛很是紧张。其他室友有的在劝架，有的默默看着。房间里充满了令人不适的沉默，每个人都心事重重。桌上的台灯在暖黄色的光晕中照出了大家紧绷的表情。
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
                elif key == "室友":
                    renpy.show("roommate", at_list=[player_right])
                    renpy.say(roommate, value)
                    renpy.hide("roommate")
                elif key == "其他室友":
                    renpy.show("rs", at_list=[player_right])
                    renpy.say(rs, value)
                    renpy.hide("rs")
                else:
                    continue

    # 玩家互动选项
    menu:
        "主动沟通解决":
            $ plot_history.extend(["旁白：我选择主动沟通解决"])
            jump a_quarrel_communicate
        
        "忍气吞声":
            $ plot_history.extend(["旁白：我选择忍气吞声"])
            jump a_quarrel_endure

        "向辅导员投诉":
            $ plot_history.extend(["旁白：我选择向辅导员投诉"])
            jump a_quarrel_report

label a_quarrel_communicate:
    scene bg dormitory
    with fade
    python:
        scen_desc_1 = """
        时间：晚上
        地点：宿舍
        人物：我，室友
        场景描述：我主动找室友沟通，表达自己的想法和感受。经过一番交流，我们找到了共同的解决方案，互相理解了对方的立场。气氛逐渐缓和，宿舍里的紧张气氛也得到了缓解。
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
                elif key == "室友":
                    renpy.show("roommate", at_list=[player_right])
                    renpy.say(roommate, value)
                    renpy.hide("roommate")
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:-10~-5,A:0~0,B:0~0,M:+5~+10,S:+5~+10,F:0~0", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_finalexam

label a_quarrel_endure:
    scene bg dormitory
    with fade
    python:
        scen_desc_1 = """
        时间：晚上
        地点：宿舍
        人物：我，室友
        场景描述：我选择了忍气吞声，没有和室友继续争吵。虽然心里有些委屈，但为了维护宿舍的和谐氛围，我选择了忍让。室友也渐渐冷静下来，宿舍里的气氛逐渐缓和。
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
                elif key == "室友":
                    renpy.show("roommate", at_list=[player_right])
                    renpy.say(roommate, value)
                    renpy.hide("roommate")
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:-5~-3,A:-5~-3,B:-5~-3,M:-5~-10,S:-5~-10,F:0~0", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_finalexam

label a_quarrel_report:
    scene bg dormitory
    with fade
    python:
        scen_desc_1 = """
        时间：晚上
        地点：宿舍
        人物：我，室友，辅导员
        场景描述：我选择向辅导员投诉室友的行为，希望能够得到解决。辅导员听取了我的诉求，表示会尽快处理。室友也被辅导员找去谈话，宿舍里的气氛变得紧张起来。
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
                elif key == "室友":
                    renpy.show("roommate", at_list=[player_right])
                    renpy.say(roommate, value)
                    renpy.hide("roommate")
                elif key == "辅导员":
                    renpy.show("guider", at_list=[player_right])
                    renpy.say(guider, value)
                    renpy.hide("guider")
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:-5~-10,A:0~0,B:-5~-3,M:-10~-5,S:-5~-10,F:0~0", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_finalexam

label a_dorm_clean:
    scene bg dormitory
    with fade
    python:
        scen_desc_1 = """
        时间：周五下午
        地点：宿舍
        人物：我，室友们，宿管阿姨
        场景描述：宿管阿姨通知今天下午要进行例行卫生检查。宿舍里确实有些凌乱：桌上堆着外卖盒，床上散落着衣服，地上有些纸屑，垃圾桶也快满了。室友们有的在打游戏，有的准备出门。窗外阳光正好，显得房间里的灰尘格外明显。
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
                elif key == "室友们":
                    renpy.show("roommates", at_list=[player_right])
                    renpy.say(roommates, value)
                    renpy.hide("roommates")
                elif key == "宿管阿姨":
                    renpy.show("aunt", at_list=[player_right])
                    renpy.say(aunt, value)
                    renpy.hide("aunt")
                else:
                    continue

    # 玩家互动选项
    menu:
        "积极打扫":
            $ plot_history.extend(["旁白：我选择积极打扫宿舍"])
            jump a_clean_thoroughly
        
        "临时应付，草草收拾":
            $ plot_history.extend(["旁白：我选择草草收拾宿舍"])
            jump a_clean_barely

        "完全不理会":
            $ plot_history.extend(["旁白：我选择不理会宿管阿姨的提醒"])
            jump a_clean_ignore

label a_clean_thoroughly:
    scene bg dormitory
    with fade
    python:
        scen_desc_1 = """
        时间：周五下午
        地点：宿舍
        人物：我，室友们，宿管阿姨
        场景描述：我和室友们一起动手，认真打扫了宿舍。大家分工合作，清理了地面、桌面、床铺等各个角落。宿管阿姨看到宿舍焕然一新，满意地点点头，表扬了我们的努力。
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
                elif key == "室友们":
                    renpy.show("roommates", at_list=[player_right])
                    renpy.say(roommates, value)
                    renpy.hide("roommates")
                elif key == "宿管阿姨":
                    renpy.say(aunt, value)
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:-1~-5,A:0~0,B:+1~+5,M:+1~+5,S:+5~+10,F:-3~-1", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_finalexam

label a_clean_barely:
    scene bg dormitory
    with fade
    python:
        scen_desc_1 = """
        时间：周五下午
        地点：宿舍
        人物：我，室友们，宿管阿姨
        场景描述：我随便收拾了一下明显的垃圾，把衣服胡乱塞进衣柜，将桌上的杂物推到一边。虽然表面上看起来整洁了一些，但抽屉和柜子里仍是一团糟。检查时，宿管阿姨皱着眉头记录了几项问题，但也没说什么。
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
                elif key == "室友们":
                    renpy.show("roommates", at_list=[player_right])
                    renpy.say(roommates, value)
                    renpy.hide("roommates")
                elif key == "宿管阿姨":
                    renpy.say(aunt, value)
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:-5~-3,A:0~0,B:-5~-3,M:-5~-3,S:-3~-1,F:0~0", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_finalexam

label a_clean_ignore:
    scene bg dormitory
    with fade
    python:
        scen_desc_1 = """
        时间：周五下午
        地点：宿舍
        人物：我，室友，宿管阿姨
        场景描述：我继续玩手机，对即将到来的检查置之不理。检查时，宿管阿姨看到凌乱的环境很是生气，严厉批评了我们，并要求限期整改，否则将通报辅导员。室友们也对我的态度有些不满。
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
                elif key == "室友":
                    renpy.show("roommate", at_list=[player_right])
                    renpy.say(roommate, value)
                    renpy.hide("roommate")
                elif key == "宿管阿姨":
                    renpy.say(aunt, value)
                else:
                    continue

        li = value_ai_with_loading_screen(new_plot, "E:0~0,A:0~0,B:-5~-10,M:-10~-5,S:-1~-5,F:0~0", value_dict)
        
        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump a_finalexam

