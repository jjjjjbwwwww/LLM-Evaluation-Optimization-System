LLM Evaluation & Optimization System

一个模块化的 AI 评估与优化系统，支持对大模型回答进行自动评分、问题分析和优化建议生成。

 项目简介

本项目实现了一个完整的 LLM 评估闭环：

Query + Answer
        ↓
LLM Judge（评分）
        ↓
Score Parser（解析）
        ↓
Metrics（统计）
        ↓
Analyzer（问题诊断）
        ↓
Optimizer（优化建议）
        ↓
Logger（日志记录）

 可用于：

RAG系统评估
Prompt优化分析
LLM回答质量监控
 核心功能
1️⃣ 自动评分（LLM Judge）
correctness（正确性）
relevance（相关性）
completeness（完整性）
2️⃣ 问题分析（Analyzer）

自动识别问题类型：

答案不准确
检索不相关
回答不完整
3️⃣ 优化建议（Optimizer）

根据问题自动生成建议：

增强 RAG
Query Rewrite
Prompt 优化
4️⃣ 日志系统（Logger）

记录每次评估结果：

{
  "query": "...",
  "answer": "...",
  "scores": {...},
  "analysis": "...",
  "suggestion": "..."
}
 
 Project Structure
llm_eval_system/
│
├── app/
│   ├── core/           # Evaluation pipeline
│   ├── evaluator/      # LLM judging & scoring
│   ├── analysis/       # Issue detection
│   ├── optimizer/      # Optimization logic
│   ├── storage/        # Logging system
│   └── main.py         # FastAPI entrypoint
│
├── data/
│   └── logs.json
│
├── README.md
└── pyproject.toml
 
 

 安装与运行
1️⃣ 创建环境
pip install fastapi uvicorn
2️⃣ 启动服务
uvicorn app.main:app --reload
3️⃣ 打开接口文档
http://127.0.0.1:8000/docs
🧪 示例请求
GET /eval
/eval?query=苹果市值是多少&answer=苹果市值1万亿美元
 关于 OpenAI API

默认使用 LLM 进行评分，如无 API Key 可使用 Mock：

def evaluate(self, query, answer):
    return '''
    correctness: 0.7
    relevance: 0.8
    completeness: 0.6
    '''
 后续优化方向

多维度评估（Hallucination检测）

自动 Prompt 优化（Agent）

RAG 自动调参

前端可视化界面

Docker 部署
