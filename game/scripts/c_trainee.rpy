label c_trainee:
    scene bg company
    with fade
    python:
        scen_desc = """
        时间：大四
        地点：公司
        场景描述：根据当前的属性值自行生成，可以参考下述描述：
        第一部分：入职
        1、E值和S值越高入职越容易
        2、S值越高入职后越容易获得领导赏识
        3、当S值较低的时候入职可能失败，不再生成别的剧情
        第二部分：开始工作
        根据E值高低决定工作表现，E值越高工作表现越好
        第三部分：遇到困难
        1、当遇到困难时，若S值较高则通过求助前辈解决
        2、当遇到困难时，若A值较低则通过自行思考解决
        3、若M值或者E值过低则困难不能被解决，收到上司批评
        第四部分：转正
        根据之前的工作表现决定是否能转正
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
