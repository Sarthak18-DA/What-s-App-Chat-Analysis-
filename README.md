# 💬 WhatsApp Chat Analysis 📊

A **Streamlit web app** that analyzes WhatsApp chat exports to uncover user activity patterns, message statistics, media sharing behavior, and more.

> Built with Python, Pandas, Regex, and Matplotlib.

🔗 **Live App**: [Click here to try it out](https://lambf6nmwdagbkhfwuzkfs.streamlit.app/)  
📁 Sample Chat File: chat.txt`uploaded

---

## 🔍 What This Project Does

This tool takes your exported WhatsApp chat file and extracts valuable insights such as:

- 📊 Total messages and word count
- 📸 Media files shared
- 🔗 Links shared
- 👥 Most active participants
- 📆 Time-based trends (yearly, monthly, daily, hourly)
- 🧹 Cleans and structures raw `.txt` chat exports
- 🗂️ Prepares data for visual storytelling
- 🔒 Automatically removes sensitive info like phone numbers

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
├── chat.txt     # (Optional) Example WhatsApp chat file
└── README.md           # Project documentation


# 🗞️ File Descriptions

app.py Main Streamlit app that manages file upload, user inputs, and visual output.

Preprocessor.py Cleans raw text and extracts structured information (users, messages, timestamps, etc.).

helper.py Contains functions to calculate total messages, word counts, media/link shares, and identify most active users.


# 🚀 How to Run Locally

Make sure you have Python 3.7+ and pip installed.

### 🔧 Step 1: Clone the Repository

```bash
git clone https://github.com/Sarthak18-DA/What-s-App-Chat-Analysis-.git
cd What-s-App-Chat-Analysis-

# 📦 Step 2: Install Required Packages
pip install -r requirements.txt
pip install streamlit pandas matplotlib urlextract

# ▶️ Step 3: Run the Streamlit App

streamlit run App.py

You’ll see the app open in your default web browser.

# 📂 How to Export WhatsApp Chat

1. Open the WhatsApp chat (group or personal).
2. Click on the 3 dots → More → Export Chat.
3. Choose "Without Media".
4. Transfer the .txt file to your computer and upload it in the Streamlit app.

# 👤 About the Author

Sarthak More – Data Analyst | Streamlit/PowerBI Developer | Python Enthusiast
Hi there! 👋 I'm Sarthak More, a data analyst passionate about transforming raw data into interactive and insightful web applications. This WhatsApp Chat Analyzer project reflects my interest in combining Python, Streamlit, and data science to create tools that make everyday data more understandable and fun to explore.

# 🔍 What I Do:

Develop interactive dashboards using Streamlit and Power BI

Clean, analyze, and visualize data using Python, Pandas, Matplotlib, and SQL

Create real-world projects focused on user behavior, business metrics, and analytics

📫 Let’s Connect:

GitHub: @Sarthak18-DA

LinkedIn: Sarthak More

🛠️ Stay Tuned!
I’m constantly working on new ideas, tools, and data experiments. Star ⭐ this repo and follow me for more!
