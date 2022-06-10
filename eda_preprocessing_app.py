"""
Create a Streamlit application that a user can enter a data file and uses panda-profiling for as an interactive exploratory data analysis and uses bamboolib package for cleaning the data and returns a python script with the cleaning code
"""
# Importing the main libraries
import streamlit as st
import pandas as pd
import numpy as np
# importing the libraries for data visualization
import matplotlib.pyplot as plt
import seaborn as sns
# importing the library for data profiling
import pandas_profiling


# importing the libraries for data cleaning
import script as script
from bamboolib import *

def main():
    """A data file cleaning and profiling app with Streamlit and Bamboolib packages"""

    st.title('Data processing and profiling')
    st.write("Please select the uploaded file")

    uploaded_file = st.sidebar.file_uploader("Choose a CSV file",type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.sidebar.title("Process the Data")
        st.sidebar.markdown("1. click on any of the button below to conitnue")
        st.sidebar.markdown("2. After using each of the buttons please remember to click the 'Commit Changes' button again")
        st.sidebar.markdown("3. To clear these changes click the 'Reset Data' link in the sidebar")
        st.markdown("Please click the 'Commit Changes' Button")
        st.markdown("After Using the button for proccesing the Data")
        st.markdown("You can also add the code to script editor on the left side of the screen")

        with bam.Bamboo():
            if st.sidebar.button('Converting a column type'):
                # Convert to string
                df = convert_to_str()

            if st.sidebar.button('Checking missing values'):
                # Display data
                show(df)
                # Display missing values
                display_missing_values()

            if st.sidebar.button('Removing duplicates'):
                # Display data
                show(df)
                # Display missing values
                # Checking for duplicate entries
                duplicates()

            if st.sidebar.button('Renaming columns'):
                # Display data
                show(df)
                #check for duplicates
                rename_col(['column_name1','column_name2'])

            if st.sidebar.button('Remove column'):
                # Display data
                show(df)
                # remove a column
                remove_col(['column_name1'])
                # remove multiple columns
                remove_cols(['column_name1','column_name2'])

            if st.sidebar.button('drop row'):
                # Display data
                show(df)
                # Remove a row
                drop_row('index')
                # Remove multiple rows
                drop_rows('index')

            if st.sidebar.button('Filter rows'):
                # Display data
                show(df)
                # Filter rows
                show(df.query('column_name > 5'))

            if st.sidebar.button('filter rows by regex pattern'):
                # Display data
                show(df)
                # Filter rows by regex pattern
                data = show(df[df["column1"].str.contains("pattern")])

            if st.sidebar.button('Adding formula rows'):
                # Display data
                show(df)
                # Add formula rows
                add_formula_row()

            if st.sidebar.button('Deleting formula rows'):
                # Display data
                show(df)
                # Delete formula rows
                add_formula_row()

            if st.sidebar.button('Insert rows'):
                # Display data
                show(df)
                # insert rows
                insert_row()

            if st.sidebar.button('Replace values'):
                # Display data
                show(df)
                # Replacing values
                replace_values()

            if st.sidebar.button('Replace Question marks with value'):
                # Display data
                show(df)
                # Replace Question marks with value in a column
                replace_na()

            if st.sidebar.button('Round values up'):
                # Display data
                show(df)
                # Round values up
                data = round_ndigits()

            if st.sidebar.button('Filtering multiple rows'):
                # Display data
                show(df)
                # Filter multiple rows by regex pattern
                data = show(df[df["column1"].str.contains("pattern", "pattern")])

            if st.sidebar.button('Merge two or more files'):
                # Display data
                show(df)
                # Merge two or more files
                data = merge_files(['file1','file2'])

            if st.sidebar.button('Deleting formula rows'):
                # Display data
                show(df)
                # Delete formula rows
                delete_formula_rows()

            if st.sidebar.button('Unpivot table'):
                # Display data
                show(df)
                # Unpivot table
                unpivot_table()

            if st.sidebar.button('Pivot table'):
                # Display data
                show(df)
                # Pivot table
                pivot_table()

            if st.sidebar.button('Sort values by column'):
                # Display data
                show(df)
                # Pivot table
                pivot_table()

            if st.sidebar.button('Sort rows in dataframe'):
                # Display data
                show(df)
                # Sort rows in dataframe
                sort_rows()

            if st.sidebar.button('Split column'):
                # Display data
                show(df)
                # Split column
                split_col(column = 'Country', separator = ' ')

            if st.sidebar.button('Extract'):
                # Display data
                show(df)
                # Extract
                extract_after_last(column = 'Country', pattern = '[A-Za-z\\s]*', new_name = 'extracted_word')

            if st.sidebar.button('Extract after first_occurence'):
                # Display data
                show(df)
                # Extract after first occurence
                extract_after_first(column = 'Country', pattern = '[A-Za-z\\s]*', new_name = 'extracted_word')

            if st.sidebar.button('Concat'):
                # Display data
                show(df)
                # Concat
                concat_cols(['column1', 'column2'], new_name = 'concatinated_column', sep = ' - ')

            if st.sidebar.button('Concat with delimiter'):
                # Display data
                show(df)
                # Concat with delimiter
                concat_cols_with_delimiter(base_col_name = 'State', delimiter = ' ', new_name = 'State2', names = ['State', 'Country'])

            if st.sidebar.button('Count occurences'):
                # Display data
                show(df)
                # Count occurences in a column
                count_occurences(column = 'column_name')

            if st.sidebar.button('Replace values in column'):
                # Display data
                show(df)
                # Replace values in column
                replace_values(replace_what = 'Brasil', replace_with = 'Brazil', columns = 'Country')

            if st.sidebar.button('Replace values in multiple column'):
                # Display data
                show(df)
                # Replace values in multiple columns
                replace_values_in_multiple_cols(replace_what = 'Brasil', replace_with = 'Brazil', columns = ['column1', 'column2'])

            if st.sidebar.button('Replace values by regex'):
                # Display data
                show(df)
                # Replace values by regex
                replace_values_by_regex(pattern = ',' , replacement = '.', columns = 'column_name')

            if st.sidebar.button('Strip whitespace'):
                # Display data
                show(df)
                # Strip whitespace
                strip_whitespace(columns = 'column_name')


            if st.sidebar.button('Capitalize text'):
                # Display data
                show(df)
                # Capitalize text
                capitalize_text(column = 'column_name')

            if st.sidebar.button('Write to Excel'):
                # Display data
                show(df)
                # Capitalize text
                write_to_excel('Address')

            if st.sidebar.button('Write to CSV'):
                # Display data
                show(df)
                # Write to CSV
                write_to_csv('Address')

            if st.sidebar.button( 'Apply function to column'):
                # Display data
                show(df)
                # Apply function to column
                apply_func_to_col(column = 'column_name', func = func)

            if st.sidebar.button( 'Apply function to multiple cols'):
                # Display data
                show(df)
                # Apply function to multiple cols
                apply_func_to_multiple_cols(columns = ['column_name1','column_name2'], func = func)

            if st.sidebar.button( 'Apply function to rows'):
                # Display data
                show(df)
                # Apply function to rows
                apply_func_to_rows([row_number], func = func)

            if st.sidebar.button( 'Apply function to dataframe'):
                # Display data
                show(df)
                # Apply function to dataframe
                apply_func_to_dataframe(func = func)

            if st.sidebar.button( 'Delete Data'):

   #                # Delete data
                # Delete data
                delete_rows_with_value('column', 'value')
                remove_outliers()

            if st.sidebar.button('Show Profile Report'):
                data_type = st.radio("Please selectd data type  to view", ('html', 'json', 'py'))
                html = pandas_profiling.ProfileReport(df)
                if data_type == 'html':
                    st.title("Data Profiling Report- html")
                    # body = st.empty()
                    # body.use_markdown(html)
                    st.markdown(html, unsafe_allow_html=True)


            if st.sidebar.button('Show Data'):
                if st.checkbox('Preview Spark Data'):
                    st.write(df.head(5))
                    if st.checkbox('Show Shape of Data'):
                        st.write(df.shape)
                        if st.checkbox('Show Summary of Data'):
                            st.write(df.describe())
                else:
                    st.title('Data')
                    st.table(df)

                # st.write(df)



                if st.checkbox('Preview Spark Data'):
                    st.write(df.head(5))
                    if st.checkbox('Show Shape of Data'):
                        st.write(df.shape)
                        if st.checkbox('Show Summary of Data'):
                            st.write(df.describe())


                else:
                    st.title('Data')
                    st.table(df)


                if st.checkbox('Preview Spark Data'):
                    st.write(df.head(5))
                    if st.checkbox('Show Shape of Data'):
                        st.write(df.shape)
                        if st.checkbox('Show Summary of Data'):
                            st.write(df.describe())

if __name__ == '__main__':
    main()