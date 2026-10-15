import streamlit as st

st.set_page_config(page_title="Developer Note Saver", page_icon="💡")

st.title("💡 Quick Developer Note & Snippet Saver")
st.write("Jot down your programming thoughts, logic structures, or debugging reminders.")

note_title = st.text_input("Note Title:", "Python List Comprehension Trick")
note_content = st.text_area("Write your code snippet or note here:", "[x**2 for x in range(10) if x % 2 == 0]")

if st.button("Save & Display Note"):
    if note_title and note_content:
        st.success("Note saved successfully to session memory!")
        st.markdown(f"### 📌 {note_title}")
        st.code(note_content, language="python")
    else:
        st.warning("Please fill in both title and content fields.")
