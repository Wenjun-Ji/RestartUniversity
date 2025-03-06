label c_grau_exam_target:
    scene bg school
    with fade

    python:
        scen_desc = """
        时间：大三下学期为考研做准备以及大四实施考研计划
        地点：学校
        场景描述：根据当前的属性值自行生成，可以参考下述描述：
        第一部分：做准备
        1、A值越高目标越明确
        2、当不明确时S值越高求助老师和学长学姐越容易成功
        第二部分：学习
        1、E值越高学习效率越高
        2、A值越高计划完成度越高
        3、当计划完成度不高时，若B值或者E值过低就放弃考研
        第三部分：备考
        1.当A值过低时感受到考研的巨大压力
        2.当感受到巨大压力时若M值或者E值较低则放弃考研
        第四部分：考试
        1.A值越高考研结果越好
        2.当考研结果较好时，若F值较高则出国读研
        3.当考研结果较好时，若F值一般则国内读研
        4.当考研结果不好时，根据当前属性值选择就业、接受调剂读研或者重新考研
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
