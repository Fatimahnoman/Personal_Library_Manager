# Mad Libs Demo - Shows how the game works

def demo_mad_lib():
    print("MAD LIBS DEMO")
    print("=" * 30)
    print("This is how the game works:\n")

    # Pre-filled example
    words = {
        'place': 'moon',
        'adjective': 'purple',
        'noun': 'banana',
        'animal': 'giraffe',
        'verb': 'dance',
        'emotion': 'excited',
        'verb2': 'sing',
        'food': 'pizza',
        'clothing': 'tuxedo',
        'name': 'Captain'
    }

    story_template = """Yesterday, I went to the {place} with my {adjective} {noun}.
We {verb}ed all day long! Then we saw a {animal} wearing {clothing}.
It was so {emotion} that we {verb2}ed all the way home."""

    print("Story template:")
    print(story_template)
    print("\nWords used:")
    for key, value in words.items():
        if key in story_template:
            print(f"  {key}: {value}")

    print("\n" + "="*60)
    print("FINAL STORY")
    print("="*60)
    print(story_template.format(**words))
    print("="*60)

    print("\nTry running the actual games:")
    print("- python madlibs_game.py (GUI version)")
    print("- python madlibs_simple.py (Console version)")
    print("\nNote: In Windows terminal, emojis might not display properly.")

if __name__ == "__main__":
    demo_mad_lib()