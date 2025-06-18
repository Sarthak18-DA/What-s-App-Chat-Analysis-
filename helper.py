import pandas as pd
from wordcloud import WordCloud
from collections import Counter
import emoji
import re

def fetch_stats(selected_user, df):
    if selected_user != "Overall":
        df = df[df["Users"] == selected_user]

    num_messages = df.shape[0]
    words = sum(len(msg.split()) for msg in df["Message"])
    media = df[df["Message"].str.lower() == "<media omitted>"].shape[0]

    link_pattern = r'(https?://\S+|www\.\S+)'
    links = df["Message"].str.contains(link_pattern, na=False).sum()

    return num_messages, words, media, links

def most_busy_users(df):
    x = df["Users"].value_counts().head()
    new_df = round((df["Users"].value_counts() / df.shape[0]) * 100, 2).reset_index()
    new_df.columns = ["User", "Percentage"]
    return x, new_df

def create_wordcloud(selected_user, df):
    if selected_user != "Overall":
        df = df[df["Users"] == selected_user]
    temp = df[df["Message"] != "<media omitted>"]
    text = " ".join(temp["Message"])
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color="white")
    return wc.generate(text)

def most_common_words(selected_user, df):
    if selected_user != "Overall":
        df = df[df["Users"] == selected_user]

    words = []
    for msg in df["Message"]:
        words.extend([word for word in msg.lower().split() if word not in ("<media omitted>", "https", "http") and not word.startswith("www.")])

    most_common = pd.DataFrame(Counter(words).most_common(20), columns=["Word", "Count"])
    return most_common

def emoji_helper(selected_user, df):
    if selected_user != "Overall":
        df = df[df["Users"] == selected_user]
    emojis = []
    for msg in df["Message"]:
        emojis.extend(c for c in msg if c in emoji.EMOJI_DATA)
    return pd.DataFrame(Counter(emojis).most_common(), columns=["Emoji", "Count"])

def monthly_timeline(selected_user, df):
    if selected_user != "Overall":
        df = df[df["Users"] == selected_user]
    timeline = df.groupby(["Year", "Month_Num", "Month"]).count()["Message"].reset_index()
    timeline["time"] = timeline["Month"] + "-" + timeline["Year"].astype(str)
    return timeline.rename(columns={"Message": "message_count"})

def daily_timeline(selected_user, df):
    if selected_user != "Overall":
        df = df[df["Users"] == selected_user]
    return df.groupby("only_date").count()["Message"].reset_index().rename(columns={"Message": "message_count"})

def week_activity_map(selected_user, df):
    if selected_user != "Overall":
        df = df[df["Users"] == selected_user]
    return df["Day_Name"].value_counts()

def month_activity_map(selected_user, df):
    if selected_user != "Overall":
        df = df[df["Users"] == selected_user]
    return df["Month"].value_counts()

def activity_heatmap(selected_user, df):
    if selected_user != "Overall":
        df = df[df["Users"] == selected_user]
    heatmap = df.pivot_table(index="Day_Name", columns="Hour", values="Message", aggfunc="count").fillna(0)
    return heatmap
