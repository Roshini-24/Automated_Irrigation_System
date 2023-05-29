from typing import no_type_check
import streamlit as st
import pickle
import time
import datetime
from datetime import datetime, date, time
import numpy as np
from notebook import function_pred

def show_predict_page():
    st.title("water content prediction for best irrigation practice")
    st.write("enter the following details")
    plant_types = (
        "Tomato", "Potato", "Corn",
    )
    plant_types_input = st.selectbox("Plant Types", plant_types)
    start_date = st.date_input("start date")
    today = date.today()
    no_of_days = (today-start_date).days
    st.text("completed days from plantation")
    st.text(no_of_days)

    acre = st.number_input("Enter the acre amount:", min_value=1, max_value=10, value=1, step=1)
    b = no_of_days * 0.212
    T = acre * 14223 * b

    ok = st.button("Calculate Water")

    if ok:
        # prediction = water.predict()
        st.subheader(f"The estimated water Requirement in Liter is {T: .2f}")


