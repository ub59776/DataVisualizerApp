import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Set page config
st.set_page_config(page_title='Data Visualizer App', layout='wide', page_icon='📈')

# Title
st.title('📈  Data Visualizer App')
st.write("")

working_dir = os.path.dirname(os.path.abspath(__file__))

# CSV files 
folder_path = f"{working_dir}/csvfiles"

# Listing all files in the folder
files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# To select a file
selected_file = st.selectbox('Select one file', files, index=None)

if selected_file:
    # path to the file
    file_path = os.path.join(folder_path, selected_file)

    # Read CSV file
    df = pd.read_csv(file_path)

    col1, col2 = st.columns(2)

    columns = df.columns.tolist()

    with col1:
        st.write("")
        st.write("")
        st.write(df.head(6))
        
        st.write("")
        #To select columns for plotting
        x_axis = st.selectbox('Select X-axis ', options=columns+["None"])
        y_axis = st.selectbox('Select Y-axis ', options=columns+["None"])

        plot_list = ['Scatter Plot', 'Distribution Plot', 'Line Plot', 'Bar Chart', 'Count Plot']
        # To select the type of plotting
        plot_type = st.selectbox('Select the Plot Type', options=plot_list)
   

    with col2:
        if st.button('Generate Plot'):
       
            fig, ax = plt.subplots(figsize=(6, 4))

            if plot_type == 'Line Plot':
                sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)

            elif plot_type == 'Scatter Plot':
                sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)

            elif plot_type == 'Bar Chart':
                sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)

            elif plot_type == 'Distribution Plot':
                sns.histplot(df[x_axis], kde=True, ax=ax)
                y_axis='Density'

            elif plot_type == 'Count Plot':
                sns.countplot(x=df[x_axis], ax=ax)
                y_axis = 'Count'

            # Adjust label sizes
            ax.tick_params(axis='x', labelsize=10) 

            ax.tick_params(axis='y', labelsize=10)

            # Title and axis labels size
            plt.title(f'{plot_type} of {y_axis} vs {x_axis}', fontsize=12)

            plt.xlabel(x_axis, fontsize=10)

            plt.ylabel(y_axis, fontsize=10)

            # result
            st.pyplot(fig)