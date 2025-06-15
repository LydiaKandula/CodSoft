import tkinter as tk
import math

# Game state
board = [' ' for _ in range(9)]
player_score = 0
ai_score = 0
draw_score = 0

# Check for winner
def is_winner(brd, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(brd[i] == player for i in cond) for cond in win_conditions)

# Check if board is full
def is_full(brd):
    return ' ' not in brd

# Minimax algorithm
def minimax(brd, depth, is_maximizing):
    if is_winner(brd, 'O'):
        return 1
    elif is_winner(brd, 'X'):
        return -1
    elif is_full(brd):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                score = minimax(brd, depth + 1, False)
                brd[i] = ' '
                best = max(score, best)
        return best
    else:
        best = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                score = minimax(brd, depth + 1, True)
                brd[i] = ' '
                best = min(score, best)
        return best

# AI move using minimax
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'
    buttons[move].config(text='O', state='disabled')
    check_game_over()

# Handle player's click
def on_click(i):
    if board[i] == ' ':
        board[i] = 'X'
        buttons[i].config(text='X', state='disabled')
        check_game_over()
        if not is_winner(board, 'X') and not is_full(board):
            ai_move()

# Highlight buttons on win
def highlight_winner(winner):
    for win_combo in [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]:
        if all(board[i] == winner for i in win_combo):
            for i in win_combo:
                buttons[i].config(bg='lightgreen' if winner == 'X' else 'lightcoral')
            break

# Check for win or draw
def check_game_over():
    global player_score, ai_score, draw_score
    if is_winner(board, 'X'):
        status.config(text="🎉 You Win!")
        highlight_winner('X')
        player_score += 1
        update_score()
        disable_all()
    elif is_winner(board, 'O'):
        status.config(text="💻 AI Wins!")
        highlight_winner('O')
        ai_score += 1
        update_score()
        disable_all()
    elif is_full(board):
        status.config(text="🤝 It's a Draw!")
        draw_score += 1
        update_score()
        for btn in buttons:
            btn.config(bg='lightblue')
        disable_all()

# Disable all buttons
def disable_all():
    for btn in buttons:
        btn.config(state='disabled')

# Restart game
def restart_game():
    global board
    board = [' ' for _ in range(9)]
    for btn in buttons:
        btn.config(text=' ', state='normal', bg='SystemButtonFace')
    status.config(text="Your Turn!")

# Update score labels
def update_score():
    score_label.config(
        text=f"👤 You: {player_score}    🤖 AI: {ai_score}    🤝 Draws: {draw_score}"
    )

# --- GUI Setup ---
window = tk.Tk()
window.title("Tic-Tac-Toe AI (with Score)")

# Board buttons
buttons = []
for i in range(9):
    btn = tk.Button(window, text=' ', font=('Arial', 24), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Status and score
status = tk.Label(window, text="Your Turn!", font=('Arial', 16))
status.grid(row=3, column=0, columnspan=3)

score_label = tk.Label(window, text="👤 You: 0    🤖 AI: 0    🤝 Draws: 0", font=('Arial', 14))
score_label.grid(row=4, column=0, columnspan=3)

# Restart button
restart_btn = tk.Button(window, text="🔄 Restart Game", font=('Arial', 12), command=restart_game)
restart_btn.grid(row=5, column=0, columnspan=3, pady=10)

window.mainloop()
