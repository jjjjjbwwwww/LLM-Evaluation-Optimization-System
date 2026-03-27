

from app.evaluator.judge import LLMJudge
from app.evaluator.scorer import parse_score
from app.evaluator.metrics import Metrics
from app.storage.logger import Logger
from app.analysis.analyzer import Analyzer
from app.optimizer.optimizer import Optimizer

class EvalPipeline:

    def __init__(self):
        self.judge = LLMJudge()
        self.metrics = Metrics()
        self.logger = Logger()
        self.analyzer = Analyzer()
        self.optimizer = Optimizer()

    def run(self, query, answer):
        # 1. 评估
        raw = self.judge.evaluate(query, answer)

        # 2. 解析
        scores = parse_score(raw)

        # 3. 统计
        self.metrics.add(scores)

        # 4. 分析
        analysis = self.analyzer.analyze(scores)

        # 5. 优化建议
        suggestion = self.optimizer.suggest(analysis)

        # 6. 日志
        self.logger.log({
            "query": query,
            "answer": answer,
            "scores": scores,
            "analysis": analysis,
            "suggestion": suggestion
        })

        return {
            "scores": scores,
            "analysis": analysis,
            "suggestion": suggestion
        }