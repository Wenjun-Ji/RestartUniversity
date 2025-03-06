import requests
import json
from datetime import datetime


def call_api(prompt: str) -> list:
    api_key = "sk-qxU0fiYsCZeBRxGW15A608161e2f40E48eD6B7B11dD695A6"  # 在此处直接内置API密钥
    proxy = ""  # 如果有代理需求，可以在此设置代理URL
    url = "https://api.gpt.ge/v1/chat/completions"
    if proxy:
        url = proxy

    headers = {
        'Authorization': f"Bearer {api_key}",
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1688,
        "temperature": 0.7,
        "stream": False
    })

    # 发送请求并返回结果
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        response_data = response.json()
        # 提取生成的内容
        result = response_data['choices'][0]['message']['content']

        # # 将结果保存到文件
        # with open("api_results.txt", "a", encoding="utf-8") as f:
        #     f.write(f"Timestamp: {datetime.now()}\n")
        #     f.write("Prompt:\n")
        #     f.write(prompt + "\n")
        #     f.write("Result:\n")
        #     f.write(result + "\n")
        #     f.write("="*50 + "\n")  # 分隔符

        return result
    else:
        print(f"API 请求失败，状态码: {response.status_code}")
        return ""


class TextAI:
    def __init__(self):
        self.plot_template = """
        # 场景描述：
        以下是当前剧情的场景描述，请根据场景描述生成剧情片段：
        {scen_desc}

        # 剧情生成规则：
        请严格遵循以下规则，以确保生成的剧情符合预期效果：
        1. 每个剧情片段的长度不超过500字。
        2. 剧情应包含旁白、人物对话和人物内心独白，确保场景切换自然、对话真实。
        3. 旁白需详细描述场景，包括环境、时间、人物动作等，帮助玩家身临其境。
        4. 人物内心独白需反映角色内心的冲突或情感波动，推动剧情发展。
        5. 剧情围绕大学生活中的现实挑战展开，例如学业压力、人际关系、未来迷茫等，展现真实的成长历程。
        6. 剧情受到当前的属性值影响，但一定注意不要在剧情中体现出属性值的影响，而是要通过剧情的发展来体现属性值的变化。

        # 语言风格：
        剧情的语言风格应贴近现代大学生的表达方式，细腻、生动，能够引发玩家的共鸣和思考。描述应具有感染力，尤其是对角色情感和内心世界的刻画。风格可参考青春校园文学作品，着重于心理描写和情感表达。

        # 剧情格式：
        请严格使用以下格式输出剧情，每种内容类型都应单独一行，不要混合，**确保输出的内容不包含任何与剧情内容无关的信息，尤其不要出现属性相关内容**:
        1. 每行剧情内容必须严格以特定符号开头，按照以下格式编写：
            - 旁白格式：`^@旁白：旁白内容`
            - 人物对话格式：`^#人物名字：人物所说的话`
            - 人物内心独白格式：`^$人物名字：（人物内心独白内容）`

        2. 确保每一行的内容准确对应格式符号的类型，旁白行只能用 `^@` 开头，对话行只能用 `^#` 开头，内心独白只能用 `^$` 开头。
        
        3. 避免使用重复的开头符号或不完整的内容，确保剧情紧凑、明确。未遵循格式的输出内容将被视为错误。

        # 剧情历史：
        以下是当前剧情的剧情历史，请根据剧情历史生成剧情片段：
        {plot_history}

        # 属性说明：
        以下为各项属性的具体含义：
        {value_desc}

        # 当前角色属性：
        以下是当前角色属性值，请在生成剧情时参考当前角色属性值：
        {value_dict}

        # 生成要求：
        请根据以上内容生成新的、具有创意的剧情片段，体现角色的成长和变化。
        
        # 示例剧情：
        为了帮助理解格式和风格，以下是一个示例剧情片段：
        {example_plot}
        """

        self.example_plot = """
        ^@旁白：午后的图书馆里，阳光透过落地窗洒在书桌上，营造出一片宁静祥和的氛围。我正专注地翻阅着手中的专业书籍。
        ^$我：（这门课程的内容比想象中要难理解得多，不过我一定要坚持下去。）
        ^#同学：嘿，你也在这里啊？
        ^@旁白：熟悉的声音打断了我的思绪，抬头看到了一位同班同学。
        ^#我：是啊，这门课的期中考试快到了，我想提前做些准备。
        ^$同学：（看到同学这么认真，我都有些惭愧了。）
        ^#同学：其实我也正为这门课发愁呢，要不要一起讨论一下？
        ^@旁白：我露出了欣喜的笑容，往旁边挪了挪，给同学腾出了位置。
        ^#我：好啊，我正好有几个问题想请教你呢。
        ^@旁白：我们开始低声交流起来，偶尔在笔记本上写写画画，互相启发，共同进步。
        ^$我：（有时候和别人一起学习，真的能激发出更多的思路和动力呢。）
        """

        self.value_desc = '''
        E(精力值)：表示角色的体力和精神状态
        A(学业进度)：反映学习成果和知识积累
        B(身体健康状况)：表示整体身体状况
        M(心理健康状况)：反映心理压力和情绪状态
        S(社会关系)：代表人际关系网络的广度和深度
        F(财务状况)：表示经济能力和财务健康
        '''

    def invoke(self, scen_desc: str, plot_history: list, value_dict: dict) -> list:
        # 构建完整的 prompt
        full_prompt = self.plot_template.format(
            scen_desc=scen_desc,
            plot_history="\n".join(plot_history),
            example_plot=self.example_plot,
            value_dict=value_dict,
            value_desc=self.value_desc
        )

        # 调用API生成剧情
        new_plot = call_api(full_prompt)
        new_plot = self.parse_plot(new_plot)
        return new_plot

    def parse_plot(self, plot: str) -> list:
        # 去掉换行符
        plot = plot.replace('\n', '')
        li = plot.split('^')[1:]
        res = []
        for item in li:
            if item[0] == '@' or item[0] == '#' or item[0] == '$':
                res.append({item[1:].split('：')[0]: item.split('：')[1]})
            else:
                print("error")
        return res


class ValueAI:
    def __init__(self):
        self.value_template = """
        # 当前剧情内容：
        以下为当前剧情片段，用于分析该剧情对角色各项属性的影响：
        {current_plot}

        # 属性变化规则：
        请根据以下规则判断剧情对角色属性的影响，并生成符合逻辑的属性变化：
        {value_rules}

        # 属性说明：
        以下为各项属性的具体含义，请参考这些描述，确保生成的属性变化符合角色当前状态及剧情需要：
        {value_desc}

        # 属性变化格式：
        请根据剧情和范围生成属性变化，只需给出最终的属性变化结果，不要输出任何与“角色属性更新”相关的提示。
        返回格式严格为：
        "E": -3, "A": -4, "B": -2, "M": -15, "S": -7, "F": -4

        # 属性变化范围：
        以下为属性值的变化范围，确保变化量在这个范围内：
        {value_change_range}
        
        """

        self.value_rules = """
        1. 属性判断必须符合常理和情节发展；
        2. 所有属性值必须保持为非负整数；
        3. 属性变化值必须为整数；
        4. 考虑事件对各属性的直接和间接影响；
        5. 属性变化应与情节的重要性相匹配。
        """

        self.value_desc = """
        E(精力值)：表示角色的体力和精神状态
        A(学业进度)：反映学习成果和知识积累
        B(身体健康状况)：表示整体身体状况
        M(心理健康状况)：反映心理压力和情绪状态
        S(社会关系)：代表人际关系网络的广度和深度
        F(财务状况)：表示经济能力和财务健康
        """

    def invoke(self, current_plot: list, value_change_ranges: dict, value_dict: dict) -> dict:
        # 构建完整的 prompt
        full_prompt = self.value_template.format(
            current_plot=current_plot,
            value_change_range=value_change_ranges,
            value_rules=self.value_rules,
            value_desc=self.value_desc
        )

        # 调用 API 获取属性变化的结果
        value_change = call_api(full_prompt)

        # 将返回的内容解析为字典
        value_change_dict = self.process(value_change)

        # 更新 value_dict
        for key, change in value_change_dict.items():
            if key in value_dict:
                value_dict[key] = max(0, value_dict[key] + change)  # 确保属性值非负

        return value_dict

    def process(self, value_change: str) -> dict:
        # 将 API 返回的字符串解析为字典
        try:
            # 将字符串解析为字典，例如 "E": -3, "A": -4, ...
            value_change_dict = eval(f"{{{value_change}}}")
            return value_change_dict
        except Exception as e:
            print(f"解析错误: {e}")
            return {}


class SelectAI:  # 构建场景选择AI
    def __init__(self):
        self.select_template = """
        # 场景选择
        以下是玩家的选择选项，请根据玩家当前的属性状态、剧情历史和候选场景列表，选择一个最合适的场景。

        # 玩家选择选项：
        {select_option}

        # 玩家当前属性状态：
        {value_dict}

        # 剧情历史：
        {plot_history}

        # 候选场景列表：
        {scene_list}

        # 选择规则：
        {select_rules}

        # 属性说明：
        {value_desc}

        请按照以上信息选择一个最合适的场景。只输出结果，严格按照以下格式，不要包含任何其他内容：
        ->choosen_scene_name<-
        """

        self.select_rules = """
        1. 选择符合常理和玩家选项的场景；
        2. 选择符合玩家当前属性状态的场景；
        3. 考虑场景对玩家属性可能产生的影响；
        4. 选择能推动剧情发展的场景
        """

        self.select_format = """
        输出严格按照如下格式，不要包含任何别的内容
        ->choosen_scene_name<-
        """

        self.value_desc = """
        E(精力值)：表示角色的体力和精神状态
        A(学业进度)：反映学习成果和知识积累
        B(身体健康状况)：表示整体身体状况
        M(心理健康状况)：反映心理压力和情绪状态
        S(社会关系)：代表人际关系网络的广度和深度
        F(财务状况)：表示经济能力和财务健康
        """

    def invoke(self, select_option: str, value_dict: dict, plot_history: list, scene_list: list) -> str:
        full_prompt = self.select_template.format(
            select_option=select_option,
            value_dict=value_dict,
            plot_history="\n".join(plot_history),
            scene_list=scene_list,
            select_format=self.select_format,
            select_rules=self.select_rules,
            value_desc=self.value_desc
        )

        selected_scene = call_api(full_prompt)
        selected_scene = selected_scene.split('->')[1].split('<-')[0]
        return selected_scene


class SummaryAI:
    def __init__(self):
        self.plot_template = """
        作为大学生活故事线的专家，您的任务是根据给定的场景和玩家属性设计一个引人入胜的剧情。请严格遵循以下指令：

        # 场景描述：
        {scen_desc}

        # 玩家当前属性（请在编写剧情时考虑这些）：
        {value_dict}

        # 属性描述（使用这些来理解每个属性的含义）：
        {value_desc}

        # 剧情规则（请严格遵循这些）：
        {plot_rules}

        # 写作风格指南：
        {plot_style}

        # 剧情历史（请确保连续性）：
        {plot_history}

        # 输出格式（请严格按照以下格式）：
        {plot_format}

        请记住：您的输出必须严格遵循指定的格式，同时提供一个高质量、引人入胜的故事线，反映现代大学生活的复杂性。
        """
        self.plot_rules = """
        1. 生成的概述必须多于15句话，每句话不少于20字。不要生成一长段，每一到两句话隔开一段“^@概述：”
        2. 剧情应只包含概述，体现一个简要但全面的剧情。
        3. 剧情应聚焦于大学生在成长过程中遇到的现实困惑和挑战，反映真实的大学生活。
        4. 通过剧情的展开，让玩家获得独特的人生体验，并在虚拟世界中积累宝贵的人生经验。
        5. 剧情受到当前的属性值影响，但一定注意不要在剧情中体现出属性值的影响。
        """
        self.plot_style = """
        语言风格应贴近现代大学生的表达方式，生动细腻，能够引发玩家的共鸣和思考。使用富有感染力的描述，突出角色的情感和内心世界。风格可参考青春校园类的文学作品，注重心理描写和情感表达。
        剧情中不要出现“我”的主观视角，而是概述我的经历。
        一定注意不要在剧情中体现出属性值的影响，剧情中不要出现“我”的属性值、“我”的属性变化、“我”的属性描述。
        """
        self.plot_format = """
        概述的格式应该是 ^@概述：概述内容
        输出的所有内容不要带上&符号
        输出的内容中不要出现属性值、A值、B值、M值、S值、F值等内容
        """
        self.example_plot = """
        ^@概述：炎热的夏日，窗外的知了声此起彼伏。
        ^@概述：持续了一周的AIGC大赛终于落下了帷幕。
        ^@概述：我们团队的作品获得了第一名。
        ^@概述：我感到非常高兴，因为这是我大学期间最难忘的经历之一。
        """
        self.value_desc = '''
        E(精力值)：表示角色的体力和精神状态
        A(学业进度)：反映学习成果和知识积累
        B(身体健康状况)：表示整体身体状况
        M(心理健康状况)：反映心理压力和情绪状态
        S(社会关系)：代表人际关系网络的广度和深度
        F(财务状况)：表示经济能力和财务健康
        '''

    def invoke(self, scen_desc: str, plot_history: list, value_dict: dict) -> list:
        # 构建完整的 prompt
        full_prompt = self.plot_template.format(
            scen_desc=scen_desc,
            plot_rules=self.plot_rules,
            plot_style=self.plot_style,
            plot_format=self.plot_format,
            plot_history="\n".join(plot_history),
            example_plot=self.example_plot,
            value_dict=value_dict,
            value_desc=self.value_desc
        )

        # 调用API生成剧情
        new_plot = call_api(full_prompt)
        new_plot = self.parse_plot(new_plot)
        return new_plot

    def parse_plot(self, plot: str) -> list:
        # 去掉&符号和换行符
        plot = plot.replace('\n', '')
        li = plot.split('^')[1:]
        res = []
        for item in li:
            if item[0] == '@':
                res.append({item[1:].split('：')[0]: item.split('：')[1]})
            else:
                print("error")
        return res


class EndAI:
    def __init__(self):
        self.plot_template = """
        #任务
        你的任务是根据之前的剧情历史生成一段综述性的大学生活总结，然后再给出类似于红楼梦人物结局的判词

        # 剧情历史：
        以下是之前的剧情内容，用于生成总结内容和判词，请避免重复或矛盾的内容。
        {plot_history}

        # 生成规则：
        请严格遵循以下规则，以确保生成的总结内容和判词符合预期效果：
        1. 总结内容不超过500字，需要分成若干段；判词分四句，每句七个字。
        2. 总结内容清晰凝练，概括整个剧情历史中的内容。
        3. 判词内容具有极高概括性，且极富批判性和反思性。

        # 语言风格：
        总结的风格具有鲜明的大学生特色；
        判词的风格类似红楼梦判词，富有哲理和思考空间，深刻反应剧情内容，如：勘破三春景不长，缁衣顿改昔年妆。可怜绣户侯门女，独卧青灯古佛旁

        # 总结格式：
        请严格使用以下格式输出剧情:
        总结分为五到六段，每一段四到五句，每段段首空两格。

        #判词格式：
        判词在总结之后另外再起一段，分四句，每句七个字，中间用逗号隔开，结尾不要句号。

        # 示例生成：
        为了帮助理解格式和风格，以下是一个示例剧情片段：
        {example}
        """
        self.example = """
          匆匆四年过去，我经历了太多难忘的时光。从最初的迷茫无助，到逐渐找到自己的方向，每一步都留下了成长的痕迹。图书馆里挑灯夜读的身影，实验室里反复实验的坚持，都是青春最美的注脚。
          社团活动给我带来了意想不到的收获。在学生会的工作让我学会了如何与人相处，街舞社的表演让我找到了自信，志愿者服务让我懂得了付出的意义。这些经历，都让我成为了更好的自己。
          学业上的起起落落，让我明白了什么是真正的坚持。考试周的紧张备考，小组作业的通宵达旦，论文答辩的忐忑不安，都成为了最珍贵的回忆。即使有挫折和失败，但每一次都让我变得更加坚强。
          寝室生活是最温暖的记忆。四年里，我们一起吃夜宵，一起熬夜赶作业，一起分享喜怒哀乐。那些深夜的谈心，互相的鼓励和支持，都让我感受到了真挚的友情。
          在这片充满希望的校园里，我不仅收获了知识，更找到了人生的方向。那些看似平凡的日子，却处处闪耀着青春的光芒。
          勘破三春景不长，缁衣顿改昔年妆。可怜绣户侯门女，独卧青灯古佛旁
        """

    def invoke(self, plot_history: list) -> list:
        # 构建完整的 prompt
        full_prompt = self.plot_template.format(
            plot_history="\n".join(plot_history),
            example=self.example,
        )

        # 调用API生成剧情
        end = call_api(full_prompt)
        end = self.parse_plot(end)
        return end

    def parse_plot(self, plot: str) -> list:
        li = plot.split('\n')
        li = [celebrity for celebrity in li if celebrity != '']
        return li
