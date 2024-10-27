### 这是一条恋爱线

label speak_love:
    # 显示场景
    scene bg love  # 这个是江边的日落风景
    # 定义角色
    define p = Character("我")
    define s = Character("她")

    python:
        # 第一幕情节描述
        scen_desc = """
        时间：傍晚
        地点：江边
        人物：我，女主（她）
        场景描述：
        夕阳的余晖洒在江面上，微风轻拂，空气中充满了一种温柔而静谧的气氛。主角和女主走在一起，沉默伴随着他们的步伐。主角内心已经下定决心要向她表白，但依然有些紧张，心中在纠结是否要说出口。
        **此时，主角内心的犹豫和紧张感应在对话中有所体现。主角还未完全表露心迹，但心里已经有了打算。**
        """

        # 调用AI生成新剧情
        new_plot = text_ai.invoke(scen_desc, plot_history, value_dict)

        # 显示生成的剧情
        for d in new_plot:
            for key, value in d.items():
                if key == "旁白":
                    renpy.say(None, value)  # 显示旁白
                elif key == "我":
                    renpy.say(p, value)  # "我" 的对话
                elif key == "她":
                    renpy.say(s, value)  # "她" 的对话

    # 显示选择按钮
    menu:
        "大胆表白":
            python:
                # 更新剧情历史
                plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
                plot_history.extend(["旁白：主角鼓起勇气，深吸一口气，对她表白了心意。心中充满期待与不安。"])  # 强调表白后的情绪变化
                # 调用AI更新属性
                li = value_ai.invoke(new_plot, "E:-10~-15,A:0~0,B:+5~+7,M:+10~+15,S:+10~+15,F:0~0", value_dict)
                # 表白带来的紧张消耗精力（E），心理满足感（M）和社交关系（S）显著提升，身体健康（B）稍微上升
                # 显示属性变化
                renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            pause
            jump love_outcome  # 跳转到表白后的结果场景

        "算了，还是做朋友吧":
            python:
                # 更新剧情历史
                plot_history.extend([f"{key}：{value}" for d in new_plot for key, value in d.items()])
                plot_history.extend(["旁白：主角最终没有鼓起勇气表白，决定维持现在的关系，做普通朋友。"])  # 强调选择的后果
                # 调用AI更新属性
                li = value_ai.invoke(new_plot, "E:+5~+8,A:0~0,B:+3~+5,M:+3~+5,S:+2~+5,F:0~0", value_dict)
                # 放弃表白带来的解脱（E）增加了些许精力，心理满足感（M）和社交关系（S）略微提升，身体健康（B）小幅上升
                # 显示属性变化
                renpy.say(None, "\n".join([f"{key}：{value}" for key, value in li.items()]))
            pause 
            jump sanbu  # 跳转到其他场景（例如散步场景）

