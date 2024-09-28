# -*- coding: UTF-8 -*-
# 连接数据库，生成查询语句，返回结果

import re
import sys
sys.path.append('/home/pi/django/knowledgeApp/neodb')
from query_neo4j import Query


class QuestionTemplate():
	def __init__(self):
		self.q_template_dict = {
			1: self.get_baby_knowledge,
			2: self.get_age_grade_detail,
			3: self.get_baby_nutrient_characteristics,
			4: self.get_baby_feeding_method,
			5: self.get_baby_supplementary_food,
			6: self.get_baby_dietary_arrangement,
			7: self.get_baby_clothe_work,
			8: self.get_baby_clothe_style,
			9: self.get_baby_clothe_material,
			10: self.get_baby_clothe_size,
			11: self.get_baby_clothe_thickness,
			12: self.get_baby_clothe_method,
			13: self.get_baby_nursing,
			14: self.get_baby_warmth,
			15: self.get_baby_sleep,
			16: self.get_baby_healthcare_matters,
			17: self.get_baby_physical_examination,
			18: self.get_baby_immunization,
			19: self.get_baby_security_check,
			20: self.get_baby_weight,
			21: self.get_baby_height,
			22: self.get_baby_head_circumference,
			23: self.get_baby_chest_circumference,
			24: self.get_baby_tooth,
			25: self.get_baby_exercise,
			26: self.get_baby_sense,
			27: self.get_baby_language_development,
			28: self.get_baby_cognitive_development,
			29: self.get_baby_sociability,
			30: self.get_baby_emotional_development,
			31: self.get_baby_finger_development,
			32: self.get_baby_health_indicator,
			33: self.get_baby_intelligence,
			34: self.get_baby_compatriot,
			35: self.get_baby_behavior,
			36: self.get_baby_family_education,
			37: self.get_baby_illness,
			38: self.get_baby_illness_name,
			39: self.get_baby_illness_symptom,
			40: self.get_baby_illness_therapies
		}

		# 连接数据库
		self.graph = Query()

	def get_question_answer(self, question, template):
		# 如果问题模板的格式不正确则结束
		assert len(str(template).strip().split("\t")) == 2
		template_id, template_str = int(str(template).strip().split("\t")[0]), str(template).strip().split("\t")[1]
		self.template_id = template_id
		self.template_str2list = str(template_str).split()

		# 预处理问题
		question_word, question_flag = [], []
		for one in question:
			word, flag = one.split("/")
			question_word.append(str(word).strip())
			question_flag.append(str(flag).strip())
		assert len(question_flag) == len(question_word)
		self.question_word = question_word
		self.question_flag = question_flag
		self.raw_question = question
		# 根据问题模板来做对应的处理，获取答案
		# print("template_id:"+template_id)
		answer = self.q_template_dict[template_id]()
		return answer

	# 获取阶段名字
	def get_baby_stage(self):
		## 获取nb在原问题中的下标
		tag_index = self.question_flag.index("nb")
		## 获取阶段名称
		baby_stage = self.question_word[tag_index]
		return baby_stage

	def get_name(self, type_str):
		name_count = self.question_flag.count(type_str)
		if name_count == 1:
			## 获取标签在原问题中的下标
			tag_index = self.question_flag.index(type_str)
			## 获取标签名称
			name = self.question_word[tag_index]
			return name
		else:
			result_list = []
			for i, flag in enumerate(self.question_flag):
				if flag == str(type_str):
					result_list.append(self.question_word[i])
			return result_list

	# 获取问题中的数字

	"""
		def get_num_x(self):
		x = re.sub(r'\D', "", "".join(self.question_word))
		return x
	"""

	# 1.获取育儿知识
	def get_baby_knowledge(self):
		# 宝宝分为几个阶段，这个是在原问题中抽取的
		baby_stage = self.get_name('nnb')
		cql = f"MATCH (n:宝宝) RETURN n.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		answer_list = list(answer)
		answers = []
		for ans in answer_list:
			answers.append(str(ans[0]))
		answers = "、".join(answers)
		final_answer = baby_stage + "知识包含" + answers + "阶段！"
		print("查询答案为："+"\n"+final_answer)
		return final_answer

	# 2.宝宝各阶段详情
	def get_age_grade_detail(self):
		# 获取阶段名称，这个是在原问题中抽取的
		baby_stage = self.get_name('nt')
		print(baby_stage)
		cql = f"match (m:宝宝)-[]->() where m.baby_stage='{baby_stage}' return distinct m.baby_age_message"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		final_answer = baby_stage + "指："+ list(answer)[0][0]
		print("查询答案为："+"\n"+final_answer)
		return final_answer

	# 3.某阶段宝宝的营养特点
	def get_baby_nutrient_characteristics(self):
		# 某阶段宝宝的营养特点，这个是在原问题中抽取的
		baby_stage = self.get_baby_stage()
		print(baby_stage)
		cql = f"match (p:营养与喂养)-[r]->(m) where p.node_name='{baby_stage}' +'营养特点' return m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		final_answer = list(answer)[0][0]
		print("查询答案为："+"\n"+final_answer)
		return final_answer

	# 4.某阶段宝宝的喂养
	def get_baby_feeding_method(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:营养与喂养)-[r:包含]->(m:营养方面细节) where p.node_name='{baby_stage}' + '喂养'  return m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		answer_list = list(answer)
		answers = []
		for ans in answer_list:
			answers.append(str(ans[0]))
		answers = " ".join(answers)
		final_answer = baby_stage + "喂养方法：" + answers
		print("查询答案为："+"\n"+final_answer)
		return final_answer

	# 5.某阶段宝宝的补充食物
	def get_baby_supplementary_food(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:营养与喂养)-[r:包含]->(m:营养方面细节) where p.node_name='{baby_stage}'+'营养补充'  return m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		answer_list = list(answer)
		answers = []
		for ans in answer_list:
			answers.append(str(ans[0]))
		answers = "、".join(answers)
		final_answer = baby_stage + "营养补充包括：" + answers
		print("查询答案为："+"\n"+final_answer)
		return final_answer

	# 6.某阶段宝宝的膳食安排
	def get_baby_dietary_arrangement(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:营养与喂养)-[r:包含]->(m:营养方面细节) where p.node_name='{baby_stage}'+'食谱'  return m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		answer_list = list(answer)
		answers = []
		for ans in answer_list:
			answers.append(str(ans[0]))
		answers = " ".join(answers)
		final_answer = baby_stage + "食谱：" + answers
		print("查询答案为："+"\n"+final_answer)
		return final_answer

	# 7.宝宝的衣服做工
	def get_baby_clothe_work(self):
		cql = f"match (p:穿着方面内容)-[r:包含]->(m:穿着方面细节) where p.node_name='衣服做工' return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		final_answer = "宝宝衣服做工要求：" + str(list(answer)[0][0])
		print("查询答案为：" +"\n"+ final_answer)
		return final_answer

	# 8.宝宝的衣服款式
	def get_baby_clothe_style(self):
		cql = f"match (p:穿着方面内容)-[r:包含]->(m:穿着方面细节) where p.node_name='衣服风格' return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		final_answer = "宝宝衣服款式要求：" + str(list(answer)[0][0])
		print("查询答案为：" +"\n"+ final_answer)
		return final_answer

	# 9.宝宝的衣服材质
	def get_baby_clothe_material(self):
		cql = f"match (p:穿着方面内容)-[r:包含]->(m:穿着方面细节) where p.node_name='衣服材质' return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		final_answer = "宝宝衣服材质要求：" + str(list(answer)[0][0])
		print("查询答案为："+"\n" + final_answer)
		return final_answer

	# 10.宝宝的衣服尺寸
	def get_baby_clothe_size(self):
		cql = f"match (p:穿着方面内容)-[r:包含]->(m:穿着方面细节) where p.node_name='衣服大小' return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		final_answer = "宝宝衣服尺寸要求：" + str(list(answer)[0][0])
		print("查询答案为：" +"\n"+ final_answer)
		return final_answer

	# 11.宝宝的衣服厚薄
	def get_baby_clothe_thickness(self):
		cql = f"match (p:穿着方面内容)-[r:包含]->(m:穿着方面细节) where p.node_name='衣服厚度'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		final_answer = "宝宝衣服厚度要求：" + str(list(answer)[0][0])
		print("查询答案为：" +"\n"+ final_answer)
		return final_answer

	# 12.宝宝的穿衣方式
	def get_baby_clothe_method(self):
		cql = f"match (p:穿着方面内容)-[r:包含]->(m:穿着方面细节) where p.node_name='给孩子穿衣服' return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		final_answer = "给宝宝穿衣的方式：" + str(list(answer)[0][0])
		print("查询答案为：" +"\n"+ final_answer)
		return final_answer

	# 13.某阶段宝宝的基本护理
	def get_baby_nursing(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:保健护理)-[r:包含]->(m:保健护理细节) where p.node_name='{baby_stage}'+'基本护理'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		answer_list = list(answer)
		answers = []
		for ans in answer_list:
			answers.append(str(ans[0]))
		answers = "、".join(answers)
		final_answer = baby_stage + "的基本护理包括：" + answers + "等内容。"
		print("查询答案为："+"\n" + final_answer)
		return final_answer

	# 14.某阶段宝宝的保暖方法
	def get_baby_warmth(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:保健护理细节)-[r:包含]->(m:保健护理细节的内容) where p.node_name='{baby_stage}'+'保暖'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		final_answer = baby_stage +"的保暖方法是：" + str(list(answer)[0][0])
		print("查询答案为："+"\n"+final_answer)
		return final_answer

	# 15.某阶段宝宝的睡眠
	def get_baby_sleep(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:保健护理细节)-[r:包含]->(m:保健护理细节的内容) where p.node_name='{baby_stage}'+'睡眠'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		answer_list = list(answer)
		answers = []
		for ans in answer_list:
			answers.append(str(ans[0]))
		answers = "、".join(answers)
		final_answer = baby_stage + "的睡眠情况：" + answers
		print("查询答案为："+"\n" + final_answer)
		return final_answer

	# 16.某阶段宝宝的护理注意事项
	def get_baby_healthcare_matters(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:保健护理)-[r:包含]->(m:保健护理细节) where p.node_name='{baby_stage}'+'护理注意事项'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		final_answer = baby_stage +"的护理注意事项有：" + str(list(answer)[0][0])
		print("查询答案为：" +"\n"+ final_answer)
		return final_answer

	# 17.某阶段宝宝的定期体检
	def get_baby_physical_examination(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:保健护理细节)-[r:包含]->(m:保健护理细节的内容) where p.node_name='{baby_stage}'+'定期体检'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		final_answer = baby_stage +"的定期体检方法：" + str(list(answer)[0][0])
		print("查询答案为："+"\n" + final_answer)
		return final_answer

	# 18.某阶段宝宝的免疫接种
	def get_baby_immunization(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:保健护理细节)-[r:包含]->(m:保健护理细节的内容) where p.node_name='{baby_stage}'+'免疫接种'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		final_answer = baby_stage +"的免疫接种：" + str(list(answer)[0][0])
		print("查询答案为：" +"\n"+ final_answer)
		return final_answer

	# 19.某阶段宝宝的安全检查
	def get_baby_security_check(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:保健护理)-[r:包含]->(m:保健护理细节) where p.node_name='{baby_stage}'+'安全检查'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		answer_list = list(answer)
		answers = []
		for ans in answer_list:
			answers.append(str(ans[0]))
		answers = "、".join(answers)
		final_answer = baby_stage + "的安全检查事项有：" + answers + "等内容。"
		print("查询答案为：" +"\n"+ final_answer)
		return final_answer

	# 20.某阶段宝宝正常的体重范围
	def get_baby_weight(self):
		# 宝宝分为几个阶段，这个是在原问题中抽取的
		baby_stage = self.get_baby_stage()
		cql = f"match (p:年龄)-[r1:生长发育方面]->(m:生长发育)-[r2:包含]->(n)  where p.node_name='{baby_stage}' and r2.relationships='体重' return n.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		# print(list(answer)[0][0])
		final_answer = baby_stage + "的正常的体重范围是：" + str(list(answer)[0][0]) + "。"
		print("查询答案为："+"\n" + final_answer)
		return final_answer

	# 21.某阶段宝宝正常的身高范围
	def get_baby_height(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:年龄)-[r1:生长发育方面]->(m:生长发育)-[r2:包含]->(n)  where p.node_name='{baby_stage}' and r2.relationships='身长' return n.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		# print(list(answer)[0][0])
		final_answer = baby_stage + "的正常的身高范围是：" + str(list(answer)[0][0]) + "。"
		print("查询答案为：" +"\n"+ final_answer)
		return final_answer

	# 22.某阶段宝宝正常的头围范围
	def get_baby_head_circumference(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:年龄)-[r1:生长发育方面]->(m:生长发育)-[r2:包含]->(n)  where p.node_name='{baby_stage}' and r2.relationships='头围' return n.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		# print(list(answer)[0][0])
		final_answer = baby_stage + "的正常的头围范围是：" + str(list(answer)[0][0]) + "。"
		print("查询答案为："+"\n" + final_answer)
		return final_answer

	# 23.某阶段宝宝正常的胸围范围
	def get_baby_chest_circumference(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:年龄)-[r1:生长发育方面]->(m:生长发育)-[r2:包含]->(n)  where p.node_name='{baby_stage}' and r2.relationships='胸围' return n.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		# print(list(answer)[0][0])
		final_answer = baby_stage + "的正常的胸围范围是：" + str(list(answer)[0][0]) + "。"
		print("查询答案为：" +"\n"+ final_answer)
		return final_answer

	# 24.某阶段宝宝的长牙情况
	def get_baby_tooth(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:年龄)-[r1:生长发育方面]->(m:生长发育)-[r2:包含]->(n)  where p.node_name='{baby_stage}' and r2.relationships='牙齿' return n.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		# print(list(answer)[0][0])
		final_answer = baby_stage + "的长牙情况：" + str(list(answer)[0][0])
		print("查询答案为："+"\n" + final_answer)
		return final_answer

	# 25.某阶段宝宝的运动发育标准
	def get_baby_exercise(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:生长发育)-[r:包含]->(m:生长发育细节) where p.node_name='{baby_stage}'+'运动'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		# print(list(answer)[0][0])
		final_answer = baby_stage + "的运动发育里程碑：" + str(list(answer)[0][0])
		print("查询答案为："+"\n" + final_answer)
		return final_answer

	# 26.某阶段宝宝的感官发育
	def get_baby_sense(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:生长发育)-[r:包含]->(m:生长发育细节) where p.node_name='{baby_stage}'+'感官发育'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		answer_list = list(answer)
		answers = []
		for ans in answer_list:
			answers.append(str(ans[0]))
		answers = "、".join(answers)
		final_answer = baby_stage + "的感官发育包括：" + answers + "等内容。"
		print("查询答案为："+"\n" + final_answer)
		return final_answer

	# 27.某阶段宝宝的语言发育
	def get_baby_language_development(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:生长发育)-[r:包含]->(m:生长发育细节) where p.node_name='{baby_stage}'+'语言发育'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		# print(list(answer)[0][0])
		final_answer = baby_stage + "的语言发育里程碑：" + str(list(answer)[0][0])
		print("查询答案为："+"\n" + final_answer)
		return final_answer

	# 28.某阶段宝宝的认知发育
	def get_baby_cognitive_development(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:生长发育)-[r:包含]->(m:生长发育细节) where p.node_name='{baby_stage}'+'认知发育'  return distinct m.node_name"
		print("cql语句："+cql)
		answer = self.graph.run(cql)
		# print(list(answer)[0][0])
		final_answer = baby_stage + "的认知发育里程碑：" + str(list(answer)[0][0])
		print("查询答案为："+"\n" + final_answer)
		return final_answer

	# 29.某阶段宝宝的社交能力
	def get_baby_sociability(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:生长发育)-[r:包含]->(m:生长发育细节) where p.node_name='{baby_stage}'+'社交能力发育'  return distinct m.node_name"
		print("cql语句："+cql)
		answer = self.graph.run(cql)
		# print(list(answer)[0][0])
		final_answer = baby_stage + "的社交能力发育里程碑：" + str(list(answer)[0][0])
		print("查询答案为：" +"\n"+ final_answer)
		return final_answer

	# 30.某阶段宝宝的情感发育
	def get_baby_emotional_development(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:生长发育)-[r:包含]->(m:生长发育细节) where p.node_name='{baby_stage}'+'情感发育'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		# print(list(answer)[0][0])
		final_answer = baby_stage + "的情感发育里程碑：" + str(list(answer)[0][0])
		print("查询答案为：" +"\n"+ final_answer)
		return final_answer

	# 31.某阶段宝宝手和手指的技能发育
	def get_baby_finger_development(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:生长发育)-[r:包含]->(m:生长发育细节) where p.node_name='{baby_stage}'+'手和手指的技能'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		# print(list(answer)[0][0])
		final_answer = baby_stage + "的手和手指的技能发育情况：" + str(list(answer)[0][0])
		print("查询答案为：" +"\n"+ final_answer)
		return final_answer

	# 32.某阶段宝宝的健康发育观察标准
	def get_baby_health_indicator(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:生长发育)-[r:包含]->(m:生长发育细节) where p.node_name='{baby_stage}'+'健康发育观察项目'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		answer_list = list(answer)
		answers = []
		for ans in answer_list:
			answers.append(str(ans[0]))
		answers = "、".join(answers)
		final_answer = baby_stage + "的健康发育观察项目包括：" + answers + "等内容。"
		print("查询答案为：" +"\n"+ final_answer)
		return final_answer

	# 33.某阶段宝宝的智力开发
	def get_baby_intelligence(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:儿童教育)-[r:包含]->(m:儿童教育内容) where p.node_name='{baby_stage}'+'智力开发'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		answer_list = list(answer)
		answers = []
		for ans in answer_list:
			answers.append(str(ans[0]))
		answers = " ".join(answers)
		final_answer = "促进" + baby_stage + "智力开发的方法包括：" + answers
		print("查询答案为："+"\n" + final_answer)
		return final_answer

	# 34.某阶段宝宝的同胞教育
	def get_baby_compatriot(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:儿童教育)-[r:包含]->(m:儿童教育内容) where p.node_name='{baby_stage}'+'同胞教育'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		answer_list = list(answer)
		answers = []
		for ans in answer_list:
			answers.append(str(ans[0]))
		answers = " ".join(answers)
		final_answer = baby_stage + "同胞教育内容包括：" + answers
		print("查询答案为："+"\n" + final_answer)
		return final_answer

	# 35.某阶段宝宝的行为教育
	def get_baby_behavior(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:儿童教育)-[r:包含]->(m:儿童教育内容) where p.node_name='{baby_stage}'+'行为教育'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		answer_list = list(answer)
		answers = []
		for ans in answer_list:
			answers.append(str(ans[0]))
		answers = " ".join(answers)
		final_answer = baby_stage + "行为教育内容包括：" + answers
		print("查询答案为："+"\n" + final_answer)
		return final_answer

	# 36.某阶段宝宝的家庭教育
	def get_baby_family_education(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:儿童教育)-[r:包含]->(m:儿童教育内容) where p.node_name='{baby_stage}'+'家庭教育'  return distinct m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		answer_list = list(answer)
		answers = []
		for ans in answer_list:
			answers.append(str(ans[0]))
		answers = " ".join(answers)
		final_answer = baby_stage + "家庭教育内容包括：" + answers
		print("查询答案为："+"\n" + final_answer)
		return final_answer

	# 37.某阶段宝宝易患的疾病
	def get_baby_illness(self):
		baby_stage = self.get_baby_stage()
		cql = f"match (p:年龄)-[r:常见疾病方面]->(m:常见疾病) where p.node_name='{baby_stage}'  return m.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		answer_list = list(answer)
		answers = []
		for ans in answer_list:
			answers.append(str(ans[0]))
		answers = "、".join(answers)
		final_answer = baby_stage + "易患的疾病有" + answers + "等。"
		print("查询答案为："+"\n" + final_answer)
		return final_answer


	# 38.获取常见的儿科疾病名称
	def get_baby_illness_name(self):
		cql = f"MATCH (n:常见疾病) RETURN n.node_name"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		answer_list = list(answer)
		answers = []
		for ans in answer_list:
			answers.append(str(ans[0]))
		answers = "、".join(answers)
		final_answer = "常见的儿科疾病有" + answers + "等。"
		print("查询答案为：" +"\n"+ final_answer)
		return final_answer


	# 39.某疾病的症状表现
	def get_baby_illness_symptom(self):
		## 获取疾病名称
		illness_name = self.get_name('nni')
		cql = f"match (p:常见疾病) where p.node_name='{illness_name}' return distinct p.symptom"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		# print(list(answer)[0][0])
		final_answer = illness_name + "的症状表现：" + str(list(answer)[0][0])
		print("查询答案为：" +"\n"+ final_answer)
		return final_answer

	# 40.某疾病的治疗方法
	def get_baby_illness_therapies(self):
		## 获取疾病名称
		illness_name = self.get_name('nni')
		cql = f"match (p:常见疾病) where p.node_name='{illness_name}' return distinct p.treatment"
		print("cql语句："+"\n"+cql)
		answer = self.graph.run(cql)
		# print(list(answer)[0][0])
		final_answer = illness_name + "的治疗方法：" + str(list(answer)[0][0])
		print("查询答案为：" +"\n"+ final_answer)
		return final_answer
