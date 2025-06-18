# 💬Whats App Chat Analysis📊
A Streamlit web app that analyzes WhatsApp chat exports to uncover user activity patterns, message statistics, media sharing behavior, and more. Built using Python, Pandas, Regex, and Matplotlib.

# 🔍 What This Project Does?

This tool takes your exported WhatsApp chat file and extracts valuable insights such as:
📊 Counting total messages and words exchanged
📸 Detecting number of media files shared
🔗 Identifying how many links were shared in the chat
👥 Highlighting the most active participants
⏳ Showing time-based trends (yearly, monthly, daily, hourly)
🧹 Cleaning and structuring raw exported .txt chat files
🗂️ Preparing data for further analysis and visualization
🤖 Removing sensitive info like phone numbers automatically

Perfect for curious individuals, researchers, or anyone interested in understanding their digital conversations better.


# 🧠 Key Features

 **Feature**                        **Description**
--------------------------------------------------------------------------------------------------------
 📦 File Upload                   Chat.txt` exported WhatsApp chat file directly 
 📈 Top Stats                     Total messages, word count, media files, and links
 🧑‍🧻‍🧑 User Filter              View stats for specific users or entire group
 🔝 Most Active                    Identify top contributors in the chat 
 📅 Time Features                  Breakdown by year, month, day, and hour 
 🩼 Preprocessing                  Cleans raw text, removes phone numbers, extracts metadata 


 ## 🛠️ Tech Stack

🔹 Python        – Core programming language
🔹 Streamlit     – Web framework for interactive dashboards
🔹 Pandas        – Data processing and manipulation
🔹 Matplotlib    – Creating insightful visualizations
🔹 Regex         – Extracting structured patterns from raw text
🔹 URLExtract    – Identifying URLs within chat messages


# 📁 Project Structure

whatsapp-chat-analyzer/
├── App.py              # Streamlit frontend app
├── Preprocessor.py     # Handles cleaning and structuring of data
├── helper.py           # Statistical computations and utilities
├── sample_chat.txt     # (Optional) Example WhatsApp chat file
└── README.md           # Project documentation


# 🗞️ File Descriptions

App.py Main Streamlit app that manages file upload, user inputs, and visual output.

Preprocessor.py Cleans raw text and extracts structured information (users, messages, timestamps, etc.).

helper.py Contains functions to calculate total messages, word counts, media/link shares, and identify most active users.


# 🚀 How to Run Locally

Make sure you have Python 3.7+ and pip installed.

# 🔧 Step 1: Clone the Repository

git clone https://github.com/YOUR_USERNAME/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer

# 📦 Step 2: Install Required Packages

pip install streamlit pandas matplotlib urlextract

# ▶️ Step 3: Run the Streamlit App

streamlit run App.py

You’ll see the app open in your default web browser.

# 📂 How to Export WhatsApp Chat

1. Open the WhatsApp chat (group or personal).
2. Click on the 3 dots → More → Export Chat.
3. Choose "Without Media".
4. Transfer the .txt file to your computer and upload it in the Streamlit app.


# 🚀 Try the App Live

👉 [Click here to open the WhatsApp Chat Analyzer]()

> *(Replace the URL above with your actual Streamlit app deployment link)*
