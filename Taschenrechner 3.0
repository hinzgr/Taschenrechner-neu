import streamlit as st

st.title("🧮 Taschenrechner")

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
