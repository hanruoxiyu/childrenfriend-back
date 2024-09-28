# -*- coding: utf-8 -*-
import sys
sys.path.append('/home/pi/django/knowledgeApp/neodb')
from config import graph


def query_table(name):
	data = graph.run(
		"match(p )-[r]->(n{node_name:'%s'}) return  p.node_name,r.relationships,n.node_name,p.node_cate,n.node_cate\
			Union all\
		match(p{node_name:'%s'}) -[r]->(n) return p.node_name,r.relationships,n.node_name,p.node_cate,n.node_cate" % (
			name, name)
	)
	data = list(data)
	# print(data)
	return data


def get_list_data(data):
	data_list = []
	for i in data:
		dt = {}
		# print(i["n.node_cate"], i["n.node_name"])
		dt["关联属性"] = i["r.relationships"]
		dt["关联节点"] = i["n.node_name"]
		# print(dt)
		data_list.append(dt)
	# print(str(data_list))
	return data_list


def get_table_data(name):
	data = query_table(name)
	data_list = get_list_data(data)
	#print(str(data_list))
	return data_list

	#f = codecs.open('./static/table_data.txt', 'w', encoding='UTF-8')
	#f.seek(0)
	#f.truncate()  # 清空文件
	#f.write(str(data_list))


# get_table_data("婴儿")
