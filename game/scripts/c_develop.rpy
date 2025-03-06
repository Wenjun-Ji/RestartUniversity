label c_develop:
    scene bg nowhere
    with fade

    python:
        scen_desc = """
        时间：大四
        场景描述：根据当前的属性值自行生成，可以参考下述描述：
        若A值最高则去发展自身职业技能，例如学习编程、学习英语、学习数据分析等
        若M值或者E值或者B值最高则去发展自身兴趣爱好，例如学习乐器、学习绘画、学习写作等
        若S值或者F值最高则去发展综合素质，例如参加社团活动、参加志愿活动等
        """
        new_plot = summary_ai_with_loading_screen(scen_desc, plot_history, value_dict)

        # 更新剧情历史
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])

        # 显示生成的剧情
        for d in new_plot:
            for key, value in d.items():
                if key == "概述":
                    renpy.say(None, value)  # 显示旁白
                else:
                    continue  # 如果没有匹配的角色，继续循环
    
    jump end