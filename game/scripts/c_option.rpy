label c_option:
    scene bg classroom
    with fade
    
    python:
        scen_desc = """
        时间：大三下学期
        地点：教室
        人物：我
        场景描述：随着大三即将结束，未来的道路选择摆在了眼前。班上的同学们都在为自己的未来做着不同的规划：有人准备考研，有人投简历找工作，有人准备公务员考试...面对着多种可能性，我需要认真思考该如何规划自己的未来。
        **注意生成的独白要体现主角在各个选项之间的思考和权衡,但是不要直接做出选择**
        """
        
        new_plot = text_ai_with_loading_screen(scen_desc, plot_history, value_dict)

        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        
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
        
    menu:
        "考研深造":
            python:
                plot_history.extend(["旁白：我决定考研继续深造"])
            jump c_grau_exam_target
            
        "考公务员":
            python:
                plot_history.extend(["旁白：我选择了考公务员"])
            jump c_civil_exam
            
        "享受当下生活":
            python:
                plot_history.extend(["旁白：我决定先好好享受生活"])
            jump c_nothing
            
        "自我提升":
            python:
                plot_history.extend(["旁白：我选择投入时间提升自己"])
            jump c_develop
            
        "参加竞赛":
            python:
                plot_history.extend(["旁白：我决定通过竞赛提升实力"])
            jump c_competition
            
        "实习积累经验":
            python:
                plot_history.extend(["旁白：我选择去实习积累经验"])
            jump c_trainee
            
        "创业":
            python:
                plot_history.extend(["旁白：我决定尝试创业"])
            jump c_start_business
            
        "参与课题研究":
            python:
                plot_history.extend(["旁白：我选择参与课题研究"])
            jump c_first_research