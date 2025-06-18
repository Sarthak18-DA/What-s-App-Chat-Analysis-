import streamlit as st
import Preprocessor,helper
import matplotlib.pyplot as plt
import emoji 

st.sidebar.title("WhatsApp Chat Analysis")

uploaded_file = st.sidebar.file_uploader("Choose a File")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = Preprocessor.preprocess(data)
    
    
    st.dataframe(df)
    
    # Fetch Unique Users
    user_list = df["Users"].unique().tolist()
    user_list.remove("Group Notification")
    user_list.sort()
    user_list.insert(0,"OverAll")
    
    selected_user = st.sidebar.selectbox("Show Analysis Result",user_list)
    
    if st.sidebar.button("Show Analysis"):
    
        num_messages,words,num_media_messages,links = helper.fetch_stats(selected_user,df)
        
        st.title("Top Statistics of WhatsApp Chat")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
            
            
        with col2:
            st.header("Total Words")
            st.title(words)
            
            
        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)  
              
            
        with col4:
            st.header("Link Shared")
            st.title(links)
        
    if selected_user == "OverAll":
        st.title("Most Busy Users")
        x,new_df = helper.most_busy_users(df)
        
        fig, ax = plt.subplots()
        modified_names = [" ".join(name.split()[:1]) for name in x.index]
        
        
        col1, col2 = st.columns(2)
        
        with col1:
            ax.bar(modified_names, x.values, color = "red")
            st.pyplot(fig)
        
        
        with col2:
            st.dataframe(new_df)
            
    st.pyplot(fig)
    
    emoji_df = helper.emoji_helper(selected_user,df)
    st.title("Emoji Analysis")
    
    
    col1,col2 = st.columns(2)
    
    with col1:
        st.dataframe(emoji_df)
        print(emoji_df)
                
        