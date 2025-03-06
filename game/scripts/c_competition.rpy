label c_competition:
    scene bg competition_scene
    with fade

    python:
        scen_desc = """
        时间：大四
        地点：比赛地点
        场景描述：根据当前的属性值自行生成，可以参考下述描述：
        1.首先，根据值的相对高低决定比赛类型——若A值最高则比赛类型为技术型比赛，若F值和M值最高则比赛类型为商业型比赛，若S值最高则比赛类型为文艺型比赛，若S值最高则比赛类型为体育型比赛，若E值最高则为综合类比赛
        2.其次根据S值决定能否找到志同道合的好队友
        3.根据E值决定对比赛的投入程度，E值越高越容易获得好成绩
        4.根据比赛对应的值类型决定比赛结果，值越高越容易获得好成绩
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
                    continue

    jump end
