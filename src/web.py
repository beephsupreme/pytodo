import streamlit as st
import functions as fn

def add_todo():
    todo = st.session_state["new_todo"]
    fn.add(todo)
    st.session_state["new_todo"] = ""

todos = fn.load_store()

st.title("PyTodo")
st.subheader("A simple task manager.")
st.write("Made to increase your productivity.")

enumerated_todos = [f"{i}. {item}" for i, item in enumerate(todos)]
for i, et in enumerate(enumerated_todos):
    checkbox = st.checkbox(et)
    if checkbox:
        fn.complete(i)
        todos = fn.load_store()
        st.rerun()



st.text_input(label=" ", placeholder="Enter a todo",
              on_change=add_todo, key='new_todo')

