


class Optimizer:

    def suggest(self, analysis):
        if "RAG" in analysis:
            return "增加检索数据或使用rerank"

        if "query" in analysis:
            return "引入query rewrite"

        if "prompt" in analysis:
            return "增加约束提示"

        return "无需优化"