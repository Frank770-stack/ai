"""
crypto_bot.py
A beginner-friendly, heavily commented chatbot that recommends cryptocurrencies
based on simple, rule-based logic (profitability + sustainability).

How to run:
1. Save this file as crypto_bot.py
2. Open terminal in VS Code
3. Run: python crypto_bot.py


"""

# -----------------------
# 1) Data: mini crypto DB
# -----------------------
# This is our "dataset" — like a tiny database stored in memory.
# It's a Python dictionary (key -> value). Each key is the coin name, value is another dict.
# Note: expressions like 3/10 evaluate to 0.3 in Python (float).
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",        # possible values: "rising", "stable", "falling"
        "market_cap": "high",           # "high", "medium", "low"
        "energy_use": "high",           # "high", "medium", "low"
        "sustainability_score": 3/10    # number between 0.0 and 1.0 (3/10 = 0.3)
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# -----------------------
# 2) Helper functions
# -----------------------
# Breaking logic into functions makes the code easier to read and test.
# Each function below performs one small job and has comments explaining what it does.

def find_most_sustainable(db):
    """
    Return the coin name with the highest sustainability_score.
    - max(iterable, key=...) finds the element with the maximum key value.
    - key=lambda x: db[x]['sustainability_score'] tells max which value to compare.
    """
    # If db is empty this would raise an error, but for our assignment we always have data.
    return max(db, key=lambda coin: db[coin]["sustainability_score"])


def find_trending_coins(db):
    """
    Return a list of coin names that have price_trend == "rising".
    - This uses a list comprehension, similar to JS filter:
      [coin for coin, data in db.items() if data['price_trend'] == 'rising']
    """
    return [coin for coin, data in db.items() if data["price_trend"] == "rising"]


def recommend_long_term(db):
    """
    Recommend a coin for long-term growth using simple combined rules:
    - Prefer coins that are 'rising' AND have sustainability_score > 0.7 (i.e., > 7/10).
    - Returns the first match or None if none match the criteria.
    """
    # We iterate over the DB and pick coins that match both conditions.
    candidates = [
        coin for coin, data in db.items()
        if data["price_trend"] == "rising" and data["sustainability_score"] > 7/10
    ]
    # If our candidate list is empty, return None so caller can handle it.
    return candidates[0] if candidates else None


# -----------------------
# 3) Main chatbot loop
# -----------------------
# This is the interactive part. It loops forever until the user types "exit".
# input(prompt) pauses and waits for user typing and Enter.
# .lower() converts the input to lowercase so we can do case-insensitive checks.
def run_chatbot():
    # Print a friendly introduction. Change tone here if you want (funny, formal, etc).
    print(" Hi! I’m CryptoBuddy — your AI-powered financial sidekick!")
    print("Ask me about crypto trends, sustainability, or what to invest in.")
    print("Try: 'Which crypto is sustainable?', 'Which are trending?', 'Long-term growth?'\n")
    print("Type 'exit' to quit.\n")

    # The loop keeps the conversation going until the user types "exit".
    while True:
        # Get user input. Equivalent to JS: const userQuery = prompt(...).toLowerCase();
        user_query = input("You: ").strip().lower()  # .strip() removes extra spaces

        # If the user wants to quit, break out of the loop.
        if user_query == "exit":
            print("CryptoBuddy: Goodbye!  Remember, crypto is risky. Do your own research!")
            break  # exit the while loop -> program ends

        # ---------------------------------------
        # Now we check for keywords in the user query
        # to decide what the user is asking for.
        # This is very simple "keyword matching" NLP.
        # ---------------------------------------

        # 1) Sustainability questions
        if "sustain" in user_query or "eco" in user_query or "environment" in user_query:
            # We call our helper to find the most sustainable coin.
            best = find_most_sustainable(crypto_db)
            # Format a nice response. Use f-strings to insert variables into text.
            print(f"CryptoBuddy: I recommend {best}! It has the highest sustainability score in our dataset.")

        # 2) Trending / rising price questions
        elif "trend" in user_query or "trending" in user_query or "rising" in user_query:
            trending = find_trending_coins(crypto_db)
            if trending:
                # join() makes a single string from list items, separated by commas
                print(f"CryptoBuddy:These are trending right now: {', '.join(trending)}")
            else:
                print("CryptoBuddy:  No coins are trending up in our dataset.")

        # 3) Long-term growth questions (combining sustainability + trend)
        elif "long-term" in user_query or "long term" in user_query or "growth" in user_query:
            pick = recommend_long_term(crypto_db)
            if pick:
                print(f"CryptoBuddy:  For long-term growth, consider {pick}. It is rising and has strong sustainability.")
            else:
                # Friendly fallback if nothing matches strict long-term criteria
                print("CryptoBuddy: I don't see a perfect long-term pick right now. Cardano looks promising but consider more research.")

        # 4) Ask for help / examples
        elif "help" in user_query or "examples" in user_query or "what can you do" in user_query:
            print("CryptoBuddy: I can tell you which coins are sustainable, which are trending, or recommend for long-term growth.")
            print("Try asking: 'Which crypto is sustainable?', 'Which coins are trending?', or 'What should I buy for long-term growth?'")

        # 5) Catch-all fallback for unknown questions
        else:
            # We can't understand complex natural language yet. This is an opportunity to improve:
            print("CryptoBuddy:  I didn’t understand that. Try asking about 'sustainability', 'trending', or 'long-term growth'.")

# If this script is run directly (python crypto_bot.py), start the chatbot.
# This "if __name__ == '__main__':" is the standard Python idiom to allow
# importing functions from this file without starting the bot automatically.
if __name__ == "__main__":
    run_chatbot()
