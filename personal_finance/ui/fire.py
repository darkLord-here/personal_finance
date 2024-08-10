"""
Author: darklord-here
Description: Front End of the F.I.R.E. calculator
"""

import streamlit as st
from personal_finance import core


def show_fire():
    """
    This function will render the screen of the F.I.R.E. calculator
    Args: None
    """
    monthly_expense = st.number_input(label="Enter the monthly salary", min_value=0)
    current_age = st.number_input(label="Enter the current age", min_value=0)
    retirement_age = st.number_input(label="Enter the retirement age", min_value=0)
    inflation = st.number_input(label="Enter the percentage of inflation", min_value=0)
    coast_fire_age = st.number_input(label="Enter the Coast fire age", value=35, min_value=0)

    try:
        result = core.calculate_fire(monthly_expense, current_age, retirement_age, float(inflation)/float(100), coast_fire_age)
        popover = st.popover("Filter items")
        lean_fire = popover.checkbox("Show Lean Fire", True)
        fire = popover.checkbox("Show Fire", True)
        fat_fire = popover.checkbox("Show Fat Fire", True)
        coast_fire = popover.checkbox("Show Coast Fire", True)

        container = st.container()
        script = """<div id = 'result'></div>"""
        st.markdown(script, unsafe_allow_html=True)

        with container:
            columns = st.columns(2)
            script = """<div id = 'inner'></div>"""
            st.markdown(script, unsafe_allow_html=True)
            with columns[0]:
                if lean_fire:
                    st.markdown(f"Lean FIRE &nbsp; `{result[2]}`")
                if fire:
                    st.markdown(f"FIRE &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; `{result[3]}`")
            with columns[1]:
                if fat_fire:
                    st.markdown(f"Fat FIRE  &nbsp; &nbsp; `{result[4]}`")
                if coast_fire:
                    st.markdown(f"Coast FIRE `{result[5]}`")
            
            style = """<style>
                div[data-testid='stVerticalBlock']:has(div#inner):not(:has(div#result)) {background-color: #E4F2EC; color: #000000};
                </style>
                """
            st.markdown(style, unsafe_allow_html=True)
    
        with st.expander("Some info related to FIRE"):
            st.markdown("some info related to FIRE")
    except ValueError:
        st.write("Enter the valid values in the fields")

    

    