import json

from llm.groq import ask_groq


class BudgetAdvisorAgent:

    def analyze(self, shopping_plan):

        prompt = f"""
You are a budget advisor.

Shopping Plan:

{json.dumps(shopping_plan, indent=2)}

Tasks:

1. Check if the shopping plan fits the budget.
2. Suggest cheaper alternatives if needed.
3. Recommend ways to save money.

Return ONLY valid JSON using this format:

{{
    "status":"Within Budget",
    "total":1380,
    "remaining":3620,
    "saving_tips":[
        "...",
        "..."
    ],
    "alternatives":[
        "...",
        "..."
    ]
}}
"""

        answer = ask_groq(prompt)

        try:
            return json.loads(answer)

        except:

            return {
                "status": "Unknown",
                "total": shopping_plan["estimated_total"],
                "remaining": 0,
                "saving_tips": [],
                "alternatives": [],
                "raw": answer
            }