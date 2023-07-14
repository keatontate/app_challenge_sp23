from collections import namedtuple
from sklearn.model_selection import train_test_split
# from xgboost import XGBRegressor
import altair as alt
import math
import pandas as pd
import streamlit as st


"""
# Welcome to Streamlit, doodette!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    # total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    # num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    # Point = namedtuple('Point', 'x y')
    # data = []

    # points_per_turn = total_points / num_turns

    # for curr_point_num in range(total_points):
    #     curr_turn, i = divmod(curr_point_num, points_per_turn)
    #     angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
    #     radius = curr_point_num / total_points
    #     x = radius * math.cos(angle)
    #     y = radius * math.sin(angle)
    #     data.append(Point(x, y))

    # st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
    #     .mark_circle(color='#0068c9', opacity=0.5)
    #     .encode(x='x:Q', y='y:Q'))
    
    ### PART 1. Allow the users to upload the [data.csv](data.csv) file into the app.
    # documentation - https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
    uploaded_data = st.file_uploader('Please upload your data as a .csv file.',type='csv')
    if uploaded_data is not None:
        # may need to figure out how to keep in raw pickle format
        # I'll try reading it as a string first
        data = pd.read_csv(uploaded_data)
        st.dataframe(data)


    ### PART 2. Require the user to select the `target` variable.
    target = st.selectbox('Select the target variable', data.columns)
    target

    ### PART 3. Allow the users to pick the features they want to use in their ML model.
    features = st.multiselect('Select features to use in the model', data.columns)
    features

    ### PART 4. Provide a plot that allows the users to pick an x and plot it against their target (you can have it only work for numeric values).
    feature_selection = st.radio("What feature to plot against the target?",(features))

    # I always forget Altair syntax: https://altair-viz.github.io/getting_started/overview.html#overview
    # I could probably check the columns and do box plots for discrete variables, but I'm just gonna get it working with scatter plots first.
    feature_target_chart = alt.Chart(data).mark_circle().encode(
        x=feature_selection,
        y=target
    )
    st.altair_chart(feature_target_chart)

    ### PART 5. Explain your ML model (pick something fun or easy) and provide them a`fit` button.
    

    ### PART 6. Report a feature importance plot and at least one measure of model fit.
    

    ### PART 7. Provide a space on the app where the users can input new values for their features and get a prediction based on the fit model.
    # data editor widget? https://docs.streamlit.io/library/api-reference/data/st.data_editor
    # yes, set num_rows to dynamic on the chosen features dataframe

    ### PART 8. Allow them to download their [`.pickle` model file](https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/).
