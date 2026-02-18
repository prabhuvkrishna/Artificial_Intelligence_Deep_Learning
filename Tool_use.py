import os
from dotenv import load_dotenv
import aisuite as ai


# --------------------------------------------------
# Setup
# --------------------------------------------------

load_dotenv()  # Loads OPENAI_API_KEY from .env

CLIENT = ai.Client()


# --------------------------------------------------
# Step 1 – Generate Draft
# --------------------------------------------------

def generate_draft(topic: str, model: str = "openai:gpt-4o") -> str:
    prompt = f"""
    Write a well-structured, factual, and balanced essay on the following topic:

    "{topic}"

    The essay should:
    - Have a clear introduction, body, and conclusion
    - Present logical arguments
    - Maintain a formal tone
    """

    response = CLIENT.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content


# --------------------------------------------------
# Step 2 – Reflect on Draft
# --------------------------------------------------

def reflect_on_draft(draft: str, model: str = "openai:o4-mini") -> str:
    prompt = f"""
    Review the following essay draft and provide constructive feedback.

    Focus on:
    - Structure
    - Clarity
    - Strength of argument
    - Writing style
    - Logical coherence

    Be critical but professional.

    Essay:
    {draft}
    """

    response = CLIENT.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content


# --------------------------------------------------
# Step 3 – Revise Draft
# --------------------------------------------------

def revise_draft(original_draft: str, reflection: str, model: str = "openai:gpt-4o") -> str:
    prompt = f"""
    Revise the following essay using the provided feedback.

    Ensure:
    - Improved clarity
    - Better structure
    - Stronger arguments
    - Smoother flow
    - Professional tone

    Original Draft:
    {original_draft}

    Feedback:
    {reflection}

    Return only the improved essay.
    """

    response = CLIENT.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content


# --------------------------------------------------
# Main Workflow
# --------------------------------------------------

def main():
    topic = input("Enter essay topic: ")

    print("\n📝 Generating Draft...\n")
    draft = generate_draft(topic)
    print(draft)

    print("\n🧠 Reflecting on Draft...\n")
    feedback = reflect_on_draft(draft)
    print(feedback)

    print("\n✍️ Revising Draft...\n")
    revised = revise_draft(draft, feedback)
    print(revised)


if __name__ == "__main__":
    main()
