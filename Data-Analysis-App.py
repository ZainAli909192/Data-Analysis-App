import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)



path='E:\\All python\\Data Analysis\\Data sets\\youtube_dataset.csv'
data=pd.read_csv(path)


# upload data set 
upload=st.file_uploader("Upload your dataset (in CSV formate)")
if upload is not None:
    data=pd.read_csv(upload)
   
    if st.checkbox("Preview Data set"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
            
    if st.checkbox("Shape"):
        data_shape=st.radio("What dimension?" ,("Rows", "column") )
        if data_shape=='Rows':
            st.write("Number of Rows: ",data.shape[0])
        else:
            st.write("Number of Columns: ",data.shape[1])
   
   
    if st.checkbox("Overal summary of dataset"):
        st.write(data.describe())
        if st.button("All columns include?"):
            st.write(data.describe(include='all'))
        
    if st.checkbox("Data type of each column?"):
        st.text('DataTypes')
        st.write(data.dtypes)

    if st.checkbox("Sort"): 
        data_column=st.radio("Please select Column: ",(data.columns))
        if(data_column is not None):
            data_order=st.radio("Pick the order: ",("Ascending","Descending"))
            if data_order=='Ascending':
                st.text('Sorting in ascending')
                st.write(data.sort_values(by=data_column))
            elif data_order=='Descending':
                st.text('Sorting in Descending')
                st.write(data.sort_values(by=data_column, ascending=False))

    if st.checkbox("Find null values"):
        test=data.isnull().values.any()
        if test==True:
           sns.heatmap(data.isnull())     
           st.pyplot()
           rem=st.selectbox("Do you want to remove them?",("Select one","Yes","No"))
           
           if rem=="Yes":
                data=data.dropna()
                sns.heatmap(data.isnull())     
                st.pyplot()
                st.success("Null values are removed")
           elif rem=="No":
                st.text("Ok Good luck with your Null values")
     
        else:
            st.success("Congratulations!!! No missing values")
    
    if st.checkbox("Find Duplicate values"):  
        test=data.duplicated().values.any()
        if test==True:  
            st.warning("Duplicated values found.")
            dup=st.selectbox("Do you want to remove them?","Select one","Yes","No")
            if dup=="Yes":
                data=data.drop_duplicates()
                st.success("Duplicated values are removed")
            elif dup=="No":
                st.text("Ok Good luck with your duplicated values")
        else:
            st.success("Congratulations! No Duplicate value is present")
    if st.button("Save updated Data file"):
        open('streamlit.csv','w').write(data.to_csv())
        st.text("File is saved in your current folder...")
st.title('Data Anlaysis project')
st.subheader('Data Analysis using python & streamlit')
