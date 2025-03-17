# src/view.py
import tkinter as tk
from tkinter import messagebox


class TicTacToeGUI:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        # הפעלה במסך מלא
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="#1e1e1e")  # רקע כהה
        # יצירת אפשרות לצאת ממסך מלא על ידי לחיצה על מקש Escape
        self.root.bind("<Escape>", self.exit_fullscreen)
        self.buttons = []
        self.create_widgets()

    def exit_fullscreen(self, event=None):
        self.root.attributes("-fullscreen", False)

    def create_widgets(self):
        # מסגרת ללוח המשחק עם רקע מותאם
        board_frame = tk.Frame(self.root, bg="#1e1e1e")
        board_frame.pack(pady=50)

        # יצירת 9 לחצנים במבנה 3x3 עם עיצוב משופר
        for i in range(9):
            button = tk.Button(board_frame, text="", font=('Arial', 36, 'bold'), width=4, height=2,
                               bg="#282c34", fg="white", activebackground="#3a3f47",
                               command=lambda i=i: self.controller.on_cell_click(i))
            button.grid(row=i // 3, column=i % 3, padx=10, pady=10)
            self.buttons.append(button)

        # מסגרת להצגת ניקוד וראונדים
        score_frame = tk.Frame(self.root, bg="#1e1e1e")
        score_frame.pack(pady=20)

        self.human_score_label = tk.Label(score_frame, text="Player (X): 0", font=('Arial', 24), bg="#1e1e1e",
                                          fg="white")
        self.human_score_label.pack(side=tk.LEFT, padx=40)

        self.ai_score_label = tk.Label(score_frame, text="AI (O): 0", font=('Arial', 24), bg="#1e1e1e", fg="white")
        self.ai_score_label.pack(side=tk.LEFT, padx=40)

        self.round_label = tk.Label(score_frame, text="Round: 1", font=('Arial', 24), bg="#1e1e1e", fg="white")
        self.round_label.pack(side=tk.LEFT, padx=40)

    def update_board(self, board_state):
        """
        מעדכן את תצוגת הלוח בהתאם למצב הנתון.
        """
        for i, cell in enumerate(board_state):
            text = cell if cell is not None else ""
            self.buttons[i].config(text=text)

    def update_score(self, human_rounds, ai_rounds, current_round):
        """
        מעדכן את תצוגת הניקוד והראונדים.
        """
        self.human_score_label.config(text=f"Player (X): {human_rounds}")
        self.ai_score_label.config(text=f"AI (O): {ai_rounds}")
        self.round_label.config(text=f"Round: {current_round}")

    def show_message(self, title, message):
        """
        מציג הודעה (MessageBox).
        """
        messagebox.showinfo(title, message)
