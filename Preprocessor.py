import re
import pandas as pd



def preprocess(data):
    pattern = r"\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\s?(?:am|pm)\s-\s"
    messages = re.split(pattern,data)[1:]
    dates = re.findall(pattern,data)
    df = pd.DataFrame({"User Message":messages,"Dates": dates})
    df['Dates'] = df['Dates'].str.strip()
    df['Dates'] = pd.to_datetime(df['Dates'], format='%d/%m/%y, %I:%M %p -')
    df.rename(columns = {"Dates":"Date"},inplace = True)
    
    User = []
    Messages = []

    for message in df["User Message"]:
        
        entry = re.split(r'(.*?):\s', message, maxsplit=1)
        if len(entry) > 2:  
            User.append(entry[1])  
            Messages.append(entry[2])  
        else: 
            User.append("Group Notification")
            Messages.append(entry[0])  

    df["Users"] = User
    df["Message"] = Messages
    
    df.drop(columns='User Message', inplace=True)
    
    phone_pattern = r'\+91\s\d{5}\s\d{5}'

    df = df[~df['Users'].str.contains(phone_pattern, regex=True)]
    
    df.loc[:, "Year"] = df["Date"].dt.year
    df.loc[:, "Month"] = df["Date"].dt.month_name()
    df.loc[:, "Day"] = df["Date"].dt.day
    df.loc[:, "Hour"] = df["Date"].dt.hour
    df.loc[:, "Minute"] = df["Date"].dt.minute
    
    return df