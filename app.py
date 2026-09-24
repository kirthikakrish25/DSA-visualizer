import streamlit as st

from visualizers.array_visualizer import show_array_visualizer

# Page configuration
st.set_page_config(
    page_title="DSA Visualizer",
    page_icon="📊",
    layout="wide"
)

# Main title
st.title("DSA Visualizer")

st.write(
    "An interactive platform to learn and visualize "
    "Data Structures and Algorithms."
)

# Sidebar
st.sidebar.title("DSA Topics")

topic = st.sidebar.selectbox(
    "Choose a topic:",
    [
        "Home",
        "Arrays",
        "Searching",
        "Sorting",
        "Stack",
        "Queue",
        "Linked List",
        "Trees",
        "Graphs"
    ]
)

if topic == "Home":

    st.header("Welcome to DSA Visualizer")

    st.write(
        "Select a topic from the sidebar to begin."
    )

elif topic == "Arrays":

    show_array_visualizer()

else:

    st.header(topic)

    st.info(
        f"{topic} visualizer will be added soon."
    )