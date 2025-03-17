# src/model.py

def check_winner(board, player):
    """
    בודק האם השחקן (player) ניצח בלוח.
    """
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # שורות
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # עמודות
        (0, 4, 8), (2, 4, 6)              # אלכסונים
    ]
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_board_full(board):
    """
    בודק האם כל תאי הלוח מלאים.
    """
    return all(cell is not None for cell in board)

def get_available_moves(board):
    """
    מחזיר רשימה של אינדקסים של תאים פנויים בלוח.
    """
    return [i for i, cell in enumerate(board) if cell is None]

def minimax(board, is_maximizing):
    """
    אלגוריתם Minimax המחשב ניקוד למצב נתון בלוח.
    """
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in get_available_moves(board):
            board[move] = "O"
            score = minimax(board, False)
            board[move] = None
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(board):
            board[move] = "X"
            score = minimax(board, True)
            board[move] = None
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    """
    מחשב את המהלך הטוב ביותר עבור ה-AI.
    """
    best_score = -float('inf')
    move_choice = None
    for move in get_available_moves(board):
        board[move] = "O"
        score = minimax(board, False)
        board[move] = None
        if score > best_score:
            best_score = score
            move_choice = move
    return move_choice

class Board:
    """
    מחלקה לניהול מצב לוח המשחק.
    """
    def __init__(self):
        self.state = [None] * 9  # לוח בגודל 3x3

    def make_move(self, index, player):
        """
        מבצעת מהלך בלוח. מחזירה True אם המהלך הצליח.
        """
        if self.state[index] is None:
            self.state[index] = player
            return True
        return False

    def reset(self):
        """
        מאפס את הלוח.
        """
        self.state = [None] * 9

    def check_winner(self, player):
        """
        בודק האם לשחקן יש ניצחון.
        """
        return check_winner(self.state, player)

    def is_full(self):
        """
        בודק האם הלוח מלא.
        """
        return is_board_full(self.state)

    def get_available_moves(self):
        """
        מחזיר את רשימת התאים הפנויים.
        """
        return get_available_moves(self.state)
