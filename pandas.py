import streamlit as st 

st.set_page_config(
    page_title="Pandas Basics",
    page_icon="ℹ️",
    layout="wide"
)

st.title(":rainbow[Pandas Basics]",text_alignment="center")
st.divider()

st.subheader(":blue[Read File]",text_alignment="center")
st.html("""
    <pre style="background-color: aqua; color: black;">
                            df = pd.read_csv("data.csv")
                            df = pd.read_json("data.json")
                            df = pd.read_excel("data.xlsx")
    </pre>""")

st.divider()

st.subheader(":green[Create DataFrame]",text_alignment="center")
st.html("""
    <pre style="background-color: aqua; color: black;">
                            df = pd.DataFrame({
                                "Name":["Rohan","Raju","Rahul","Karan"],
                                "Age":[13,12,10,11],
                                "Job":["AI/ML","CA","Engineer","Doctor"]
                            })
                            print(df)        
    </pre>
""")
st.divider()

st.subheader(":red[Describe & Info]",text_alignment="center")
st.html("""
    <pre style="background-color: aqua; color: black;">
                            df = pd.DataFrame({
                                "Name":["Rohan","Raju","Rahul","Karan"],
                                "Age":[13,12,10,11],
                                "Job":["AI/ML","CA","Engineer","Doctor"]
                            })
                            print(df.describe()) 
                            print(df.info())       
    </pre>
""")
st.divider()

st.subheader(":yellow[Save File]",text_alignment="center")
st.html("""
    <pre style="background-color: aqua; color: black;">
                            df = pd.DataFrame({
                                "Name":["Rohan","Raju","Rahul","Karan"],
                                "Age":[13,12,10,11],
                                "Job":["AI/ML","CA","Engineer","Doctor"]
                            })
                             
                            df.to_csv("data.csv",index=False)       
                            df.to_json("data.json")
                            df.excel("data.xlsx",index=False)
    </pre>                  
""")
st.divider()

st.subheader("Data Preview",text_alignment="center")
st.html("""
    <table style="color: deeppink;">
        <tr><th>Name</th><th>Age</th><th>Job</th></tr>
        <tr><td>Rohan</td><td>13</td><td>AI/ML</td></tr>
        <tr><td>Raju</td><td>12</td><td>CA</td></tr>
        <tr><td>Rahul</td><td>10</td><td>Enginner</td></tr>
        <tr><td>Karan</td><td>11</td><td>Doctor</td></tr>
    </table>        
""")