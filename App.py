import streamlit as st
import Preprocessor
import helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("📊 WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a WhatsApp Chat File")
if uploaded_file is not None:
    data = uploaded_file.getvalue().decode("utf-8")
    df = Preprocessor.preprocess(data)
    
    st.dataframe(df)

    # Fetch unique users
    user_list = df["Users"].unique().tolist()
    if "Group Notification" in user_list:
        user_list.remove("Group Notification")
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show Analysis For", user_list)

    if st.sidebar.button("Show Analysis"):
        # Top Stats
        num_messages, words, media, links = helper.fetch_stats(selected_user, df)
        st.title("📌 Top Statistics")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Messages", num_messages)
        col2.metric("Words", words)
        col3.metric("Media Shared", media)
        col4.metric("Links Shared", links)

        # Monthly timeline
        st.title("🗓 Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message_count'], color='green')
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Daily timeline
        st.title("📆 Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message_count'], color='orange')
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Activity maps
        st.title("📅 Activity Map")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Most Busy Day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='purple')
            plt.xticks(rotation=45)
            st.pyplot(fig)

        with col2:
            st.subheader("Most Busy Month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='teal')
            plt.xticks(rotation=45)
            st.pyplot(fig)

        # Heatmap
        st.title("⏰ Weekly Activity Heatmap")
        heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        sns.heatmap(heatmap, ax=ax)
        st.pyplot(fig)

        # Most busy users (group only)
        if selected_user == "Overall":
            st.title("💬 Most Active Users")
            x, new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()
            ax.bar(x.index, x.values, color='red')
            st.pyplot(fig)
            st.dataframe(new_df)

        # Wordcloud
        st.title("☁️ WordCloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # Most common words
        st.title("🔠 Most Common Words")
        most_common_df = helper.most_common_words(selected_user, df)
        st.dataframe(most_common_df)

        # Emoji analysis
        st.title("😊 Emoji Analysis")
        emoji_df = helper.emoji_helper(selected_user, df)
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df["Count"].head(), labels=emoji_df["Emoji"].head(), autopct="%0.2f")
            st.pyplot(fig)
