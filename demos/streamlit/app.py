import streamlit as st

from great_tables import GT, GTI, data
from great_tables.streamlit import st_gti, update_gti

cars = data.gtcars[["mfr", "model", "year", "hp", "msrp"]]

st.button("Fastest first", on_click=update_gti, args=("cars",), kwargs={"sort": "-hp"})
table = (
    GTI(cars)
    .fmt_integer("hp")
    .fmt_currency("msrp", decimals=0)
    .i_cols_filter(columns="mfr", type="facet")
    .i_selection("multiple")
)
state = st_gti(table, key="cars")
st.write(f"{len(state.selection)} of {len(state.rows or [])} cars selected")

chosen = cars.iloc[state.selection]
st.bar_chart(chosen, x="model", y="hp")
st.html(GT(chosen).fmt_integer("hp").fmt_currency("msrp", decimals=0).as_raw_html())
