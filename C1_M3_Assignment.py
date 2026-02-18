# ==========================================
# Pluto's Poetic Journey - Real Application
# ==========================================

import os


# ==========================================
# STEP 1: Read Article
# ==========================================

def read_article(news_article):
    try:
        with open("filename", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Error: Article file not found.")
        return ""


# ==========================================
# STEP 2: Extract Key Topics (Simple AI Simulation)
# ==========================================

def extract_key_topics(article_text):
    """
    Instead of using an LLM, we simulate topic extraction
    using keyword logic.
    """

    topics = []

    if "geological" in article_text.lower() or "surface" in article_text.lower():
        topics.append("Pluto's geological activity and features")

    if "new horizons" in article_text.lower():
        topics.append("New Horizons discoveries and mission impact")

    if "subaru" in article_text.lower() or "future" in article_text.lower():
        topics.append("Future exploration and telescope collaboration")

    # Ensure exactly 3 topics
    while len(topics) < 3:
        topics.append("Outer solar system exploration insights")

    return topics[:3]


# ==========================================
# STEP 3: Organize Topics with Usage Switch
# ==========================================

def build_topics_to_use(key_topics):
    topics_to_use = []

    for topic in key_topics:
        topics_to_use.append({
            "topic": topic,
            "to_use": True
        })

    return topics_to_use


# ==========================================
# STEP 4: Generate Poem (Local Generator)
# ==========================================

def generate_poem(topics_to_use):
    active_topics = [t["topic"] for t in topics_to_use if t["to_use"]]

    # Ensure we use only first 3 topics max
    active_topics = active_topics[:3]

    # Generate exactly 4 lines
    poem_lines = [
        f"Across the stars where silence grows,",
        f"{active_topics[0]} brightly shows,",
        f"{active_topics[1]} softly gleam,",
        f"{active_topics[2]} fuels the cosmic dream."
    ]

    return "\n".join(poem_lines)


# ==========================================
# STEP 5: Save Poem
# ==========================================

def save_to_file(contents_to_save, filename="poem.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(contents_to_save)


# ==========================================
# MAIN APPLICATION
# ==========================================

def main():

    print("🚀 Pluto's Poetic Journey 🚀")
    print("=" * 40)

    # 1️⃣ Read article
    article_path = "news_article.txt"

    if not os.path.exists(article_path):
        print("Please place 'news_article.txt' in this folder.")
        return

    article = read_article(article_path)
    print("\n📖 Article loaded successfully.")

    # 2️⃣ Extract topics
    key_topics = extract_key_topics(article)

    print("\n🔭 Extracted Key Topics:")
    for topic in key_topics:
        print("-", topic)

    # 3️⃣ Organize topics
    topics_to_use = build_topics_to_use(key_topics)

    # 4️⃣ Generate poem
    poem = generate_poem(topics_to_use)

    print("\n🖋 Generated Poem:\n")
    print(poem)

    # 5️⃣ Save poem
    save_to_file(poem)

    print("\n💾 Poem saved to 'poem.txt'")
    print("\nMission Accomplished! 🌌")


if __name__ == "__main__":
    main()


