import streamlit as st
import plotly.express as px

df = px.data.stocks()

gm = px.data.gapminder()
mask = gm["year"] == 2007
df2007 = gm[mask]

st.title("data exploration project")

st.title("Data Analysis")
st.markdown("The data is shown below: ")
st.sidebar.title("Options")
st.sidebar.markdown("Select Charts and Features:")
# st.dataframe(df)
option = st.sidebar.selectbox("Which chart would you like to see?", ["None", "line", "scatter", "bar", "histogram", "gapminder"])
if option == "line":
    fig = px.line(df, x = "date", y = "GOOG")
    st.plotly_chart(fig)
elif option == "scatter":
    fig = px.scatter(df, x = "GOOG", y = "AAPL", hover_name="date")
    st.plotly_chart(fig)
elif option == "gapminder":
    fig = px.scatter(df2007, x="gdpPercap",
               y="lifeExp",
               size="pop",
               hover_name="country",
               color="continent")
    st.plotly_chart(fig)
elif option == "bar":
    mean_population = df2007.groupby("continent")["pop"].mean().reset_index()
    fig = px.bar(mean_population, x="continent", y="pop")
    st.plotly_chart(fig)
elif option == "histogram":
    fig = px.histogram(df2007, x="lifeExp")
    st.plotly_chart(fig)