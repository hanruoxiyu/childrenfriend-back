import random
import sys
sys.path.append('/home/pi/django/knowledgeApp/neodb')
from query_neo4j import Query


class CQLCreate:
    def __init__(self):
        self.cql_growth = [
            ['MATCH (n:宝宝) RETURN n.node_name'],
            ['match (m:宝宝)-[]->() where m.baby_stage=', 'baby_stage', ' return distinct m.baby_age_message'],

        ]

        self.cql_nutrient = [
            ["match (p:营养与喂养)-[r]->(m) where p.node_name='新生儿' +'营养特点' return m.node_name"],
            ["match (p:营养与喂养)-[r:包含]->(m:营养方面细节) where p.node_name='新生儿'+'营养补充'  return m.node_name"]
        ]

        self.cql_nursing = [
            ["match (p:保健护理细节)-[r:包含]->(m:保健护理细节的内容) where p.node_name='新生儿'+'保暖'  return distinct m.node_name"],
            ["match (p:保健护理细节)-[r:包含]->(m:保健护理细节的内容) where p.node_name='新生儿'+'睡眠'  return distinct m.node_name"],
            ["match (p:保健护理细节)-[r:包含]->(m:保健护理细节的内容) where p.node_name='新生儿'+'免疫接种'  return distinct m.node_name"]
        ]
        self.cql_development = [
            ["match (p:儿童教育)-[r:包含]->(m:儿童教育内容) where p.node_name='新生儿'+'同胞教育'  return distinct m.node_name"]]
        self.cql_illness = [
            ["match (p:年龄)-[r:常见疾病方面]->(m:常见疾病) where p.node_name=", "baby_age", " return m.node_name"],
            ["MATCH (n:常见疾病) RETURN n.node_name"],
            ["match (p:常见疾病) where p.node_name=", "illness_name", " return distinct p.symptom"],
            ["match (p:常见疾病) where p.node_name=", "illness_name", " return distinct p.treatment"]
        ]
        self.cql_cloth = [
            ["match (p:穿着方面内容)-[r:包含]->(m:穿着方面细节) where p.node_name='衣服做工' return distinct m.node_name"],
            ["match (p:穿着方面内容)-[r:包含]->(m:穿着方面细节) where p.node_name='衣服风格' return distinct m.node_name"],
            ["match (p:穿着方面内容)-[r:包含]->(m:穿着方面细节) where p.node_name='衣服材质' return distinct m.node_name"],
            ["match (p:穿着方面内容)-[r:包含]->(m:穿着方面细节) where p.node_name='衣服大小' return distinct m.node_name"],
            ["match (p:穿着方面内容)-[r:包含]->(m:穿着方面细节) where p.node_name='衣服厚度'  return distinct m.node_name"],
            ["match (p:穿着方面内容)-[r:包含]->(m:穿着方面细节) where p.node_name='给孩子穿衣服' return distinct m.node_name"]
        ]

        self.word_lists = {
            'baby_stage': ["'新生儿'", "'婴儿阶段'", "'幼儿阶段'", "'学龄前儿童'"],
            'baby_age': ["'0-28天宝宝'", "'1个月宝宝'", "'2个月宝宝'", "'3个月宝宝'", "'4个月宝宝'", "'5个月宝宝'", "'6个月宝宝'", "'7个月宝宝'",
                         "'8个月宝宝'", "'9个月宝宝'",
                         "'10个月宝宝'", "'11个月宝宝'", "'12个月宝宝'", "'1至2岁宝宝'", "'2至3岁宝宝'", "'3至4岁宝宝'", "'4至6岁宝宝'"],
            "illness_name": ["'呼吸困难'", "'新生儿腹泻'", "'过渡睡眠'", "'眼部感染'", "'新生儿发热'", "'松软'", "'听觉问题'", "'黄疸'", "'颤抖'",
                             "'出疹和感染'", "'鹅口疮'", "'视觉问题'",
                             " '新生儿呕吐'", "'体重增加'", "'耳部感染'", "'出疹与皮肤疾病'", " '上呼吸道感染'", "'发热'", "'流感'", "'感冒'", "'咳嗽'",
                             "'呕吐'", "'肺炎'", "'支气管炎'",
                             "'哮喘'"]
        }
        # 连接数据库
        self.graph = Query()

    # module是数组
    def create(self, module):
        cql_m = random.choice(module)
        if cql_m == '宝宝成长':
            cql = random.choice(self.cql_growth)
        elif cql_m == '宝宝饮食':
            cql = random.choice(self.cql_nutrient)
        elif cql_m == '宝宝发育':
            cql = random.choice(self.cql_development)
        elif cql_m == '宝宝护理':
            cql = random.choice(self.cql_nursing)
        elif cql_m == '宝宝疾病':
            cql = random.choice(self.cql_illness)
        elif cql_m == '宝宝穿搭':
            cql = random.choice(self.cql_cloth)
        cql = ''.join(self.get_word(str_cql) for str_cql in cql)
        return self.get_answer(cql)

    def get_word(self, str_cql):
        if str_cql == 'baby_stage':
            return random.choice(self.word_lists.get(str_cql, []))
        elif str_cql == 'baby_age':
            return random.choice(self.word_lists.get(str_cql, []))
        elif str_cql == 'illness_name':
            return random.choice(self.word_lists.get(str_cql, []))
        return str_cql

    def get_answer(self, cql):
        answer = self.graph.run(cql)
        answer_list = list(answer)
        answers = []
        for ans in answer_list:
            answers.append(str(ans[0]))
        answers = " ".join(answers)
        return answers
