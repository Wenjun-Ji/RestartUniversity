label c_civil_exam:
    scene bg school
    with fade

    python:
        scen_desc = """
        时间：大三下学期为考公做准备以及大四实施考公计划
        地点：学校
        场景描述：根据当前的属性值自行生成，可以参考下述描述：
        第一部分：做准备
        1、S值越高目标岗位越明确
        2、当不明确时S值和F值越高查找相关信息越容易成功
        第二部分：执行计划
        1、A值越高执行计划越容易成功
        2、当执行计划失败时，若E值或者B值或者M值或者F值过低则放弃考公
        第三部分：笔试
        1、A值越高笔试成绩越好
        2、当笔试未达标时，若E值或者B值或者M值或者F值过低则放弃考公，不再生成面试部分
        3、当笔试成绩较好时，进入面试部分
        第四部分：面试
        1、S值越高面试成绩越好
        2、当面试未达标时，若E值或者B值或者M值或者F值过低则放弃考公
        3、当面试成绩较好时,被录用准备入职
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


