import random

def get_input(prompt):
    """Get user input with validation"""
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Please enter something!")

def play_mad_libs():
    """Main game function"""
    print("\n" + "="*50)
    print("🎭 WELCOME TO MAD LIBS GAME! 🎭")
    print("="*50 + "\n")

    # Story templates
    stories = [
        {
            "title": "The Adventure",
            "template": """Yesterday, I went to the {place} with my {adjective} {noun}.
We {verb}ed all day long! Then we saw a {animal} wearing {clothing}.
It was so {emotion} that we {verb2}ed all the way home.""",
            "words": ["place", "adjective", "noun", "verb", "animal", "clothing", "emotion", "verb2"]
        },
        {
            "title": "The Restaurant",
            "template": """I went to a {adjective} restaurant called '{name}'.
The waiter was a {animal} who served me {food} on a {noun}.
I {verb}ed so much that I became {emotion} and had to {verb2} out of there!""",
            "words": ["adjective", "name", "animal", "food", "noun", "verb", "emotion", "verb2"]
        },
        {
            "title": "The Dream",
            "template": """Last night I dreamed I was a {adjective} {noun} who could {verb}.
I flew to {place} where I met a {animal} who gave me {food}.
We {verb2}ed together until I woke up feeling {emotion}.""",
            "words": ["adjective", "noun", "verb", "place", "animal", "food", "verb2", "emotion"]
        },
        {
            "title": "The Superhero",
            "template": """My superhero name is {name} Man/Woman!
I have the power to {verb} {noun}s faster than a {animal}.
I wear a {adjective} {clothing} and when I get {emotion},
I {verb2} all the way to {place}.""",
            "words": ["name", "verb", "noun", "animal", "adjective", "clothing", "emotion", "verb2", "place"]
        },
        {
            "title": "The Time Machine",
            "template": """I built a time machine out of a {adjective} {noun}!
When I {verb}ed it, I went to {place} where {animal}s rule the world.
They served me {food} and made me wear {clothing}.
I felt so {emotion} that I {verb2}ed back home immediately.""",
            "words": ["adjective", "noun", "verb", "place", "animal", "food", "clothing", "emotion", "verb2"]
        }
    ]

    while True:
        print("\nChoose a story:")
        for i, story in enumerate(stories, 1):
            print(f"{i}. {story['title']}")
        print(f"{len(stories) + 1}. Random Story")
        print(f"{len(stories) + 2}. Exit")

        try:
            choice = int(get_input("\nEnter your choice (1-{}): ".format(len(stories) + 2)))

            if choice == len(stories) + 2:
                print("\nThanks for playing! Goodbye! 👋\n")
                break
            elif choice == len(stories) + 1:
                selected_story = random.choice(stories)
            elif 1 <= choice <= len(stories):
                selected_story = stories[choice - 1]
            else:
                print("Invalid choice! Please try again.")
                continue

            print(f"\n📝 You've chosen: {selected_story['title']}")
            print("Please provide the following words:\n")

            # Collect words
            words = {}
            for word_type in selected_story['words']:
                if word_type == 'verb':
                    words[word_type] = get_input(f"Enter a {word_type} (base form, e.g., 'run' not 'running'): ")
                elif word_type == 'verb2':
                    words[word_type] = get_input(f"Enter another {word_type.replace('2', '')} (base form): ")
                else:
                    words[word_type] = get_input(f"Enter a {word_type}: ")

            # Generate story
            print("\n" + "="*60)
            print("🎉 HERE'S YOUR MAD LIB! 🎉")
            print("="*60 + "\n")

            story = selected_story["template"].format(**words)
            print(story)

            print("\n" + "="*60)

            # Ask if they want to play again
            play_again = get_input("\nWould you like to play again? (yes/no): ").lower()
            if play_again not in ['yes', 'y']:
                print("\nThanks for playing! Goodbye! 👋\n")
                break

        except ValueError:
            print("Please enter a valid number!")

def quick_mad_lib():
    """Quick single story version"""
    print("\n🎭 QUICK MAD LIB 🎭\n")

    story_template = """I went to the {place} with a {adjective} {noun}.
Suddenly, a {animal} appeared and started to {verb}!
I was so {emotion} that I {verb2}ed all the way home!"""

    words_needed = ['place', 'adjective', 'noun', 'animal', 'verb', 'emotion', 'verb2']

    words = {}
    for word in words_needed:
        words[word] = input(f"Enter a {word}: ")

    print("\n🎉 Your Mad Lib:")
    print(story_template.format(**words))

if __name__ == "__main__":
    print("Choose mode:")
    print("1. Full Game")
    print("2. Quick Game")

    mode = input("Enter choice (1 or 2): ")

    if mode == "1":
        play_mad_libs()
    else:
        quick_mad_lib()