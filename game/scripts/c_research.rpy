label c_first_research:
    scene bg lab_room
    with fade

    python:
        scen_desc = """
        时间：参与实验室的老师课题研究
        地点：实验室
        场景描述：根据当前的属性值自行生成
        1.E值和A值越高我的表现应该越好，
        2.S值越高我的Leader对我的评价应该越高。
        3.剧情应该包括是否表现良好、是否参与发表论文、是否留在实验室
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