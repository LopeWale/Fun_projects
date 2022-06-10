"""
Create a Streamlit blog writing application that a user can enter a research topic in the application which then use the research topic as a prompt in a GET request to OpenAi's text-davinci-002 model API to generate a blog(or articles) on the topic then formats all the paragraphs together in a structured manner for a blog and returns the complete blog as a text file.
"""
# Import the required libraries
import streamlit as st
import requests
import markdown

# Define the function to get the user input
def get_input():
    """Gets the user input from the sidebar"""
    # Get the user input
    topic = st.sidebar.text_input("Research Topic: ")
    n_paragraphs = st.sidebar.number_input("Number of Paragraphs: ",min_value=1,max_value=5,value=1)
    save_as = st.sidebar.text_input("Save the blog as: ")
    # return the user input
    return topic,n_paragraphs,save_as

# Define the function to make a request to the API
def openai_request(topic,n_paragraphs):
    # Create the request body
    data = {
      "prompt": topic,
      "max_tokens": 1000000,
      "temperature": 1.0,
      "top_p": 0.9,
      "n": n_paragraphs
    }

    # Make the request to the API
    response = requests.post('https://api.openai.com/v1/engines/davinci/completions', json=data, headers={"Authorization": "Bearer sk-mf0tEZjM8ZHtFjQx1SgkcW6"})

    # Extract the response body
    body = response.json()

    # Extract the text and the rest of the response
    text, response = body["choices"][0]["text"], body

    # Format the text
    text = markdown.markdown(text, extensions=["nl2br", "fenced_code"])

    # Return the text and the response
    return text, response

def get_article(topic,n_paragraphs):
# Define the function to get the article
    """Makes a request to the API and returns the article and the response"""
    # Make a request to the API
    article, response = openai_request(topic,n_paragraphs)

    # Return the article and the response
# Define the main function
    return article, response

def main():
    """Main function of the app"""

    # Set the title of the app
    st.title("Blog-Me")

    # Write a markdown intro
    st.markdown("""
    This is an app to generate a blog given a research topic.

    You can enter your research topic in the sidebar and click the "Submit" button to generate a blog based on the topic.
    """)

    st.markdown("""
    The blog is generated using [OpenAI's GPT-3 API](https://beta.openai.com/docs/api-overview)
    """)

    # Get the user input
    topic,n_paragraphs,save_as = get_input()

    # Display the user input
    st.write(f"Research Topic: {topic}")
    st.write(f"Number of Paragraphs: {n_paragraphs}")

    # If the "Submit" button is pressed
    if st.sidebar.button("Submit"):

        # Get the article
        article, response = get_article(topic,n_paragraphs)
        st.write(f"Generated Blog: \n{article}")
        st.write(f"API response: {response}")

        # Save the article
        with open(f'{save_as}.txt', 'w') as f:
            f.write(f'{article}')

    # download the file
    st.sidebar.markdown("Download the file:")
    file_selector()


if __name__ == "__main__":
    main()