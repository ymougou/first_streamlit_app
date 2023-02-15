import streamlit

streamlit.title("My parents new healthy dinner")

streamlit.header("Breakfast Favorites")
streamlit.text("🥣 Omega3 & blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach and Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞Avocado toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
