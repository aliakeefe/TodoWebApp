import streamlit as st
import functions
import time

todo_list = functions.read_todo_list()
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todo_list.append(todo)
    functions.write_todo_list(todo_list)
    st.session_state['new_todo']=''

st.title('My Todo App')
st.subheader(str(time.strftime('%B %d, %Y')))
st.write('Here is your list:')



for index, item in enumerate(todo_list):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todo_list.pop(index)
        functions.write_todo_list(todo_list)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label='', placeholder='Add a todo item..', on_change=add_todo,
              key='new_todo')

