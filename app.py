import streamlit as st
import os
from crew import crew

st.title("🚀 AI-Powered Blog Generator")

# User input for the topic
topic = st.text_input("Enter a topic for research:", "AI in healthcare")

# Path to the generated markdown file
output_file = "new-blog-post.md"

# Function to run CrewAI and read the generated blog post
def generate_blog(topic):
    try:
        # Run CrewAI process
        crew.kickoff(inputs={'topic': topic})

        # Check if the output file exists
        if os.path.exists(output_file):
            with open(output_file, "r", encoding="utf-8") as file:
                return file.read()
        else:
            return "⚠️ Blog post generation failed. No output file found."
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Button to trigger blog generation
if st.button("Generate Blog"):
    with st.spinner("Researching and Writing... Please wait ⏳"):
        blog_content = generate_blog(topic)
        st.success("✅ Blog Generated Successfully!")
        
        st.subheader("Generated Blog Post:")
        st.markdown(blog_content)

# Footer
st.markdown("---")
st.markdown("💡 Powered by CrewAI and Google Gemini API")
