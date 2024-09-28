# -*- coding: utf-8 -*-
# 查询图数据库


from py2neo import Graph

class Query():
    def __init__(self):
        #搭建自己的本地数据库
        self.graph=Graph(host="localhost", port=7687, user="neo4j", password="285801438wq")
    # 运行cql语句
    def run(self,cql):
        find_rela = self.graph.run(cql)
        return find_rela