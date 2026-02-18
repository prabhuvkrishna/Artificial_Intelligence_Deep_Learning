import csv
import statistics as stats
from openai import OpenAI

# ===============================
# Candy Analysis Application 🍭
# ===============================

print("🍬 DeepLearning.AI Sugar Rush Delights 🍬")
print("=" * 50)


# -------------------------------
# Step 1: Read Candy Data
# -------------------------------
def read_candy_data(candy_data):
    with open("filename", newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


# -------------------------------
# Step 2: Extract Popularity Scores
# -------------------------------
def get_popularity_scores(candy_data):
    return [int(candy["Popularity Score"]) for candy in candy_data]


# -------------------------------
# Step 3: Find Top Candies
# -------------------------------
def get_top_candies(candy_data, avg_popularity):
    return [
        candy for candy in candy_data
        if int(candy["Popularity Score"]) >= avg_popularity
    ]


# -------------------------------
# Step 4: Pretty Print Table
# -------------------------------
def display_pretty_table(candies):
    print("\n🏆 Top Candy Leaderboard 🏆")
    print("+-------------------------------+------------------+--------------+")
    print("| Candy Name                    | Popularity Score | Price in USD |")
    print("+-------------------------------+------------------+--------------+")

    for candy in candies:
        print(
            f"| {candy['Candy Name']:<29} | "
            f"{candy['Popularity Score']:^16} | "
            f"{candy['Price in USD']:^12} |"
        )

    print("+-------------------------------+------------------+--------------+")


# -------------------------------
# Step 5: LLM Description Generator
# -------------------------------
client = OpenAI()  # Requires OPENAI_API_KEY set in environment

def get_llm_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an energetic candy marketing expert.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )
    return completion.choices[0].message.content


# -------------------------------
# MAIN PROGRAM
# -------------------------------
def main():

    # Load data
    candy_data = read_candy_data("candy_data.csv")

    # Show raw data
    print("\n📊 Candy Data Loaded Successfully!")

    # Extract popularity scores
    popularity_scores = get_popularity_scores(candy_data)

    # Calculate average
    avg_popularity = stats.mean(popularity_scores)
    print(f"\n🎯 Average Popularity Score: {avg_popularity:.2f}")

    # Get top candies
    top_candies = get_top_candies(candy_data, avg_popularity)

    # Display leaderboard
    display_pretty_table(top_candies)

    # Generate descriptions
    print("\n📝 Marketing Descriptions\n")
    for candy in top_candies:
        prompt = f"""
        For the candy named {candy['Candy Name']},
        write a short, catchy two-sentence marketing description.
        """

        response = get_llm_response(prompt)

        print(f"NAME: {candy['Candy Name']}")
        print(f"DESCRIPTION: {response}")
        print("-" * 50)


if __name__ == "__main__":
    main()
