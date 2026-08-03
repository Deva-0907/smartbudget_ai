import streamlit as st
from dotenv import load_dotenv
import os
from agents.orchestrator import Orchestrator

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="🛒 SmartShop AI",
    page_icon="🛒",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title(" Configuration")

    groq_available = bool(os.getenv("GROQ_API_KEY"))
    openrouter_available = bool(os.getenv("OPENROUTER_API_KEY"))

    st.subheader("API Status")

    st.write(f"Groq: {'✅ Connected' if groq_available else '❌ Missing'}")
    st.write(f"OpenRouter: {'✅ Connected' if openrouter_available else '❌ Missing'}")

# Main Page
st.title(" SmartShop AI")
st.subheader("Agentic Shopping & Budget Assistant")

st.markdown("---")

budget = st.number_input(
    "Enter Your Budget (LKR)",
    min_value=100,
    value=5000,
    step=100
)

shopping_goal = st.text_input(
    " What do you want to buy?",
    placeholder="Example: Weekly groceries for 4 people"
)
from agents.orchestrator import Orchestrator

orchestrator = Orchestrator()

if st.button(" Generate Shopping Plan"):

    if shopping_goal.strip() == "":
        st.warning("Please enter your shopping goal.")

    else:

        with st.spinner(" AI Agents are working..."):

            result = orchestrator.process(
                budget,
                shopping_goal
            )

        shopping = result["shopping_plan"]
        analysis = result["budget_analysis"]

        st.success("Shopping Plan Generated!")

        st.subheader("🛒 Shopping Plan")

        for product in shopping["products"]:
            st.write(
                f"{product['name']} - Rs.{product['price']}"
            )

        st.subheader(" Budget Analysis")

        st.json(analysis)

        st.write("Budget:", budget)
        st.write("Goal:", shopping_goal)

        st.info(" Shopping Planner Agent will be added in the next step.")