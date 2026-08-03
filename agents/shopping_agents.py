import json

from rag.retriever import RAGRetriever
from llm.openrouter import ask_openrouter


class ShoppingPlannerAgent:

    def __init__(self):

        self.rag = RAGRetriever()

    def plan(self, budget, goal):

        docs = self.rag.retrieve(goal)

        context = "\n\n".join(docs)

        prompt = f"""
You are a shopping planner.

Budget:
Rs.{budget}

Shopping Goal:
{goal}

Knowledge Base:
{context}

Create a shopping plan.

Return ONLY valid JSON.

Example:

{{
 "products":[
   {{
      "name":"Rice",
      "price":250
   }}
 ],
 "estimated_total":250,
 "reason":"..."
}}
"""

        answer = ask_openrouter(prompt)

        try:
            return json.loads(answer)

        except:

            return {
                "products": [],
                "estimated_total": 0,
                "reason": answer
            }