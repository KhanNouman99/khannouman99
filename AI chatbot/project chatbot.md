
 LSTM Chatbot with Voice Support
 
This project is an intelligent chatbot powered by an LSTM neural network and enhanced with voice input/output capabilities. It allows users to interact via text or voice and receive spoken responses from the bot.

🌟 Features
Trainable with multiple JSON intent files

Intent classification using an LSTM model

Voice input via speech recognition

Text-to-speech output using gTTS

Interactive Gradio UI for both typing and recording voice

Fully customizable and easy to extend

📁 Data Format
The bot uses one or more uploaded JSON files for training. Each file should contain a list of intents, each with:

An intent name

examples of user inputs

Possible responses the bot can give

🚀 How to Use
Launch the notebook in Google Colab or your Python environment.

Upload your intent JSON files when prompted.

The bot trains itself automatically on the uploaded data.

Use the Gradio interface to chat via:

Typing messages

Recording your voice

Listen to the bot's spoken response.

🧠 Model Overview
Built using TensorFlow/Keras

Embedding + LSTM layers for sequential learning

Trained with user-defined intent examples

Label encoding and tokenization handled automatically

🔊 Voice Interaction
Speech Recognition: Converts your voice to text

Text-to-Speech: Bot responses are spoken using gTTS

Responses are played back in .wav format using pydub

📦 Requirements
Make sure the following libraries are installed:

tensorflow

numpy

gradio

speechrecognition

gtts

pydub

🧪 Notes
Retrains every time the notebook is run — consider adding model saving/loading if needed.

Can be adapted to other domains by updating the JSON intent data.

Use clear and diverse examples in your JSON files for better performance.

📄 License
This project is open-source and intended for educational and personal use.