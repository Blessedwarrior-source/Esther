import streamlit as st
import pandas as pd

# Initialize session state for task data if it doesn't exist
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = pd.DataFrame(columns=["Task", "Status"])

# Function to update the task list
def add_task(task, status):
    new_task = pd.DataFrame([[task, status]], columns=["Task", "Status"])
    st.session_state['tasks'] = pd.concat([st.session_state['tasks'], new_task], ignore_index=True)

# Streamlit app header
st.title("Esther's Simplistic Action Planner")
st.write(
    """
    Welcome to Esther, a simplistic action planning tool. 
    Use this tool to help you stay focused and organized as you prioritize your tasks.
    Add your tasks, categorize them, and track your progress with ease.
    """
)

# Task input
task_input = st.text_input("Enter your task:")
status_option = st.selectbox("Select task status", ["To Do", "In Progress", "Completed"])

if st.button("Add Task"):
    if task_input:
        add_task(task_input, status_option)
        st.success(f"Task '{task_input}' added successfully!")
    else:
        st.warning("Please enter a task!")

# Display tasks in a table
st.subheader("Your Task List")
st.write("Below is your current action plan:")

# Display the DataFrame
if not st.session_state['tasks'].empty:
    st.dataframe(st.session_state['tasks'])
else:
    st.write("No tasks added yet.")

# Filter tasks by status
st.subheader("Filter Tasks by Status")
status_filter = st.selectbox("Choose task status to filter", ["All", "To Do", "In Progress", "Completed"])

if status_filter != "All":
    filtered_tasks = st.session_state['tasks'][st.session_state['tasks']['Status'] == status_filter]
    st.write(filtered_tasks)
else:
    st.write(st.session_state['tasks'])

