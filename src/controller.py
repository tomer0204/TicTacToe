# src/controller.py
from src import model
from src import view


class GameController:
    def __init__(self):
        self.board = model.Board()
        self.human_rounds = 0
        self.ai_rounds = 0
        self.current_round = 1
        self.current_player = "X"  # השחקן האנושי מתחיל
        self.gui = view.TicTacToeGUI(self)
        self.update_gui()

    def update_gui(self):
        self.gui.update_board(self.board.state)
        self.gui.update_score(self.human_rounds, self.ai_rounds, self.current_round)

    def reset_round(self):
        """
        מאפס את הלוח ומעדכן את מספר הראונד.
        """
        self.board.reset()
        self.current_round += 1
        self.current_player = "X"
        self.update_gui()

    def reset_match(self):
        """
        מאפס את כל המידע למשחק חדש (מערכת ניקוד).
        """
        self.human_rounds = 0
        self.ai_rounds = 0
        self.current_round = 1
        self.board.reset()
        self.current_player = "X"
        self.update_gui()

    def on_cell_click(self, index):
        """
        מטפל בלחיצה על תא – רק כאשר תור השחקן.
        """
        if self.current_player != "X":
            return
        if not self.board.make_move(index, "X"):
            return
        self.update_gui()

        if self.board.check_winner("X"):
            self.human_rounds += 1
            self.gui.show_message("Round Over", "You win this round!")
            if self.human_rounds == 3:
                self.gui.show_message("Match Over", "Congratulations! You won the match!")
                self.reset_match()
            else:
                self.reset_round()
            return

        if self.board.is_full():
            self.gui.show_message("Round Over", "It's a tie!")
            self.reset_round()
            return

        self.current_player = "O"
        self.gui.root.after(500, self.ai_move)

    def ai_move(self):
        """
        מבצע מהלך AI באמצעות אלגוריתם Minimax.
        """
        move = model.best_move(self.board.state)
        if move is not None:
            self.board.make_move(move, "O")
        self.update_gui()
        if self.board.check_winner("O"):
            self.ai_rounds += 1
            self.gui.show_message("Round Over", "AI wins this round!")
            if self.ai_rounds == 3:
                self.gui.show_message("Match Over", "AI won the match!")
                self.reset_match()
            else:
                self.reset_round()
            return
        if self.board.is_full():
            self.gui.show_message("Round Over", "It's a tie!")
            self.reset_round()
            return
        self.current_player = "X"
        self.update_gui()


def start_game():
    controller = GameController()
    controller.gui.root.mainloop()
