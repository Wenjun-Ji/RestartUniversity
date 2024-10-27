import requests
import json


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
        "max_tokens": 2000,
        "temperature": 0.7,
        "stream": False
    })

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        completion = response.json()["choices"][0]["message"]["content"]
        return completion
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")


class TextAI:
    def __init__(self):
        self.plot_template = """
        As an expert in crafting engaging university life storylines, your task is to design a compelling plot based on the given scenario and player attributes. Follow these instructions precisely:

        1. Scenario Description:
        ***
        {scen_desc}
        ***

        2. Player's Current Attributes (Please consider these when crafting the plot):
        %%%
        {value_dict}
        %%%

        3. Attributes Description (Use this to understand the meaning of each attribute):
        ^^^
        {value_desc}
        ^^^

        4. Plot Rules (Please adhere strictly to these):
        $$$
        {plot_rules}
        $$$

        5. Writing Style Guidelines:
        ###
        {plot_style}
        ###

        6. Plot History (Please ensure continuity):
        @@@
        {plot_history}
        @@@

        7. Output Format (Please follow this exactly):
        &&&
        {plot_format}
        &&&
        
        Remember: Your output must strictly adhere to the specified format while delivering a high-quality, engaging storyline that reflects the complexities of modern university life.
        """
        self.plot_rules = """
        1. 剧情长度不超过500字。
        2. 剧情应包含旁白、人物对话或人物内心独白等元素，体现丰富的场景切换和深度对话。
        3. 旁白应对场景进行详细描述，确保读者能够清晰感受到环境、时间、人物的动作等。
        4. 人物内心独白应反映角色内心的冲突或情感波动，并能推动剧情的发展。
        5. 剧情应聚焦于大学生在成长过程中遇到的现实困惑和挑战，反映真实的大学生活。
        6. 通过剧情的展开，让玩家获得独特的人生体验，并在虚拟世界中积累宝贵的人生经验。
        """
        self.plot_style = """
        语言风格应贴近现代大学生的表达方式，生动细腻，能够引发玩家的共鸣和思考。使用富有感染力的描述，突出角色的情感和内心世界。风格可参考青春校园类的文学作品，注重心理描写和情感表达。
        """
        self.plot_format = """
        旁白的格式应该是 ^@旁白：旁白内容
        人物对话格式应该是 ^#人物名字：人物所说的话。
        人物内心独白格式应该是 ^$人物名字：（人物内心独白内容）
        输出的所有内容不要带上&
        """
        self.example_plot = """
        ^@旁白：炎热的夏日，窗外的知了声此起彼伏。
        ^#我：高考终于结束了，感觉像做了一场梦。
        ^$我：（未来的路该怎么走？我有些迷茫。）
        ^#爸爸：接下来有什么打算？
        ^#我：可能会选择自己感兴趣的专业吧。
        ^@旁白：我和父母讨论着未来，内心却充满了不确定和期待。
        """
        self.value_desc = '''
        E(精力值)：表示角色的体力和精神状态
        A(学业进度)：反映学习成果和知识积累
        B(身体健康状况)：表示整体身体状况
        M(心理健康状况)：反映心理压力和情绪状态
        S(社会关系)：代表人际关系网络的广度和深度
        F(财务状况)：表示经济能力和财务健康
        '''

    def invoke(self, scen_desc: str, plot_history: list, value_dict: str) -> list:
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

        # 将 full_prompt 写入文件
        with open(r'D:\Program\renpy-8.3.2-sdk\Nankai simulator\plot.txt', 'a', encoding='utf-8') as f:
            f.write("\n===================================Full prompt===================================\n")
            f.write(f"Full prompt: \n{full_prompt}\n")
        
        # 调用API生成剧情
        new_plot = call_api(full_prompt)
        new_plot = self.parse_plot(new_plot)
        return new_plot
    
    def parse_plot(self, plot: str) -> list:
        # 打开文件并在一开始写入原始的 plot
        with open(r'D:\Program\renpy-8.3.2-sdk\Nankai simulator\plot.txt', 'a', encoding='utf-8') as f:
            f.write("\n===========================Original plot===========================\n")
            f.write(f"Original plot: \n{plot}\n")  # 写入原始 plot 并换行

        # 去掉&符号和换行符
        plot = plot.replace('&', '').replace('\n', '')
        li = plot.split('^')[1:]
        res = []
        
        # 处理每个条目
        for item in li:
            if item[0] == '@' or item[0] == '#' or item[0] == '$':
                parsed_item = {item[1:].split('：')[0]: item.split('：')[1]}
                res.append(parsed_item)
            else:
                print("error")

        # 处理完成后再将结果写入文件，并用换行符或者符号间隔
        with open('plot.txt', 'a', encoding='utf-8') as f:
            f.write("\n===========================Processed plot===========================\n")
            f.write("\nProcessed plot:\n")
            for parsed_item in res:
                f.write(f"{parsed_item}\n---\n")  # 每个条目之间用 '---' 作为间隔符

        return res



class ValueAI:
    def __init__(self):
        self.value_template = """
        As an expert value judgment system for a Ren'Py game, your task is to precisely determine attribute changes based on plot developments. Follow these instructions meticulously:

        1. Player Attributes:
        The player's attributes include: {value_desc}

        2. Current Plot:
        Analyze the following plot carefully:
        ***
        {current_plot}
        ***

        3. Value Change Rules:
        Adhere strictly to these rules when determining changes:
        $$$
        {value_rules}
        $$$

        4. Allowed Change Range:
        Ensure all changes fall within this range:
        ###
        {value_change_range}
        ###

        5. Output Format:
        Your output MUST follow this format exactly, with no additional content:
        &&&
        {value_format}
        &&&
        
        Remember: Accuracy and adherence to the specified format are crucial. Provide a thoughtful, well-reasoned analysis that captures the nuanced effects of the plot on player attributes.
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
        self.value_format = """
        ^E：value_dict['E']+5
        ^A：value_dict['A']-10
        ^B：value_dict['B']+3
        ^M：value_dict['M']-2
        ^S：value_dict['S']+1
        ^F：value_dict['F']-50
        """

    def invoke(self, current_plot: list, value_change_range: str, value_dict: dict) -> list:
        # 构建完整的 prompt
        full_prompt = self.value_template.format(
            current_plot=current_plot,
            value_change_range=value_change_range,
            value_rules=self.value_rules,
            value_format=self.value_format,
            value_desc=self.value_desc
        )

        # 将 full_prompt 写入文件
        with open(r'D:\Program\renpy-8.3.2-sdk\Nankai simulator\plot.txt', 'a', encoding='utf-8') as f:
            f.write("\n===================================Full prompt===================================\n")
            f.write(f"Full prompt: \n{full_prompt}\n")

        # 调用API生成剧情
        value_change = call_api(full_prompt)
        
        # 将 value_change 写入文件
        with open(r'D:\Program\renpy-8.3.2-sdk\Nankai simulator\plot.txt', 'a', encoding='utf-8') as f:
            f.write("\n===========================Value change===========================\n")
            f.write(f"Value change: \n{value_change}\n")
        
        value = self.process(value_change, value_dict)
        return value

    def process(self, value_change: str, value_dict: dict):
        # 提取两个&&&之间的内容
        value_change = value_change.split('&&&')[1]
        value_change = value_change.replace('\n', '')
        li = value_change.split('^')[1:]
        for item in li:
            value_dict[item.split('：')[0]] = eval(item.split('：')[1])
        return value_dict


class SelectAI:  # 构建场景选择AI
    def __init__(self):
        self.select_template = """
        As an expert scene selector for a Ren'Py game, your task is to choose the most appropriate scene based on the player's choice and attributes. Follow these instructions meticulously:

        1. Player's Selected Option:
        ***
        {select_option}
        ***

        2. Player's Current Attributes:
        ~~~
        {value_dict}
        ~~~

        3. Attribute Descriptions (Use this to understand the meaning of each attribute):
        ^^^
        {value_desc}
        ^^^

        4. Plot History (Consider this for context and continuity):
        @@@
        {plot_history}
        @@@

        5. Available Scenes (You must choose from this list only):
        ###
        {scene_list}
        ###

        6. Selection Rules (Adhere strictly to these):
        $$$
        {select_rules}
        $$$

        7. Output Format (Your response must follow this format exactly, with no additional content):
        &&&
        {select_format}
        &&&
        
        Remember: Your selection must be precisely formatted and well-reasoned, considering all provided information to create a cohesive and engaging gameplay experience.
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

        self.value_desc = "E(精力值)，A（学业进度），B（身体健康状况），M（心理健康状况），S（社会关系），F（财务状况）"


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
