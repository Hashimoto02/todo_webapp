import streamlit as st
import functionstodo

# get the list of todos
todos = functionstodo.get_todos()


# function to be called on_change to add todos in input box and write or update the checkbox
def add_todo():
    n_todo = st.session_state["new_todo"] + "\n"
    todos.append(n_todo)
    functionstodo.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

st.text_input(label="", placeholder="Add new todo....",
              on_change=add_todo, key="new_todo")
# listing the updated items in the checkbox
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)  # remove todo
        functionstodo.write_todos(todos)  # update after deleting
        del st.session_state[todo]  # delete session _state
        st.rerun()  # halts the current script run and  executes no further statements.
        # Streamlit immediately queues the script to rerun.

# connecting the input text to todo when entered reflects/adds to todos in the web app

print("Hello")


