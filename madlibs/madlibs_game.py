import tkinter as tk
from tkinter import ttk, messagebox
import random

class MadLibsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Mad Libs Game")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")

        # Story templates
        self.stories = [
            {
                "title": "The Adventure",
                "template": "Yesterday, I went to the {place} with my {adjective} {noun}. We {verb}ed all day long! Then we saw a {animal} wearing {clothing}. It was so {emotion} that we {verb2}ed all the way home.",
                "words": ["place", "adjective", "noun", "verb", "animal", "clothing", "emotion", "verb2"]
            },
            {
                "title": "The Restaurant",
                "template": "I went to a {adjective} restaurant called '{name}'. The waiter was a {animal} who served me {food} on a {noun}. I {verb}ed so much that I became {emotion} and had to {verb2} out of there!",
                "words": ["adjective", "name", "animal", "food", "noun", "verb", "emotion", "verb2"]
            },
            {
                "title": "The Dream",
                "template": "Last night I dreamed I was a {adjective} {noun} who could {verb}. I flew to {place} where I met a {animal} who gave me {food}. We {verb2}ed together until I woke up feeling {emotion}.",
                "words": ["adjective", "noun", "verb", "place", "animal", "food", "verb2", "emotion"]
            },
            {
                "title": "The Superhero",
                "template": "My superhero name is {name} Man/Woman! I have the power to {verb} {noun}s faster than a {animal}. I wear a {adjective} {clothing} and when I get {emotion}, I {verb2} all the way to {place}.",
                "words": ["name", "verb", "noun", "animal", "adjective", "clothing", "emotion", "verb2", "place"]
            },
            {
                "title": "The Time Machine",
                "template": "I built a time machine out of a {adjective} {noun}! When I {verb}ed it, I went to {place} where {animal}s rule the world. They served me {food} and made me wear {clothing}. I felt so {emotion} that I {verb2}ed back home immediately.",
                "words": ["adjective", "noun", "verb", "place", "animal", "food", "clothing", "emotion", "verb2"]
            }
        ]

        self.current_story = None
        self.entries = {}

        self.setup_ui()

    def setup_ui(self):
        # Title
        title_label = tk.Label(self.root, text="Mad Libs Game",
                              font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=20)

        # Story selection
        story_frame = tk.Frame(self.root, bg="#f0f0f0")
        story_frame.pack(pady=10)

        tk.Label(story_frame, text="Choose a story:", font=("Arial", 12), bg="#f0f0f0").pack()

        self.story_var = tk.StringVar()
        story_combo = ttk.Combobox(story_frame, textvariable=self.story_var,
                                  values=[story["title"] for story in self.stories],
                                  state="readonly", width=30)
        story_combo.pack(pady=5)
        story_combo.bind("<<ComboboxSelected>>", self.on_story_selected)

        # Words input frame
        self.words_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.words_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Buttons frame
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10)

        self.generate_btn = tk.Button(button_frame, text="Generate Story!",
                                     command=self.generate_story,
                                     font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
                                     padx=20, pady=10, state="disabled")
        self.generate_btn.pack(side="left", padx=10)

        self.reset_btn = tk.Button(button_frame, text="Reset",
                                  command=self.reset_game,
                                  font=("Arial", 12), bg="#f44336", fg="white",
                                  padx=20, pady=10)
        self.reset_btn.pack(side="left", padx=10)

        self.random_btn = tk.Button(button_frame, text="Random Story",
                                   command=self.random_story,
                                   font=("Arial", 12), bg="#2196F3", fg="white",
                                   padx=20, pady=10)
        self.random_btn.pack(side="left", padx=10)

    def on_story_selected(self, event=None):
        story_title = self.story_var.get()
        self.current_story = next(story for story in self.stories if story["title"] == story_title)
        self.create_word_inputs()
        self.generate_btn.config(state="normal")

    def create_word_inputs(self):
        # Clear previous inputs
        for widget in self.words_frame.winfo_children():
            widget.destroy()

        self.entries = {}

        # Create input fields for each word
        canvas = tk.Canvas(self.words_frame, bg="#f0f0f0")
        scrollbar = ttk.Scrollbar(self.words_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        tk.Label(scrollable_frame, text=f"Enter words for '{self.current_story['title']}':",
                font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#333").pack(pady=10)

        for word in self.current_story["words"]:
            frame = tk.Frame(scrollable_frame, bg="#f0f0f0")
            frame.pack(fill="x", pady=5, padx=20)

            label = tk.Label(frame, text=f"Enter a {word}:",
                           font=("Arial", 11), bg="#f0f0f0", width=15, anchor="w")
            label.pack(side="left", padx=5)

            entry = tk.Entry(frame, font=("Arial", 11), width=30)
            entry.pack(side="left", padx=5)
            self.entries[word] = entry

            # Add example tooltip
            examples = {
                "adjective": "(e.g., happy, blue, strange)",
                "noun": "(e.g., cat, house, car)",
                "verb": "(e.g., run, jump, sing)",
                "place": "(e.g., park, moon, school)",
                "animal": "(e.g., dog, elephant, bird)",
                "food": "(e.g., pizza, apple, cake)",
                "clothing": "(e.g., hat, shoes, dress)",
                "emotion": "(e.g., happy, scared, excited)",
                "name": "(e.g., Bob, Super, Captain)"
            }

            if word in examples:
                tk.Label(frame, text=examples[word],
                        font=("Arial", 9), fg="#666", bg="#f0f0f0").pack(side="left", padx=5)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def generate_story(self):
        if not self.current_story:
            return

        # Get all words
        words = {}
        for word_type, entry in self.entries.items():
            word = entry.get().strip()
            if not word:
                messagebox.showwarning("Missing Word", f"Please enter a {word_type}!")
                return
            words[word_type] = word

        # Generate the story
        story = self.current_story["template"].format(**words)

        # Show the story in a new window
        self.show_story(story)

    def show_story(self, story):
        story_window = tk.Toplevel(self.root)
        story_window.title(f"Your Mad Lib: {self.current_story['title']}")
        story_window.geometry("600x400")
        story_window.configure(bg="#fff")

        # Title
        title_label = tk.Label(story_window, text=f"{self.current_story['title']}",
                              font=("Arial", 18, "bold"), bg="#fff", fg="#333")
        title_label.pack(pady=10)

        # Story text
        text_frame = tk.Frame(story_window, bg="#fff")
        text_frame.pack(fill="both", expand=True, padx=20, pady=10)

        text_widget = tk.Text(text_frame, wrap="word", font=("Arial", 12),
                             bg="#f9f9f9", padx=10, pady=10)
        text_widget.insert(1.0, story)
        text_widget.config(state="disabled")
        text_widget.pack(fill="both", expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(text_widget, command=text_widget.yview)
        scrollbar.pack(side="right", fill="y")
        text_widget.config(yscrollcommand=scrollbar.set)

        # Buttons
        button_frame = tk.Frame(story_window, bg="#fff")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Play Again",
                 command=lambda: [story_window.destroy(), self.reset_game()],
                 font=("Arial", 11), bg="#4CAF50", fg="white", padx=15, pady=5).pack(side="left", padx=5)

        tk.Button(button_frame, text="Close",
                 command=story_window.destroy,
                 font=("Arial", 11), bg="#f44336", fg="white", padx=15, pady=5).pack(side="left", padx=5)

        tk.Button(button_frame, text="Copy Story",
                 command=lambda: self.copy_to_clipboard(story),
                 font=("Arial", 11), bg="#2196F3", fg="white", padx=15, pady=5).pack(side="left", padx=5)

    def copy_to_clipboard(self, text):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        messagebox.showinfo("Copied!", "Story copied to clipboard!")

    def reset_game(self):
        self.story_var.set("")
        self.current_story = None
        for widget in self.words_frame.winfo_children():
            widget.destroy()
        self.entries = {}
        self.generate_btn.config(state="disabled")

    def random_story(self):
        random_story = random.choice(self.stories)
        self.story_var.set(random_story["title"])
        self.on_story_selected()

if __name__ == "__main__":
    root = tk.Tk()
    game = MadLibsGame(root)
    root.mainloop()