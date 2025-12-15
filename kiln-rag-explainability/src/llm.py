
# src/llm.py
# Placeholder LLM response builder. Replace with Azure/OpenAI calls.

def answer_with_rules(question: str, contexts: list[str]) -> str:
    guidance = (
        "Answer only using provided context. "
        "Prioritize safety: recommend lowering setpoint deviations, checking airflow dampers, inspecting refractory wear."
    )
    return guidance + "

Q: " + question + "
A: " + " ".join(contexts)[:800]
