import streamlit as st
import functions as fn

todos = fn.load_store()

st.title("PyTodo")
st.subheader("A simple task manager.")
st.write("Made to increase your productivity.")

enumerated_todos = [f"{i + 1}. {item}" for i, item in enumerate(todos)]
for et in enumerated_todos:
    st.checkbox(et)

