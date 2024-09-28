import sys
sys.path.append('/home/pi/django/knowledgeApp/neodb')
from config import graph,CA_LIST

def query(name):
	data = graph.run(
		"match(p )-[r]->(n{node_name:'%s'}) return  p.node_name,r.relationships,n.node_name,p.node_cate,n.node_cate\
			Union all\
		match(p{node_name:'%s'}) -[r]->(n) return p.node_name,r.relationships,n.node_name,p.node_cate,n.node_cate" % (name, name)
	)
	data = list(data)
	return get_json_data(data)


def get_json_data(data):
	json_data = {'data': [], "links": []}#json字典包含data节点元素列表和links边元素列表
	d = []

	for i in data:#将查询的数据以"_"进行拼接
		# print(i["p.Name"], i["r.relation"], i["n.Name"], i["p.cate"], i["n.cate"])
		d.append(i['p.node_name'] + "_" + i['p.node_cate'])#以查询的节点作为头节点
		d.append(i['n.node_name'] + "_" + i['n.node_cate'])#以查询的节点作为尾节点
		d = list(set(d))
	name_dict = {}
	count = 0
	for j in d:#json字典中data节点元素列表填充数据
		j_array = j.split("_")

		data_item = {}
		name_dict[j_array[0]] = count
		count += 1
		data_item['name'] = j_array[0]#关联的节点名
		data_item['category'] = CA_LIST[j_array[1]]#预定义的实体类别列表元素
		json_data['data'].append(data_item)
	for i in data:
		link_item = {}

		link_item['source'] = name_dict[i['p.node_name']]#头节点，可以当作源头节点

		link_item['target'] = name_dict[i['n.node_name']]#尾节点，可以当作目标节点
		link_item['value'] = i['r.relationships']#两节点间关系
		json_data['links'].append(link_item)

	return json_data


# f = codecs.open('./static/test_data.json','w','utf-8')
# f.write(json.dumps(json_data,  ensure_ascii=False))



