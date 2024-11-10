import streamlit as st
st.set_page_config(page_title='Splunk Integration',layout='centered',page_icon=":wave:")
st.header("Splunk UX Integration")
st.title("A Web UX to fetch logs across markets")
st.write("Hi there!")
st.write("[View here](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/)")
st.write("---")
name = "Balaji"
with st.form("Query_Form"):
    column1,column2 = st.columns(2)
    with column1:
        options = st.selectbox("Specify Market",("ACC","MCC","RDC"))
        options = st.selectbox("Specify Component",("GDM","Rec","Inv"))
        options = st.selectbox("Specify Timeframe",("15 minutes","30 minutes","60 minutes","4 hours","24 hours","48 hours","7 days"))
        st.text_input(label='Specify Search Corrleation ID')
        st.write("Or")
        st.text_input(label='Specify Search Keyword')
    with column2:
        st.date_input(label='Select Date Range from')
        st.date_input(label='Select Date Range To')
        st.time_input(label='Select Time Range from',step=1800)
        st.time_input(label='Select Time Range to',step=1800)
    st.form_submit_button(label="Fetch")


    

