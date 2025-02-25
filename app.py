import streamlit as st

# Page Configuration
st.set_page_config(page_title="🎨 Colorful Tic-Tac-Toe", page_icon="❌⭕", layout="centered")

# Title with Color
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🎮 Colorful Tic-Tac-Toe</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Click a box to make your move!</p>", unsafe_allow_html=True)

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.winning_combo = []

# Winning Combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]  # Diagonals
]

# Function to check winner
def check_winner():
    for combo in winning_combinations:
        a, b, c = combo
        if (st.session_state.board[a] == 
            st.session_state.board[b] == 
            st.session_state.board[c] != ""):
            st.session_state.winner = st.session_state.board[a]
            st.session_state.winning_combo = combo
            return

# Button Click Function (One-Click Play)
def button_click(index):
    if st.session_state.board[index] == "" and not st.session_state.winner:
        st.session_state.board[index] = st.session_state.current_player
        check_winner()
        if not st.session_state.winner:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# CSS for Styling
st.markdown("""
    <style>
        .stButton > button {
            width: 100px;
            height: 100px;
            font-size: 30px;
            font-weight: bold;
            color: white;
            border-radius: 10px;
            border: 2px solid black;
            background: #3498db;
            transition: 0.3s;
        }
        .stButton > button:hover {
            background: #f1c40f;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# Display the Tic Tac Toe Board with Colorful Buttons
st.markdown("---")
cols = st.columns(3)
for i in range(9):
    btn_color = "#3498db"  # Default Blue
    text_color = "white"

    if st.session_state.board[i] == "X":
        btn_color = "#e74c3c"  # Red for X
    elif st.session_state.board[i] == "O":
        btn_color = "#2ecc71"  # Green for O

    if i in st.session_state.winning_combo:
        btn_color = "#27ae60"  # Winning Tiles Turn Dark Green

    btn_style = f"""
    <style>
        .stButton > button {{
            width: 100px;
            height: 100px;
            font-size: 30px;
            font-weight: bold;
            color: {text_color};
            background: {btn_color};
            border-radius: 10px;
            border: 2px solid black;
            transition: 0.3s;
        }}
    </style>
    """
    st.markdown(btn_style, unsafe_allow_html=True)

    with cols[i % 3]:
        if st.button(st.session_state.board[i] or " ", key=i):
            button_click(i)

st.markdown("---")

# Display Winner or Turn Announcement
if st.session_state.winner:
    st.markdown(f"<h2 style='text-align: center; color: green;'>🎉 Player {st.session_state.winner} Wins! 🎊</h2>", unsafe_allow_html=True)
else:
    turn_color = "#e74c3c" if st.session_state.current_player == "X" else "#2ecc71"
    st.markdown(f"<h3 style='text-align: center; color: {turn_color};'>🔄 Player {st.session_state.current_player}'s Turn</h3>", unsafe_allow_html=True)

# Restart Button
if st.button("🔄 Restart Game", help="Click to start a new round"):
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.winning_combo = []
    st.experimental_rerun()
