import streamlit as st

# Page setup
st.set_page_config(page_title="Agent Esther", page_icon="🗂️", layout="centered")

# Header
st.title("🗂️ Meet Agent Esther")
st.subheader("Your Personalized Action Planning Assistant")

# Introduction
st.markdown("""
Hi, I’m **Agent Esther** — I help you get things done by **organizing and prioritizing your action steps and goals**.  
I work with **individuals with ADHD/ADD** and **everyday achievers** to:
- Break down big goals into **manageable steps**
- **Arrange tasks in logical order or by timeline**
- Create **visual plans** to stay on track and focused
- Promote progress without overwhelm
""")

# Services list
st.markdown("### 🔧 What I Can Help You With")
services = [
    "🧠 Break goals into clear, actionable steps",
    "📆 Prioritize tasks and deadlines logically",
    "📊 Create simple visual timelines or task maps",
    "🎯 Keep you focused on key objectives",
    "🔄 Review and adjust plans as needed"
]
for item in services:
    st.write(item)

# ADHD/ADD Note
st.markdown("### 🧠 Especially Helpful For:")
st.info("• Individuals with ADHD or ADD who need extra structure and clarity\n"
         "• Anyone who struggles with planning, organization, or follow-through")

# Optional form for help
st.markdown("### 🚀 Ready to Start Planning?")
with st.form("connect_esther"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    goal = st.text_area("What goal or task are you trying to plan?")
    submit = st.form_submit_button("Work with Agent Esther")
    if submit:
        st.success(f"Thanks {name}! I’ll reach out to help you start planning for: {goal}")

# Footer
st.markdown("---")
st.caption("🗓️ Powered by Streamlit | Agent Esther • Action Planner 2025")
