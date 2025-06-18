import pandas as pd
from emoji import EMOJI_DATA
from collections import Counter

def fetch_stats(selected_user, df):
    # Filter by selected user if not 'OverAll'
    if selected_user != "OverAll":
        df = df[df["Users"] == selected_user]
        
    # Fetch number of messages
    num_messages = df.shape[0]
    
    # Fetch number of words
    words = []
    for message in df["Message"]:
        words.extend(message.split())
        
    # Fetch Media Share    
    num_media_messages = df[df["Message"].str.strip().str.lower() == "<media omitted>"].shape[0]
    
    # Fetch Links Shared
    link_pattern = r'(https?://\S+|www\.\S+)'  # Regex for detecting links
    links = df["Message"].str.contains(link_pattern, na=False, case=False).sum()
    
    return num_messages, len(words), num_media_messages, links

def most_busy_users(df):
    # Get top users by message count
    x = df["Users"].value_counts().head()
    
    # Calculate percentage of messages sent by each user
    new_df = (
        (df["Users"].value_counts(normalize=True) * 100)
        .round(2)
        .reset_index()
        .rename(columns={"index": "Names", "Users": "Percentage"})
    )
    
    return x, new_df  

def emoji_helper(selected_user, df):
    # Filter by selected user if not 'OverAll'
    if selected_user != "OverAll":
        df = df[df["Users"] == selected_user]
        
    emojis = []

    # Extract emojis from messages
    for message in df["Message"]:
        emojis.extend([c for c in message if c in EMOJI_DATA])
    
    # Create DataFrame with emoji counts
    emoji_df = pd.DataFrame(Counter(emojis).most_common(), columns=["Emoji", "Count"])
    
    return emoji_df
