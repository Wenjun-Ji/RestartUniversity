label c_start_business:
    scene bg company
    with fade

    python:
        scen_desc = """
        时间：大四
        地点：公司
        场景描述：根据当前的属性值自行生成，可以参考下述描述：
        1.首先，若F值较高则创业方向为服务型企业，若A值较高则创业方向为技术型企业
        2.其次，若A值或者S值较高则找到志同道合的伙伴一起创业，不然则独自创业
        3.然后，若A值较高则能通过参加创业比赛获得奖金作为启动资金；S值较高则能找到天使投资人投资；F值特别高则能自行垫付启动资金，否则启动资金有限
        4.再然后根据A值和S值高低决定市场反应，A值和S值越高市场反应越好
        5.若创业遭遇了困难根据E值、A值和S值高低决定解决方式，E值、A值和S值越高越容易解决
        6.最后，根据创业方向、启动资金、市场反应和解决方式决定创业结果，创业结果越好则创业越成功
        7.创业的要求应该较高，不能太简单
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
