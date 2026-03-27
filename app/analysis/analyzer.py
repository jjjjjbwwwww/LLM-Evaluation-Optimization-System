


class Analyzer:

    def analyze(self, scores):
        if scores["correctness"] < 0.6:
            return "问题：答案不准确，建议增强RAG"

        if scores["relevance"] < 0.6:
            return "问题：检索不相关，建议优化query"

        if scores["completeness"] < 0.6:
            return "问题：回答不完整，建议优化prompt"

        return "表现良好"