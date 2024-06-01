# Phonepe
Phonepe Visualization app
Domain : Fintech
Technologies used : Github Cloning, Python, Pandas, MySQL, mysql-connector-python, Streamlit, and Plotly.
Overview : In this streamlit web app you can visualize the phonepe pulse data and gain lot of insights on transactions, number of users, top 10 state, district, pincode and which brand has most number of users and so on. Bar charts, Pie charts and Geo map visualization are used to get some insights.

1.MySQL Connection Management:

The MySQL connection is established at the beginning and closed at the end of the script to ensure proper resource management.

2.Custom CSS for Background:

The custom CSS snippet changes the background color of the app to #6F38AD.

3.Option Menu Implementation:

The option_menu widget is used for sidebar navigation with different options like Home, Charts, Data, and About.

4.Cloning GitHub Repository:

The script checks if the pulse directory exists and clones the PhonePe Pulse repository if it doesn't.

5.Data Visualization Using Plotly:

Various Plotly charts like pie charts and bar charts are used for visualizing transaction and user data based on selected criteria.

6.Image Handling:

Images are loaded and displayed using the PIL library and Streamlit's image functions.

7.User-Friendly Interactions:

Sliders, select boxes, and info messages guide the user through the app's functionalities, providing an interactive experience.
