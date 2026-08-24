import streamlit as st

# --- CSS Styling ---
st.markdown("""
    <style>
        /* Hintergrund hellblau */
        .stApp {
            background-color: #87CEEB;
        }

        /* Überschrift in Schreibschrift und weiß */
        h1 {
            font-family: 'Brush Script MT', 'Comic Sans MS', cursive;
            color: white;
            text-align: center;
            font-size: 3em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }

        /* Eingabefeld */
        .stTextInput input {
            background-color: white;
            border-radius: 20px;
            font-family: 'Brush Script MT', 'Comic Sans MS', cursive;
            font-size: 1.5em;
            text-align: right;
            padding: 10px;
            border: none;
            box-shadow: 3px 3px 8px rgba(0,0,0,0.2);
        }

        /* Wolken-Buttons */
        .stButton button {
            background-color: white;
            color: #5b9bd5;
            font-family: 'Brush Script MT', 'Comic Sans MS', cursive;
            font-size: 1.4em;
            font-weight: bold;
            border: none;
            border-radius: 50% 50% 50% 50% / 40% 40% 60% 60%;
            box-shadow:
                0px -15px 0px 10px white,
                15px -25px 0px 5px white,
                -15px -20px 0px 8px white;
            width: 100%;
            height: 70px;
            margin: 20px 0px;
            cursor: pointer;
            transition: transform 0.1s;
        }

        /* Hover-Effekt */
        .stButton button:hover {
            transform: scale(1.1);
            background-color: #e8f4fc;
            color: #3a7abf;
        }

        /* Aktiv-Effekt */
        .stButton button:active {
            transform: scale(0.95);
        }
    </style>
""", unsafe_allow_html=True)

# --- Titel ---
st.title("☁️ Wolken Rechner ☁️")

# --- Session State für die Eingabe ---
if "eingabe" not in st.session_state:
    st.session_state.eingabe = ""

# --- Anzeigefeld ---
st.text_input("Eingabe", value=st.session_state.eingabe, disabled=True)

# --- Klick-Funktion ---
def klick(zeichen):
    if zeichen == "C":
        st.session_state.eingabe = ""
    elif zeichen == "=":
        try:
            erlaubte_zeichen = set("0123456789+-*/(). ")
            if all(z in erlaubte_zeichen for z in st.session_state.eingabe):
                ergebnis = eval(st.session_state.eingabe)
                st.session_state.eingabe = str(ergebnis)
            else:
                st.session_state.eingabe = "Fehler"
        except:
            st.session_state.eingabe = "Fehler"
    else:
        st.session_state.eingabe += zeichen

# --- Button-Layout ---
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
]

for zeile in buttons:
    spalten = st.columns(4)
    for i, zeichen in enumerate(zeile):
        spalten[i].button(
            zeichen,
            on_click=klick,
            args=(zeichen,),
            use_container_width=True
        )
