#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import plotly.graph_objects as go
import prj2_0415 as prj2

#######################
# Page configuration
st.set_page_config(
    page_title="US Educated Population Dashboard",
    page_icon="🎓 ",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")


#######################
# Load data
data_income_total = pd.read_csv('us-income.csv')
data_amount = pd.read_csv('us-population-amount.csv')
data_income = pd.read_csv('us-population_income_total.csv')
pop_per = pd.read_csv('us-population-perc.csv')

#######################
# Sidebar
with st.sidebar:
    st.title('US Population with BA Degree🎓 and Median Earnings💴 Dashboard')
    color_theme = ['blues']
    major_list = ['Computers, Mathematics and Statistics','Biological, Agricultural, and Environmental Sciences', 'Physical and Related Sciences', 'Psychology', 'Social Sciences', 'Engineering','Multidisciplinary Studies', 'Science and Engineering Related Fields', 'Business', 'Education', 'Literature and Languages','Liberal Arts and History', 'Visual and Performing Arts', 'Communications','Other']
    gender_list = ['Male', 'Female']
    field_list = ['Total', 'STEM', 'STEM Related', 'Business', 'Education', 'Humanities']

    selected_major = st.selectbox('Select a Major', major_list)
    selected_field = st.selectbox('Select a Field', field_list)
    df_selected_pop = prj2.pop_diff(pop_per, 'population_over_25_with_BA')
    df_selected_pop = df_selected_pop.sort_values(by="field", ascending=False)
    df_selected_earn = data_income_total[1:53]
    df_selected_earn = df_selected_earn.sort_values(by="Total", ascending=False)


#######################
# Choropleth map
def make_choropleth(input_df, input_column, title, color):
    fig = go.Figure(data=go.Choropleth(
        locations=input_df['state_abbrev'], # Spatial coordinates
        # z = data_trans[12].str.replace(',', '').astype(float), # Data to be color-coded
        z = input_df[input_column],
        locationmode = 'USA-states', # set of locations match entries in `locations`
        colorscale = color,
        colorbar_title = title,
    ))

    fig.update_layout(
        geo_scope='usa', # limite map scope to USA
    )
    return fig



#######################
# Dashboard Main Panel
col = st.columns((6, 4, 1), gap='small')

with col[0]:
    st.markdown('#### 2022 US Population of Selected Majors by States')
    
    choropleth = make_choropleth(data_income_total, selected_major, "Population", "armyrose")
    st.plotly_chart(choropleth, use_container_width=True)

with col[0]:
    st.markdown('#### 2022 US Gender difference in Population of Selected Fields by States')
    field = selected_field.replace(" ","_").lower()
    gender_diff = prj2.calculate_gender_diff_pop(data_amount,field)  
    choropleth2 = make_choropleth(gender_diff, 'gender_diff', "%", "blues")
    st.plotly_chart(choropleth2, use_container_width=True)

with col[0]:
    st.markdown('#### 2022 US Gender difference in Earnings of Selected Majors by States')
    gender_diff_earning = prj2.calculate_gender_earning(data_income_total,selected_major)
    choropleth3 = make_choropleth(gender_diff_earning, 'gender_diff', "%", "sunset" )
    st.plotly_chart(choropleth3, use_container_width=True)

with col[0]:    
    with st.expander('About the Data', expanded=True):
        st.write('''
            - Data: [U.S. Census Bureau, American Community Survey (ACS)](https://www.census.gov/programs-surveys/acs).
            - Notes: 
                 (1) Gender difference is the difference of population and earnings between males and females.
                 (2) Gender difference in popluation is calculated by fields while gender difference in earnings is by major. 
            ''')

    
with col[1]:
    st.markdown('#### Top States with Percentage of Population over 25 years that have a BA degree')

    st.dataframe(df_selected_pop,
                 column_order=("state_abbrev", "field"),
                 hide_index=True,
                 width=None,
                 column_config={
                    "states": st.column_config.TextColumn(
                        "States",
                    ),
                    "population": st.column_config.ProgressColumn(
                        "Population over 25 years old",
                        format="%f",
                        min_value=0,
                        max_value=max(df_selected_pop.field),
                     )}
                )
    
    st.markdown('#### Top States with Earnings of People over 25 years old that have a BA degree')

    st.dataframe(df_selected_earn,
                 column_order=("state_abbrev", "Total"),
                 hide_index=True,
                 width=None,
                 column_config={
                    "states": st.column_config.TextColumn(
                        "States",
                    ),
                    "population": st.column_config.ProgressColumn(
                        " Earnings of Population over 25 years old that have a BA degree",
                        format="%f",
                        min_value=0,
                        max_value=max(df_selected_earn.Total),
                     )}
                 )


    

