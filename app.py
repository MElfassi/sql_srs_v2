import streamlit as st
import pandas as pd
import duckdb as db

st.write("Hello world!")
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    sql_query = st.text_area(label="entrer votre input")
    result = db.sql(sql_query).df()
    st.write(f"Vous avez rentrer la query suivante : {sql_query}")
    st.dataframe(result)

with tab2:
    st.header("A Dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("A Owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
