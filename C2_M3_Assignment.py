"""
Agentic Research Application
Clean Python version (Notebook + Grader removed)
"""

from datetime import datetime
import json
import re
import ast
from aisuite import Client
import research_tools


# ==================================================
# Initialize shared client
# ==================================================
CLIENT = Client()


# ==================================================
# Planner Agent
# ==================================================
def planner_agent(topic: str, model: str = "openai:o4-mini") -> list[str]:

    user_prompt = f"""
    You are a planning agent responsible for organizing a research workflow
    using the following agents:

    - research_agent
    - writer_agent
    - editor_agent

    Return ONLY a valid Python list of steps (strings).
    Final step must generate a Markdown research report.

    Topic: "{topic}"
    """

    response = CLIENT.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": user_prompt}],
        temperature=1,
    )

    steps_str = response.choices[0].message.content.strip()
    return ast.literal_eval(steps_str)


# ==================================================
# Research Agent
# ==================================================
def research_agent(task: str, model: str = "openai:gpt-4o"):

    current_time = datetime.now().strftime("%Y-%m-%d")

    prompt = f"""
    You are a research assistant.

    Available tools:
    - arxiv_search_tool
    - tavily_search_tool
    - wikipedia_search_tool

    Current date: {current_time}

    Task:
    {task}
    """

    tools = [
        research_tools.arxiv_search_tool,
        research_tools.tavily_search_tool,
        research_tools.wikipedia_search_tool,
    ]

    response = CLIENT.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        tools=tools,
        tool_choice="auto",
        max_turns=6,
    )

    return response.choices[0].message.content


# ==================================================
# Writer Agent
# ==================================================
def writer_agent(task: str, model: str = "openai:gpt-4o") -> str:

    system_prompt = """
    You are a professional academic writing agent.
    Produce structured, formal, technical writing.
    Avoid conversational tone.
    """

    response = CLIENT.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": task},
        ],
        temperature=1.0,
    )

    return response.choices[0].message.content


# ==================================================
# Editor Agent
# ==================================================
def editor_agent(task: str, model: str = "openai:gpt-4o") -> str:

    system_prompt = """
    You are a professional editor.
    Reflect, critique, and improve drafts.
    Maintain academic tone and clarity.
    """

    response = CLIENT.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": task},
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content


# ==================================================
# Executor Agent (Orchestrator)
# ==================================================
def clean_json_block(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\n?", "", raw)
        raw = re.sub(r"\n?```$", "", raw)
    return raw.strip()


def executor_agent(topic: str, model: str = "openai:gpt-4o"):

    plan_steps = planner_agent(topic)
    history = []

    agent_registry = {
        "research_agent": research_agent,
        "writer_agent": writer_agent,
        "editor_agent": editor_agent,
    }

    for step in plan_steps[:4]:  # limit to 4 steps for runtime control

        decision_prompt = f"""
        Identify which agent should execute this instruction.
        Return JSON with:
        - agent
        - task

        Instruction: "{step}"
        """

        decision = CLIENT.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": decision_prompt}],
            temperature=0,
        )

        agent_info = json.loads(
            clean_json_block(decision.choices[0].message.content)
        )

        agent_name = agent_info["agent"]
        task = agent_info["task"]

        context = "\n".join(
            [f"{a}: {r}" for _, a, r in history]
        )

        enriched_task = f"""
        Context so far:
        {context}

        Task:
        {task}
        """

        if agent_name in agent_registry:
            output = agent_registry[agent_name](enriched_task)
        else:
            output = f"Unknown agent: {agent_name}"

        history.append((step, agent_name, output))

    return history


# ==================================================
# Main Entry Point
# ==================================================
if __name__ == "__main__":

    topic = "The ensemble Kalman filter for time series forecasting"

    print("\n🚀 Running Agentic Research Workflow...\n")

    results = executor_agent(topic)

    print("\n================ FINAL OUTPUT ================\n")
    print(results[-1][2])
