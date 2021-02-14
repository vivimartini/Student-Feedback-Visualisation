#Imports
import streamlit as st
import pandas as pd
import plotly.express as px

#configuration
st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Student Feedback Visualisation App")

# Add sidebar
st.sidebar.subheader("Visualisation settings")

# Setup file upload
global df
uploaded_file = st.sidebar.file_uploader(label="Upload your CSV file", type = ['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    #Show raw data
    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(df)
    
    # Setup sidebar
    select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='1')
    year_group = st.sidebar.selectbox('Year Group',['Year 7','Year 8','Year 9','Year 10','Year 11','Year 12','Year 13'], key='1')
    date = st.sidebar.date_input("Lesson date:")
    st.write(date)
    d = str(date)
    teacher = st.sidebar.selectbox('Teacher',['Mr Thomson','Ms Rivas','Ms Taylor','Mr Tang'],key='1')
    
    #Data filtering for Mr Thomson
    year_7_MrT = df[(df['Year Group']=='Year 7') & (df['Teacher']=='Mr Thomson') & (df['Date']== d)]
    year_7_MrT.head()
    year_8_MrT = df[(df['Year Group']=='Year 8') & (df['Teacher']=='Mr Thomson') & (df['Date']== d)]
    year_8_MrT.head()
    year_9_MrT = df[(df['Year Group']=='Year 9') & (df['Teacher']=='Mr Thomson') & (df['Date']== d)]
    year_9_MrT.head()
    year_10_MrT = df[(df['Year Group']=='Year 10') & (df['Teacher']=='Mr Thomson') & (df['Date']== d)]
    year_10_MrT.head()
    year_11_MrT = df[(df['Year Group']=='Year 11') & (df['Teacher']=='Mr Thomson') & (df['Date']== d)]
    year_11_MrT.head()
    year_12_MrT = df[(df['Year Group']=='Year 12') & (df['Teacher']=='Mr Thomson') & (df['Date']== d)]
    year_12_MrT.head()
    year_13_MrT = df[(df['Year Group']=='Year 13') & (df['Teacher']=='Mr Thomson') & (df['Date']== d)]
    year_13_MrT.head()
    
    # Data display for Mr Thomson
    # Year 7
    if select == 'Pie chart' and year_group == 'Year 7' and teacher == 'Mr Thomson':
        st.subheader("How would you rate your lesson overall?")
        fig1_7 = px.pie(year_7_MrT, names='Q1')
        st.plotly_chart(fig1_7)
        st.subheader("Was the lesson fun and interactive?")
        fig2_7 = px.pie(year_7_MrT, names='Q2')
        st.plotly_chart(fig2_7)
        st.subheader("Was the lesson content interesting and engaging?")
        fig3_7 = px.pie(year_7_MrT, names='Q3')
        st.plotly_chart(fig3_7)
        st.subheader("Were you comfortable with the pace of the lesson?")
        fig4_7 = px.pie(year_7_MrT, names='Q4')
        st.plotly_chart(fig4_7)
        st.subheader("Did your teacher explore the real-world applications of what you learnt?")
        fig5_7 = px.pie(year_7_MrT, names='Q5')
        st.plotly_chart(fig5_7)
        st.subheader("Pupil comments")
        comment_7 = (year_7_MrT['What do you think could have been better?'])
        st.write(comment_7)
        
    # Year 8
    if select == 'Pie chart' and year_group == 'Year 8' and teacher == 'Mr Thomson':
        st.subheader("How would you rate your lesson overall?")
        fig1_8 = px.pie(year_8_MrT, names='Q1')
        st.plotly_chart(fig1_8)
        st.subheader("Was the lesson fun and interactive?")
        fig2_8 = px.pie(year_8_MrT, names='Q2')
        st.plotly_chart(fig2_8)
        st.subheader("Was the lesson content interesting and engaging?")
        fig3_8 = px.pie(year_8_MrT, names='Q3')
        st.plotly_chart(fig3_8)
        st.subheader("Were you comfortable with the pace of the lesson?")
        fig4_8 = px.pie(year_8_MrT, names='Q4')
        st.plotly_chart(fig4_8)
        st.subheader("Did your teacher explore the real-world applications of what you learnt?")
        fig5_8 = px.pie(year_8_MrT, names='Q5')
        st.plotly_chart(fig5_8)
        st.subheader("Pupil comments")
        comment_8 = (year_8_MrT['What do you think could have been better?'])
        st.write(comment_8)
    
    # Year 9
    if select == 'Pie chart' and year_group == 'Year 9' and teacher == 'Mr Thomson':
        st.subheader("How would you rate your lesson overall?")
        fig1_9 = px.pie(year_9_MrT, names='Q1')
        st.plotly_chart(fig1_9)
        st.subheader("Was the lesson fun and interactive?")
        fig2_9 = px.pie(year_9_MrT, names='Q2')
        st.plotly_chart(fig2_9)
        st.subheader("Was the lesson content interesting and engaging?")
        fig3_9 = px.pie(year_9_MrT, names='Q3')
        st.plotly_chart(fig3_9)
        st.subheader("Were you comfortable with the pace of the lesson?")
        fig4_9 = px.pie(year_9_MrT, names='Q4')
        st.plotly_chart(fig4_9)
        st.subheader("Did your teacher explore the real-world applications of what you learnt?")
        fig5_9 = px.pie(year_9_MrT, names='Q5')
        st.plotly_chart(fig5_9)
        st.subheader("Pupil comments")
        comment_9 = (year_9_MrT['What do you think could have been better?'])
        st.write(comment_9)

    # Year 10
    if select == 'Pie chart' and year_group == 'Year 10' and teacher == 'Mr Thomson':
        st.subheader("How would you rate your lesson overall?")
        fig1_10 = px.pie(year_10_MrT, names='Q1')
        st.plotly_chart(fig1_10)
        st.subheader("Was the lesson fun and interactive?")
        fig2_10 = px.pie(year_10_MrT, names='Q2')
        st.plotly_chart(fig2_10)
        st.subheader("Was the lesson content interesting and engaging?")
        fig3_10 = px.pie(year_10_MrT, names='Q3')
        st.plotly_chart(fig3_10)
        st.subheader("Were you comfortable with the pace of the lesson?")
        fig4_10 = px.pie(year_10_MrT, names='Q4')
        st.plotly_chart(fig4_10)
        st.subheader("Did your teacher explore the real-world applications of what you learnt?")
        fig5_10 = px.pie(year_10_MrT, names='Q5')
        st.plotly_chart(fig5_10)
        st.subheader("Pupil comments")
        comment_10 = (year_10_MrT['What do you think could have been better?'])
        st.write(comment_10)
    
    # Year 11
    if select == 'Pie chart' and year_group == 'Year 11' and teacher == 'Mr Thomson':
        st.subheader("How would you rate your lesson overall?")
        fig1_11 = px.pie(year_11_MrT, names='Q1')
        st.plotly_chart(fig1_11)
        st.subheader("Was the lesson fun and interactive?")
        fig2_11 = px.pie(year_11_MrT, names='Q2')
        st.plotly_chart(fig2_11)
        st.subheader("Was the lesson content interesting and engaging?")
        fig3_11 = px.pie(year_11_MrT, names='Q3')
        st.plotly_chart(fig3_11)
        st.subheader("Were you comfortable with the pace of the lesson?")
        fig4_11 = px.pie(year_11_MrT, names='Q4')
        st.plotly_chart(fig4_11)
        st.subheader("Did your teacher explore the real-world applications of what you learnt?")
        fig5_11 = px.pie(year_11_MrT, names='Q5')
        st.plotly_chart(fig5_11)
        st.subheader("Pupil comments")
        comment_11 = (year_11_MrT['What do you think could have been better?'])
        st.write(comment_11)
    
    # Year 12
    if select == 'Pie chart' and year_group == 'Year 12' and teacher == 'Mr Thomson':
        st.subheader("How would you rate your lesson overall?")
        fig1_12 = px.pie(year_12_MrT, names='Q1')
        st.plotly_chart(fig1_12)
        st.subheader("Was the lesson fun and interactive?")
        fig2_12 = px.pie(year_12_MrT, names='Q2')
        st.plotly_chart(fig2_12)
        st.subheader("Was the lesson content interesting and engaging?")
        fig3_12 = px.pie(year_12_MrT, names='Q3')
        st.plotly_chart(fig3_12)
        st.subheader("Were you comfortable with the pace of the lesson?")
        fig4_12 = px.pie(year_12_MrT, names='Q4')
        st.plotly_chart(fig4_12)
        st.subheader("Did your teacher explore the real-world applications of what you learnt?")
        fig5_12 = px.pie(year_12_MrT, names='Q5')
        st.plotly_chart(fig5_12)
        st.subheader("Pupil comments")
        comment_12 = (year_12_MrT['What do you think could have been better?'])
        st.write(comment_12)
    
    # Year 13
    if select == 'Pie chart' and year_group == 'Year 13' and teacher == 'Mr Thomson':
        st.subheader("How would you rate your lesson overall?")
        fig1_13 = px.pie(year_13_MrT, names='Q1')
        st.plotly_chart(fig1_13)
        st.subheader("Was the lesson fun and interactive?")
        fig2_13 = px.pie(year_13_MrT, names='Q2')
        st.plotly_chart(fig2_13)
        st.subheader("Was the lesson content interesting and engaging?")
        fig3_13 = px.pie(year_13_MrT, names='Q3')
        st.plotly_chart(fig3_13)
        st.subheader("Were you comfortable with the pace of the lesson?")
        fig4_13 = px.pie(year_13_MrT, names='Q4')
        st.plotly_chart(fig4_13)
        st.subheader("Did your teacher explore the real-world applications of what you learnt?")
        fig5_13 = px.pie(year_13_MrT, names='Q5')
        st.plotly_chart(fig5_13)
        st.subheader("Pupil comments")
        comment_13 = (year_13_MrT['What do you think could have been better?'])
        st.write(comment_13)