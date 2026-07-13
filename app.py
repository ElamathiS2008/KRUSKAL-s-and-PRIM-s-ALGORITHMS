import streamlit as st
from program import kruskal, prim

st.title("Minimum Spanning Tree Visualizer")
st.write("Compare Prim's and Kruskal's Algorithms")

n = st.number_input(
    "Enter Number of Vertices",
    min_value=1,
    step=1
)

st.write(
    "Enter edges in the format:\n"
    "source destination weight\n"
    "One edge per line."
)

edge_text = st.text_area(
    "Edges",
    height=200,
    placeholder="0 1 4\n0 2 3\n1 2 1\n1 3 2"
)

start = st.number_input(
    "Starting Vertex for Prim's Algorithm",
    min_value=0,
    step=1
)

if st.button("Generate MST"):
    try:
        edges = []
        adj = {}

        lines = edge_text.strip().split("\n")

        for line in lines:
            u, v, w = map(int, line.split())

            edges.append((w, u, v))

            adj.setdefault(u, []).append((v, w))
            adj.setdefault(v, []).append((u, w))

        k_mst, k_cost = kruskal(int(n), edges[:])
        p_mst, p_cost = prim(int(n), adj, int(start))

        st.subheader("Kruskal's Algorithm")

        for u, v, w in k_mst:
            st.write(f"({u} - {v})   Weight = {w}")

        st.success(f"Total Cost = {k_cost}")

        st.subheader("Prim's Algorithm")

        for u, v, w in p_mst:
            st.write(f"({u} - {v})   Weight = {w}")

        st.success(f"Total Cost = {p_cost}")

    except:
        st.error("Please enter valid input.")
