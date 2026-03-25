import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors - Marv's Game")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # Game variables
        self.user_score = 0
        self.computer_score = 0
        self.choices = ["Rock", "Paper", "Scissors"]

        self.setup_ui()

    def setup_ui(self):
        # Title
        title_label = tk.Label(self.root, text="Rock Paper Scissors",
                              font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=20)

        # Score display
        self.score_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.score_frame.pack(pady=10)

        self.score_label = tk.Label(self.score_frame,
                                   text=f"You: {self.user_score}  Computer: {self.computer_score}",
                                   font=("Helvetica", 14), bg="#f0f0f0", fg="#555")
        self.score_label.pack()

        # Choice display
        self.choice_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.choice_frame.pack(pady=20)

        self.user_choice_label = tk.Label(self.choice_frame, text="Your choice: ",
                                         font=("Helvetica", 12), bg="#f0f0f0")
        self.user_choice_label.pack()

        self.computer_choice_label = tk.Label(self.choice_frame, text="Computer choice: ",
                                             font=("Helvetica", 12), bg="#f0f0f0")
        self.computer_choice_label.pack()

        # Result display
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16, "bold"),
                                    bg="#f0f0f0", fg="#007acc")
        self.result_label.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=20)

        rock_button = tk.Button(button_frame, text="🪨 Rock", command=lambda: self.play("Rock"),
                               font=("Helvetica", 12), bg="#4CAF50", fg="white",
                               padx=20, pady=10, width=8)
        rock_button.pack(side=tk.LEFT, padx=5)

        paper_button = tk.Button(button_frame, text="📄 Paper", command=lambda: self.play("Paper"),
                                font=("Helvetica", 12), bg="#2196F3", fg="white",
                                padx=20, pady=10, width=8)
        paper_button.pack(side=tk.LEFT, padx=5)

        scissors_button = tk.Button(button_frame, text="✂️ Scissors",
                                   command=lambda: self.play("Scissors"),
                                   font=("Helvetica", 12), bg="#f44336", fg="white",
                                   padx=20, pady=10, width=8)
        scissors_button.pack(side=tk.LEFT, padx=5)

        # Reset button
        reset_button = tk.Button(self.root, text="Reset Score", command=self.reset_score,
                                font=("Helvetica", 12), bg="#9E9E9E", fg="white",
                                padx=20, pady=10)
        reset_button.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)

        # Update choice labels
        self.user_choice_label.config(text=f"Your choice: {user_choice}")
        self.computer_choice_label.config(text=f"Computer choice: {computer_choice}")

        # Determine winner
        if user_choice == computer_choice:
            result = "It's a Tie! 🤝"
            color = "#FF9800"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You Win! 🎉"
            self.user_score += 1
            color = "#4CAF50"
        else:
            result = "Computer Wins! 💻"
            self.computer_score += 1
            color = "#f44336"

        # Update result and score
        self.result_label.config(text=result, fg=color)
        self.score_label.config(text=f"You: {self.user_score}  Computer: {self.computer_score}")

    def reset_score(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text=f"You: {self.user_score}  Computer: {self.computer_score}")
        self.result_label.config(text="")
        self.user_choice_label.config(text="Your choice: ")
        self.computer_choice_label.config(text="Computer choice: ")
        messagebox.showinfo("Reset", "Scores have been reset!")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()