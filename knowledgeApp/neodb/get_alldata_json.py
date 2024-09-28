# -*- coding: utf-8 -*-
import codecs
import json
import sys
sys.path.append('/home/pi/django/knowledgeApp/neodb')
from config import graph



def query():
	data = graph.run(
		"match(p )-[r]->(n) return  p.node_name,r.relationships,n.node_name,p.node_cate,n.node_cate"
	)
	data = list(data)
	return data


def get_json_data(data):
	json_data = {'data': [], "links": []}
	d = []

	for i in data:
		# print(i["p.Name"], i["r.relation"], i["n.Name"], i["p.cate"], i["n.cate"])
		d.append(i['p.node_name'] + "_" + i['p.node_cate'])
		d.append(i['n.node_name'] + "_" + i['n.node_cate'])
		d = list(set(d))
	name_dict = {}
	count = 0
	for j in d:
		j_array = j.split("_")

		data_item = {}
		name_dict[j_array[0]] = count
		count += 1
		data_item['name'] = j_array[0]
		data_item['category'] = CA_LIST[j_array[1]]
		json_data['data'].append(data_item)
	for i in data:
		link_item = {}

		link_item['source'] = name_dict[i['p.node_name']]

		link_item['target'] = name_dict[i['n.node_name']]
		link_item['value'] = i['r.relationships']
		json_data['links'].append(link_item)

	return json_data

def get_alldata():
	data = query()
	json_data = get_json_data(data)
	# f = codecs.open('./static/data/all_data.json', 'w', encoding='UTF-8')
	# f.seek(0)
	# f.truncate()  # 清空文件
	# f.write(json.dumps(json_data, ensure_ascii=False))
	return json_data

