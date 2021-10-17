import streamlit as st
import base64
import pandas as pd

main_bg = "background.jpg"
main_bg_ext = "jpg"

#code to copy and recycle for making backgrounds
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-size: cover
    }}
</style>
    """,
    unsafe_allow_html=True
)
template = """ <h1 style = "color=:drak gray; text-align:center">DataGeeks </h1>
                </div>""" #allows multiple lines of html
#css colour codes available online, basic css
st.markdown(template,unsafe_allow_html=True)

st.sidebar.title("Select the team member to view their profile")
dropdown = st.sidebar.selectbox("Select one",["","Ayesha","Nadiya","Rebecca"])
if dropdown == "Rebecca":
    st.title("Rebecca Palmer")
    st.header("Work Experience")
    col1, col2, col3 = st.columns(3)
    with col1:
        "Dates"
        "Oct 2018 - Present"
        "Aug 2016 - Oct 2018"
        "Sep 2013 - Aug 2016"
        "Jun 2011 - Aug 2013"
        "Nov 2005 - Jun 2011"
        "Aug 2004 - Nov 2005"
        "Nov 2003 - Jul 2004"
        "Mar 2003 - Nov 2003"

    with col2:
        "Company"
        "Irdeto"
        "Irdeto"
        "Irdeto"
        "Irdeto"
        "Irdeto"
        "Witter Towbars Ltd"
        "Mitras Automotive"
        "Oxford Conversis"
    with col3:
        "Position"
        "Sales Operations Manager"
        "Manager, Sales Support"
        "Manager, Business Services EMEA"
        "Senior Commercial Co-ordinator"
        "Sales Support Administrator"
        "Sales Co-ordinator"
        "Sales & Marketing Co-ordinator"
        "Administrator"
    st.header("Education")
    df_education = pd.read_csv("education.csv")
    df_education.set_index('From')
    st.table(df_education)
    st.header("Personal")
    st.text("British citizen based in the Netherlands with work/residence permit and full driving licence")
    st.text("Experienced in all aspectes of sales operations including sales incentive administration, sales forecasting etc.")
