label c_nothing:
    scene bg nowhere
    with fade

    python:
        scen_desc = """
        时间：大三、大四
        场景描述：根据当前的属性值自行生成，可以参考下述描述：
            1.去公园散步、露营、摄影、运动（M低S高）
            2.宿舍游戏、追剧、综艺、躺尸.....（M低S低）
            3.全国各地、五湖四海的旅游，体验祖国大好河山（E高F高）
            4.聚会happying from day to night(S高F较高)
            5.sleeping all the time（E低orB低）
            .......
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