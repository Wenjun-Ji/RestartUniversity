# 大学场景
label a_dailylife:
    stop music fadeout 1.0
    play music "audio/轻松欢快.mp3" fadein 1.0 volume 0.5 loop
    scene bg university
    with fade
    
    python:
        scen_desc_1 = """
        时间：大学开学后
        地点：校园里
        人物：我
        场景描述：校园里熙熙攘攘，新生们逐渐适应了大学生活的节奏。图书馆的自习室里坐满了埋头苦干的学生。操场上，运动的身影在阳光下挥洒着汗水。校园的每个角落都充满了青春的活力和对知识的渴望。
        """
        
        # 调用AI生成新的大学场景剧情
        new_plot = text_ai_with_loading_screen(scen_desc_1, plot_history, value_dict)

        # 更新剧情历史
        plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
        
        # 显示生成的剧情
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

    jump a_PEclass