from agents.shopping_agents import ShoppingPlannerAgent
from agents.budget_agents import BudgetAdvisorAgent


class Orchestrator:

    def __init__(self):

        self.shopping_agent = ShoppingPlannerAgent()

        self.budget_agent = BudgetAdvisorAgent()

    def process(self, budget, goal):

        # Step 1
        shopping_plan = self.shopping_agent.plan(
            budget,
            goal
        )

        # Add budget and goal to message
        shopping_plan["budget"] = budget
        shopping_plan["shopping_goal"] = goal

        # Step 2
        budget_analysis = self.budget_agent.analyze(
            shopping_plan
        )

        return {
            "shopping_plan": shopping_plan,
            "budget_analysis": budget_analysis
        }