"""
Reflective Writing Agent Application

This script:
1. Generates an essay draft
2. Reflects on the draft
3. Revises the draft using feedback
"""

import os
from dotenv import load_dotenv
import aisuite as ai


# -----------------------------
# Initialize Client
# -----------------------------

load_dotenv()

CLIENT = ai.Client()


# -----------------------------
# Step 1 – Generate Draft
# -----------------------------

def generate_draft(topic: str, model: str = "openai:gpt-4o") -> str:
    """
    Generate an initial essay draft for a given topic.
    """

    prompt = f"""
    Write a well-structured essay on the following topic:

    "{topic}"

    The essay should:
    - Have a clear introduction, body, and conclusion
    - Present balanced arguments
    - Maintain a formal and factual tone
    """

    response = CLIENT.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content


# -----------------------------
# Step 2 – Reflect on Draft
# -----------------------------

def reflect_on_draft(draft: str, model: str = "openai:o4-mini") -> str:
    """
    Provide constructive feedback on the essay draft.
    """

    prompt = f"""
    Review the following essay draft and provide constructive criticism.

    Focus on:
    - Structure and organization
    - Clarity and coherence
    - Strength of arguments
    - Writing style and tone

    Be critical but constructive.

    Essay Draft:
    {draft}
    """

    response = CLIENT.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content


# -----------------------------
# Step 3 – Revise Draft
# -----------------------------

def revise_draft(original_draft: str, reflection: str, model: str = "openai:gpt-4o") -> str:
    """
    Revise the essay using feedback from reflection.
    """

    prompt = f"""
    You are given an original essay draft and feedback on it.

    Improve the essay by addressing all issues mentioned in the feedback.
    Enhance clarity, structure, argument strength, and flow.

    Original Draft:
    {original_draft}

    Feedback:
    {reflection}

    Return ONLY the fully revised essay.
    """

    response = CLIENT.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content


# -----------------------------
# Main Application Runner
# -----------------------------

def main():
    print("\n=== Reflective Writing Agent ===\n")

    topic = input("Enter essay topic: ")

    print("\nGenerating draft...\n")
    draft = generate_draft(topic)
    print("----- Draft -----\n")
    print(draft)

    print("\nReflecting on draft...\n")
    feedback = reflect_on_draft(draft)
    print("----- Feedback -----\n")
    print(feedback)

    print("\nRevising draft...\n")
    revised = revise_draft(draft, feedback)
    print("----- Revised Essay -----\n")
    print(revised)


if __name__ == "__main__":
    main()


