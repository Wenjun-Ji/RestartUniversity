label a_examination:
    scene bg dormitory  # 这个是大学校园背景
    python:
        scen_desc = """
        时间：期末考试结束后  
        地点：宿舍
        人物：我，同学
        场景描述：期末考试成绩终于出来了。教务系统瞬间被挤爆，同学们都在焦急地刷新页面。走廊里不时传来欢呼或叹息声，有人在讨论各科的分数线和平均分。我深吸一口气，点开了成绩查询页面。
        """
        
        # 调用AI生成新的大学场景剧情
        new_plot = text_ai.invoke(scen_desc, plot_history, value_dict)

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

    $ res = select_ai.invoke("我查询期末考试成绩", value_dict, plot_history, ["exam_excellent", "exam_average","exam_poor"])
    if res == "exam_excellent":
        $ plot_history.extend([f"我因为努力学习考出了优异的成绩"])
        jump a_exam_excellent
    if res == "exam_average":
        $ plot_history.extend([f"我考出了一般的成绩"])
        jump a_exam_average
    if res == "exam_poor":
        $ plot_history.extend([f"我的期末考试成绩很差"])
        jump a_exam_poor

# 优异成绩场景
label a_exam_excellent:
    scene bg playground  # 这个是大学校园背景
    python:
        scen_desc = """
        时间：期末考试结束后  
        地点：操场  
        人物：我，同学
        场景描述：我在操场上跑步，心情愉悦。手机里的成绩单显示着优异的成绩，我不禁笑了出来。同学们也在操场上跑步，有的在讨论着成绩，有的在庆祝。我感到满足和自豪，决定继续努力。
        """
        
        # 调用AI生成新的大学场景剧情
        new_plot = text_ai.invoke(scen_desc, plot_history, value_dict)

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

        li = value_ai.invoke(new_plot, "E:+15~+20,A:+20~+25,B:+5~+10,M:+20~+25,S:+10~+15,F:-10~-5", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump b_option

# 一般成绩场景
label a_exam_average:
    scene bg playground  # 这个是大学校园背景
    python:
        scen_desc = """
        时间：期末考试结束后  
        地点：操场  
        人物：我，同学
        场景描述：我在操场上跑步，心情平静。手机里的成绩单显示着一般的成绩，我感到有些失落。同学们也在操场上跑步，有的在讨论着成绩，有的在安慰。我感到有些焦虑，决定更加努力。
        """
        
        # 调用AI生成新的大学场景剧情
        new_plot = text_ai.invoke(scen_desc, plot_history, value_dict)

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

        li = value_ai.invoke(new_plot, "E:+15~+20,A:+20~+25,B:+5~+10,M:+20~+25,S:+10~+15,F:-10~-5", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))

    jump b_option

# 不及格成绩场景
label a_exam_poor:
    scene bg playground  # 这个是大学校园背景
    python:
        scen_desc = """
        时间：期末考试结束后  
        地点：操场  
        人物：我，同学
        场景描述：看到成绩的那一刻，心瞬间沉到了谷底。几门重要的课程都没考好，其中一门甚至需要补考。懊悔、自责、焦虑等各种情绪涌上心头。不敢告诉父母，也不知道该如何面对老师和同学。躺在床上翻来覆去，开始思考是不是该调整学习方法，也许需要寻求老师和学霸同学的帮助。
        """
        
        # 调用AI生成新的大学场景剧情
        new_plot = text_ai.invoke(scen_desc, plot_history, value_dict)

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

        li = value_ai.invoke(new_plot, "E:-15~-10,A:-20~-15,B:-10~-5,M:-20~-15,S:-10~-5,F:-5~-3", value_dict)

        # renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
        
    jump b_option