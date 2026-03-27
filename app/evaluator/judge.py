


from langchain_openai import ChatOpenAI

class LLMJudge:

    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-3.5-turbo")

    def evaluate(self, query, answer):
        prompt = f"""
请评估以下回答质量：

问题：{query}
回答：{answer}

从以下维度打分（0-1）：
1. 正确性
2. 相关性
3. 完整性

输出格式：
correctness: x
relevance: x
completeness: x
"""
        res = self.llm.invoke(prompt).content
        return res