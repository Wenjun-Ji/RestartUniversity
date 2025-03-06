# 精力值低事件
label b_event_low_energy:
    scene bg medical_office
    with fade
    
    python:
        scen_desc = """
        时间：某天早晨
        地点：学校医务室
        人物：我，医生
        场景描述：我由于长期熬夜、缺乏休息，身心极度疲惫。一天早上，头痛欲裂，身体虚弱无力，不得不前往学校医务室。在医生的建议下，必须暂停所有活动，进行强制休息。现在我在犹豫是接受休息还是选择继续保持现在的作息。
        **注意生成的对话要求不能表明主角已经确定的选择，而是在选项之间再犹豫不决**
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
                elif key == "医生":
                    renpy.show("doctor", at_list=[player_right])
                    renpy.say(doctor, value)
                    renpy.hide("doctor")
                else:
                    continue
        
        

    menu:
        "接受休息，暂时放下学业和社交":
            python:
                plot_history.extend(["旁白：我选择了接受休息"])
                li = value_ai_with_loading_screen(new_plot, "E:+10~+15,A:-10~-5,B:+10~+15,M:+5~+10,S:-10~-5,F:0~0", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_low_energy_rest
            
        "继续保持作息，拒绝医生建议":
            python:
                plot_history.extend(["旁白：我选择了继续保持作息,拒绝医生建议"])
                li = value_ai_with_loading_screen(new_plot, "E:-10~-15,A:-15~-10,B:-15~-20,M:-15~-10,S:-5~-3,F:0~0", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_low_energy_study

# 社交关系值低事件
label b_event_low_social:
    scene bg dormitory
    with fade
    
    python:
        scen_desc = """
        时间：某个周末
        地点：宿舍
        人物：我
        场景描述：我过去一段时间里，专注于学业，渐渐与朋友失去联系。我开始感到孤独，意识到已经很久没有和任何人聊天或参加社交活动。孤独感与日俱增。现在我在犹豫要不要重新联系之前打朋友们。
        **注意生成的对话要求不能表明主角已经确定的选择，而是在选项之间再犹豫不决**
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
                else:
                    continue
        
        

    menu:
        "主动联系朋友，重建关系":
            python:
                plot_history.extend(["旁白：我选择了主动联系朋友"])
                li = value_ai_with_loading_screen(new_plot, "E:-5~-3,A:-5~-3,B:0~0,M:+10~+15,S:+10~+15,F:-5~-3", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_low_social_contact
            
        "继续专注个人事务，忽略孤独感":
            python:
                plot_history.extend(["旁白：我选择了忽略孤独感，继续专注个人事务"])
                li = value_ai_with_loading_screen(new_plot, "E:0~0,A:+10~+20,B:-5~-3,M:-15~-10,S:-10~-15,F:0~0", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_low_social_ignore

# 学习进度低事件
label b_event_low_study:
    scene bg classroom
    with fade
    
    python:
        scen_desc = """
        时间：学期中期
        地点：教室
        人物：我
        场景描述：我最近时间的课程表现不佳，几次作业中都有明显错误。面临巨大的学业压力，不知如何应对接下来的期末考试。我在犹豫是请求同学帮助，自己复习，还是放弃复习。
        **注意生成的对话要求不能表明主角已经确定的选择，而是在选项之间再犹豫不决**
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
                else:
                    continue
        

    menu:
        "请求同学帮助，进行补习":
            python:
                plot_history.extend(["旁白：我选择寻求同学帮助进行补习"])
                li = value_ai_with_loading_screen(new_plot, "E:-10~-5,A:+15~+20,B:0~0,M:+10~+20,S:+10~+20,F:-5~-3", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_low_study_help
            
        "独自面对困难，试图自我解决":
            python:
                plot_history.extend(["旁白：我选择独自面对困难，试图自己复习"])
                li = value_ai_with_loading_screen(new_plot, "E:-20~-10,A:+10~+20,B:-5~-3,M:-20~-10,S:-5~-3,F:0~0", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_low_study_self
            
        "放任不管，选择躺平":
            $ plot_history.extend(["旁白：我选择放任不管，选择躺平"])
            python:
                li = value_ai_with_loading_screen(new_plot, "E:+10~+20,A:-15~-20,B:0~0,M:-15~-20,S:-10~-5,F:0~0", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_low_study_give_up

# 心理健康低事件
label b_event_low_mental:
    scene bg dormitory
    with fade
    
    python:
        scen_desc = """
        时间：某个深夜
        地点：宿舍
        人物：我
        场景描述：我开始频繁感到焦虑和自我怀疑，觉得自己不够优秀、与同学相比落后。试图开始新任务时总是缺乏动力，负面情绪积累，无法集中注意力做简单的事情。我在想要不要寻找心理咨询，或是找朋友倾诉。
        **注意生成的对话要求不能表明主角已经确定的选择，而是在选项之间再犹豫不决**
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
                else:
                    continue
        

    menu:
        "寻求心理咨询，缓解压力":
            python:
                plot_history.extend(["旁白：我选择寻求心理咨询"])
                li = value_ai_with_loading_screen(new_plot, "E:-5~-3,A:0~0,B:+10~+20,M:+20~+25,S:+5~+10,F:-20~-10", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_low_mental_counsel
            
        "忽视情绪，继续前进":
            python:
                plot_history.extend(["旁白：我选择忽视情绪"])
                li = value_ai_with_loading_screen(new_plot, "E:-20~-10,A:-10~-5,B:-15~-10,M:-15~-20,S:-10~-5,F:0~0", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_low_mental_ignore
            
        "与朋友倾诉，寻求支持":
            python:
                plot_history.extend(["旁白：我选择与朋友倾诉"])
                li = value_ai_with_loading_screen(new_plot, "E:0~0,A:-5~-3,B:+5~+10,M:+10~+15,S:+10~+15,F:0~0", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_low_mental_friends

# 财务状况低事件
label b_event_low_finance:
    scene bg dormitory
    with fade
    
    python:
        scen_desc = """
        时间：学期中期
        地点：宿舍
        人物：我
        场景描述：我由于过度支，财务状况陷入困境，无法支付下一学期的学费或生活费。由于不想麻烦父母，我面临着是找兼职工作，还是向朋友或银行借款的选择。
        **注意生成的对话要求不能表明主角已经确定的选择，而是在选项之间再犹豫不决**
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
                else:
                    continue
        

    menu:
        "寻找兼职工作，自己解决问题":

            python:
                plot_history.extend(["旁白：我选择找兼职工作"])
                li = value_ai_with_loading_screen(new_plot, "E:-20~-10,A:-10~-5,B:-5~-3,M:+10~+20,S:-5~-3,F:+30~+50", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_low_finance_work
            
        "向家人或朋友借钱":
            python:
                plot_history.extend(["旁白：我选择借钱"])
                li = value_ai_with_loading_screen(new_plot, "E:0~0,A:0~0,B:0~0,M:-10~-5,S:-20~-10,F:+20~+30", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_low_finance_borrow
            
        "申请学生贷款":
            python:
                plot_history.extend(["旁白：我选择申请学生贷款"])
                li = value_ai_with_loading_screen(new_plot, "E:0~0,A:0~0,B:0~0,M:-20~-10,S:0~0,F:+10~+20", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_low_finance_loan

# 社交关系值过高事件
label event_high_social:
    scene bg student_center
    with fade
    
    python:
        scen_desc = """
        时间：某个周末
        地点：学生活动中心
        人物：我
        场景描述：我成为社交圈中活跃角色，频繁参加各种活动、派对和社团工作。越来越多的社交压力让我感到疲惫和内卷焦虑。意识到为了迎合别人的期望，逐渐失去了自我。我不知道自己还要不要维持这种状态。
        **注意生成的对话要求不能表明主角已经确定的选择，而是在选项之间再犹豫不决**
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
                else:
                    continue

    menu:
        "减少社交活动，给自己留些时间":
            $ plot_history.extend(["旁白：我选择减少社交活动，给自己留些时间"])
            python:
                li = value_ai_with_loading_screen(new_plot, "E:+10~+15,A:+10~+20,B:+10~+20,M:+20~+30,S:-20~-10,F:+5~+10", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_high_social_reduce
            
        "继续维持高社交频率，忽略疲惫感":
            $ plot_history.extend(["旁白：我选择继续维持高社交频率，忽略疲惫感"])
            python:
                li = value_ai_with_loading_screen(new_plot, "E:-15~-10,A:-20~-10,B:-20~-10,M:-30~-20,S:+10~+20,F:-10~-5", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_high_social_continue



# 身体健康状况低事件
label b_event_low_health:
    scene bg medical_office
    with fade
    
    python:
        scen_desc = """
        时间：某天下午
        地点：学校医务室
        人物：我，医生
        场景描述：我最近饮食不规律，缺乏运动，身体状况持续恶化。这天下午，突然感到一阵晕眩，被同学送到医务室。医生检查后发现我的身体各项指标都很差，需要及时调整生活方式。我在犹豫要不要听取建议。
        **注意生成的对话要求不能表明主角已经确定的选择，而是在选项之间再犹豫不决**
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
                elif key == "医生":
                    renpy.show("doctor", at_list=[player_right])
                    renpy.say(doctor, value)
                    renpy.hide("doctor")
                else:
                    continue
                    
    menu:
        "听从医生建议，认真调整作息和饮食":
            python:
                plot_history.extend(["旁白：我选择听从医生建议，认真调整作息和饮食"])
                li = value_ai_with_loading_screen(new_plot, "E:-10~-5,A:-5~-3,B:+30~+50,M:+10~+20,S:-5~-3,F:-10~-5", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_low_health_adjust
            
        "觉得小题大做，并没有接受医生的建议":
            python:
                plot_history.extend(["旁白：我觉得小题大做，并没有接受医生的建议"])
                li = value_ai_with_loading_screen(new_plot, "E:-5~-3,A:0~0,B:-20~-10,M:-10~-5,S:0~0,F:-5~-3", value_dict)
                #renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            jump event_low_health_ignore
