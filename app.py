import streamlit as st

from visualizers.array_visualizer import show_array_visualizer
from visualizers.searching_visualizer import show_searching_visualizer
from visualizers.sorting_visualizer import show_sorting_visualizer
from visualizers.stack_visualizer import show_stack_visualizer
from visualizers.queue_visualizer import show_queue_visualizer
from visualizers.linked_list_visualizer import show_linked_list_visualizer
from visualizers.tree_visualizer import show_tree_visualizer

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


elif topic == "Searching":

    show_searching_visualizer()


elif topic == "Sorting":

    show_sorting_visualizer()

elif topic == "Stack":

    show_stack_visualizer()

elif topic == "Queue":

    show_queue_visualizer()

elif topic == "Linked List":
    show_linked_list_visualizer()

elif topic == "Trees":
    show_tree_visualizer()


else:

    st.header(topic)

    st.info(
        f"{topic} visualizer will be added soon."
    )