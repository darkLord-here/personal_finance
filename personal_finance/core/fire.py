"""
Author: darklord-here
Description: Core logic of the F.I.R.E. calculator
"""


def calculate_fire(m_exp: int, c_age: int, r_age: int, inflation: float, c_f_age: int = 35):
    if r_age < c_age or r_age < c_f_age:
        raise ValueError("Retirement age cannot be less than Current Age or Coast Fire Age")
    
    if not (isinstance(m_exp, int) and isinstance(c_age, int) and isinstance(r_age, int) and isinstance(inflation, float) and isinstance(c_f_age, int)):
        raise TypeError(f"Type Error!! {isinstance(m_exp, int)} and {isinstance(c_age, int)} and {isinstance(r_age, int)} and {isinstance(inflation, int)} and {isinstance(c_f_age, int)}")
    
    y_exp = m_exp * 12
    r_y_exp = round(y_exp *((1+inflation)**(r_age - c_age)))
    lean_fire = r_y_exp * 20
    fire = r_y_exp * 25
    fat_fire = r_y_exp * 50
    coast_fire = round(fire/1.1 ** (r_age - c_f_age))

    return y_exp, r_y_exp, lean_fire, fire, fat_fire, coast_fire