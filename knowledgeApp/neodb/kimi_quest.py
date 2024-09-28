import requests

class kimi():
    @staticmethod
    def query_fun(content):
        # 设置请求的URL
        url = "http://localhost:8000/v1/chat/completions"

        # 设置请求头
        headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1c2VyLWNlbnRlciIsImV4cCI6MTcyMTM4ODIxOCwiaWF0IjoxNzEzNjEyMjE4LCJqdGkiOiJjb2hxYmVoa3FxNHUwNDE2Z3RnMCIsInR5cCI6InJlZnJlc2giLCJzdWIiOiJjb2hxYmVoa3FxNHUwNDE2Z3RmMCIsInNwYWNlX2lkIjoiY29ocWJlaGtxcTR1MDQxNmd0ZWciLCJhYnN0cmFjdF91c2VyX2lkIjoiY29ocWJlaGtxcTR1MDQxNmd0ZTAifQ.x88TekoksoNC8FTRMfFoKGvUs6xLPo-CQe50smsrV8DHalA41b0AcRAxJT03jviW-LkbEdeUGNyCnVKktzULiw",
            "Content-Type": "application/json"
        }

        # 设置请求体
        data = {
            "model": "kimi",
            "messages": [
                {
                    "role": "user",
                    "content": content
                }
            ],
            "use_search": True,
            "stream": False
        }

        # 发送POST请求
        response = requests.post(url, json=data, headers=headers)

        # 解析 JSON 数据
        response_json = response.json()

        # 获取 "content" 的值
        content_value = response_json["choices"][0]["message"]["content"]

        return content_value
