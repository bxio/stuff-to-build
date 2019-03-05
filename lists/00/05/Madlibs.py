# No solution due to missing information
prompts = ["exclamation", "adverb", "noun", "adjective"]
responses = []

for prompt in prompts:
    responses.append(input(f"Enter a {prompt}:"))

print (f"{responses[0]}! he said {responses[1]} as he jumped into his convertible {responses[2]} and drove off with his {responses[3]} wife.")
