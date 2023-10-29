# yaChatApp Readme.md

## Description

Welcome to yaChatApp! This application is a chat-based conversational agent built using Python, Streamlit, and OpenAI. The app allows you to interact with a virtual assistant, save your chat history, and even load previous conversations.

## Installation

1. **Clone the Repository**
    ```
    git clone https://github.com/YourUsername/yaChatApp.git
    ```

2. **Navigate to Project Directory**
    ```
    cd yaChatApp
    ```

3. **Install Dependencies**
    ```
    pip install -r requirements.txt
    ```

4. **OpenAI API Key and .Gitignore**

    1. In the root directory, create a file named `.OAI_KEY` and place your OpenAI API Key.
    2. Create a file called .gitignore and add the `.OAI_KEY` file to the list so you don't accidentally upload your api key.

5. **Run the App**
    ```
    streamlit run yaChatApp.py
    ```

## Save/Load Steps

### Save Chat History

The application automatically saves your conversation history in the `./chats/` directory. Each conversation will have a unique filename that includes a timestamp, formatted like `convo_MonthDate_Hour_Minute_SecondsAM-PM`.

### Load Chat History

You can load a previous chat history using the `--load_chat` command-line argument followed by the filename you want to load.

For example:
```bash
streamlit run app.py -- --load_chat ./chats/convo_Oct29_12_03_45am
```

This will load the chat history from the file `convo_Oct29_12_03_45am`.
> Note: because of how streamlit uses query paramaters in the command line it's required to have the double double-dashes. 

### Exiting yaChatApp

Ending the chat is two steps:
1. Close the chat window
2. In the terminal type control-c to cancel the process (or simply close the terminal)


## Feedback

If you encounter any issues or have any questions, please open an issue on GitHub. Contributions are also welcome!

Thank you for using yaChatApp! We hope you have an enjoyable experience.