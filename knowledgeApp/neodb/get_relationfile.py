# -*- coding: utf-8 -*-
import sys
sys.path.append('/home/pi/django/knowledgeApp/neodb')
from config import graph
def query():
	data = graph.run(
		"match(p )-[r]->(n) return  p.node_name,n.node_name,r.relationships,p.node_cate,n.node_cate"
	)
	data = list(data)
	return data
data=query()
with open('../raw_data/relation.txt', 'a',encoding='UTF-8') as month_file:
    for tag in data:
        for i in tag:
            month_file.write(str(i))
            month_file.write(',')
        month_file.write('\n')