import streamlit as st 

st.title("Stream Demo App By Dino the denver")

st.header(" matoru seetheye katilekkeyakunnu....")

st.subheader("dhushtanam durvidhi veendum...")

st.text("enthinu veroru sooryodayam..")


st.success(" This is success")
st.warning(" This is a clear warning")
st.info("This is some info who cares..")
st.error('some error it seems')

if st.checkbox("select/unselect"):
    st.text("You have selected")
else:
    st.text("just click the damn button you!")
    

state = st.radio("what is your hatered colour ", ("black", "yellow", 'red'))

    
if state == "yellow":
    st.error("why did you select my color??")

occupation = st.selectbox("whats your job buddy?", ("nothing", "ceo", "founder", "athelete", '**rn star'))

st.text(f"selected option is {occupation}")

st.button("example Button")

if st.button:
    st.error("Damnnnnnnnn!!!!")
else:
    st.warning("whatever")


st.sidebar.header("Heading of sidebar")
st.sidebar.text("by somebody")

