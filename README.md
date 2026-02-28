🧠 AI Resume Shortlisting & Interview Assistant System
📌 Overview

This project implements an AI-powered resume screening and evaluation system that goes beyond keyword matching.
It uses Large Language Models (LLMs) to simulate human recruiter judgment across multiple stages of candidate evaluation.

The system evaluates candidates on:

Semantic Role Fit (Screening)

Achievement / Impact

Ownership / Responsibility

Holistic Hiring Decision (Tiering)

The goal is to produce explainable, nuanced, and realistic hiring decisions rather than binary accept/reject outcomes.

🎯 Key Features

✅ LLM-based Screening (JD ↔ Resume semantic fit)

✅ LLM-based Achievement Evaluation

✅ LLM-based Ownership Evaluation

✅ LLM-based Final Hiring Decision

✅ Explainable outputs at every stage

✅ Free & fast inference using Groq API

✅ Modular, production-style architecture

🏗️ System Architecture
Resume + Job Description
        │
        ▼
LLM Screening (Semantic Fit)
        │
        ▼
LLM Achievement Evaluation
        │
        ▼
LLM Ownership Evaluation
        │
        ▼
LLM Holistic Decision Engine
        │
        ▼
Final Tier + Hiring Action + Explanation

Design principle:
Deterministic logic computes structure; LLMs handle qualitative judgment where human reasoning is required.

🔍 Evaluation Dimensions
1️⃣ LLM Screening (Semantic Similarity)

Purpose:
Evaluate whether a resume is a reasonable fit for a role even if exact skills don’t match.

Handled by: Groq-hosted LLaMA-3 model
Output:

{
  "score": 75,
  "reason": "Strong semantic alignment with minor gaps"
}

Why LLM?
Keyword matching fails on transferable skills (e.g., Kafka ↔ Kinesis).
LLMs understand context and equivalence.

2️⃣ LLM Achievement Scoring

Purpose:
Judge real-world impact, not just listed tasks.

Scoring rubric:

Score Range	Meaning
0–20	No real impact
21–40	Task-level work
41–60	Solid individual contribution
61–80	High-impact, system-level work
81–100	Exceptional, org-wide impact

Example output:

{
  "score": 70,
  "reason": "System-level impact with cross-team usage"
}
3️⃣ LLM Ownership Scoring

Purpose:
Determine depth of responsibility.

Evaluates whether the candidate:

Designed vs assisted

Owned decisions

Led or executed independently

4️⃣ LLM Holistic Decision Engine (Final)

Instead of hardcoded thresholds or static weights, the system uses an LLM as a final reasoning layer.

Inputs:

Similarity score + explanation

Achievement score + explanation

Ownership score + explanation

Job context

Output:

{
  "tier": "Tier B",
  "decision": "Conditional Offer",
  "reason": "Strong impact and ownership with partial role mismatch"
}

This mirrors how real hiring managers make decisions.

🏷️ Tiering Logic (Conceptual)
Tier	Meaning
Tier A	Fast-track candidate
Tier B	Technical interview / conditional offer
Tier C	Not suitable for this role

⚠️ Tiering is not numeric threshold-based — it is LLM-reasoned.

🤖 Why Groq + LLaMA-3?

✅ Free API tier

✅ Very low latency

✅ No local GPU required

✅ Open-weight models

✅ Strong reasoning performance

Model used:

llama-3.1-8b-instant

The system is model-agnostic and can be swapped with other providers if needed.

🧩 Tech Stack

Language: Python 3.11

LLM Provider: Groq API

Model: LLaMA-3 (8B Instant)

Architecture: Modular, LLM-as-Judge

Environment: Virtualenv / venv

▶️ How to Run
1️⃣ Clone the repository
git clone <repo-url>
cd ai-resume-evaluator
2️⃣ Create & activate virtual environment
python -m venv venv
source venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Set Groq API key
export GROQ_API_KEY="your_api_key_here"
5️⃣ Run the system
python main.py
📤 Sample Output
--- LLM SCREENING ---
Score: 75
Reason: Strong semantic alignment with minor gaps

--- LLM ACHIEVEMENT ---
Score: 70
Reason: High-impact system-level contributions

--- FINAL AI DECISION ---
Tier: Tier B
Decision: Conditional Offer
Reason: Strong impact and ownership with partial role mismatch
🧠 Design Decisions & Justification
Why LLMs instead of rules?

Hiring decisions are qualitative

Rules fail on nuance

LLMs approximate human judgment

Why not train a model?

No labeled hiring data

LLMs provide zero-shot reasoning

Why not embeddings only?

Embeddings score similarity, not suitability

LLMs reason about context, impact, and trade-offs

🚀 Future Enhancements

LLM-generated interview questions

Confidence and risk flags

Batch resume processing

UI (Streamlit / React)

Hybrid embedding + LLM optimization

✅ Final Summary

This system demonstrates how LLMs can be integrated responsibly into hiring workflows by reasoning over structured signals, producing explainable decisions, and avoiding brittle rule-based logic.