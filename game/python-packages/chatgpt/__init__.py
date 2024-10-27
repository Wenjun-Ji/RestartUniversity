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
        以下是当前剧情的场景描述，请根据场景设置生成符合以下规则的剧情片段。
        场景描述：
        {scen_desc}

        # 剧情生成规则：
        请严格遵循以下规则，以确保剧情符合预期效果：
        1. 每个剧情片段的长度不超过500字。
        2. 剧情应包含旁白、人物对话和人物内心独白，确保场景切换自然、对话真实。
        3. 旁白需详细描述场景，包括环境、时间、人物动作等，帮助玩家身临其境。
        4. 人物内心独白需反映角色内心的冲突或情感波动，推动剧情发展。
        5. 剧情围绕大学生活中的现实挑战展开，例如学业压力、人际关系、未来迷茫等，展现真实的成长历程。

        # 语言风格：
        剧情的语言风格应贴近现代大学生的表达方式，细腻、生动，能够引发玩家的共鸣和思考。描述应具有感染力，尤其是对角色情感和内心世界的刻画。风格可参考青春校园文学作品，着重于心理描写和情感表达。

        # 剧情格式：
        请严格使用以下格式输出剧情，每种内容类型都应单独一行，不要混合，**确保输出的内容不包含任何与剧情内容无关的信息**:
        1. 每行剧情内容必须严格以特定符号开头，按照以下格式编写：
            - 旁白格式：`^@旁白：旁白内容`
            - 人物对话格式：`^#人物名字：人物所说的话`
            - 人物内心独白格式：`^$人物名字：（人物内心独白内容）`

        2. 确保每一行的内容准确对应格式符号的类型，旁白行只能用 `^@` 开头，对话行只能用 `^#` 开头，内心独白只能用 `^$` 开头。

        3. 避免使用重复的开头符号或不完整的内容，确保剧情紧凑、明确。未遵循格式的输出内容将被视为错误。

        # 剧情历史：
        以下是之前的剧情片段，用于参考剧情的延续性和逻辑性，请避免重复或矛盾的内容。
        {plot_history}

        # 示例剧情：
        为了帮助理解格式和风格，以下是一个示例剧情片段：
        {example_plot}

        # 角色属性描述：
        请参考以下角色属性，确保剧情中体现角色的状态和特征。
        {value_desc}

        # 当前角色属性：
        {value_dict}

        # 生成要求：
        请根据以上内容生成新的、具有创意的剧情片段，体现角色的成长和变化。
        """
        self.plot_format = """
        旁白的格式是 ^@旁白：旁白内容
        人物对话格式是 ^#人物名字：人物所说的话。
        人物内心独白格式是 ^$人物名字：（人物内心独白内容）
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
        以下为当前剧情片段，用于分析该剧情对角色各项属性的影响。
        剧情片段：
        {current_plot}

        # 属性变化规则：
        请根据以下规则判断剧情对角色属性的影响，并生成符合逻辑的属性变化：
        {value_rules}

        # 属性说明：
        以下为各项属性的具体含义，请参考这些描述，确保生成的属性变化符合角色当前状态及剧情需要。
        {value_desc}

        # 属性变化格式：
        请根据剧情和范围生成属性变化，只需给出最终的属性变化结果，不要输出任何与“角色属性更新”相关的提示。
        返回格式严格为：
        "E": -3, "A": -4, "B": -2, "M": -15, "S": -7, "F": -4

        # 属性变化范围：
        以下为可能的属性变化范围，确保变化量在合理范围内：
        {value_change_range}

        # 生成要求：
        请根据剧情片段、属性变化规则和范围生成符合逻辑的属性变化，并严格按照以上格式输出。
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
