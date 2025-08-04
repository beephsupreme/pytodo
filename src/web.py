import streamlit as st
import functions as fn

def add_todo():
    todo = st.session_state["new_todo"]
    print(todo)

todos = fn.load_store()

st.title("PyTodo")
st.subheader("A simple task manager.")
st.write("Made to increase your productivity.")

enumerated_todos = [f"{i + 1}. {item}" for i, item in enumerate(todos)]
for et in enumerated_todos:
    st.checkbox(et)

st.text_input(label="", placeholder="Enter a todo",
              on_change=add_todo(), key="new_todo")

