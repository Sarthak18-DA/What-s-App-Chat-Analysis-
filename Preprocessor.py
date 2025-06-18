import re
import pandas as pd

def preprocess(data):
    messages = []
    dates = []
    pattern = r'(\d{1,2}/\d{1,2}/\d{2}),\s(\d{1,2}:\d{2})\s?[-–]\s'
    split_data = re.split(pattern, data)[1:]

    for i in range(0, len(split_data)-2, 3):
        date = f"{split_data[i]} {split_data[i+1]}"
        message = split_data[i+2]
        dates.append(date)
        messages.append(message)

    df = pd.DataFrame({'Date': pd.to_datetime(dates, format='%d/%m/%y %H:%M', errors='coerce'),
                       'User Message': messages})

    users = []
    texts = []

    for msg in df['User Message']:
        parts = re.split(r'([\w\s]+?):\s', msg, maxsplit=1)
        if len(parts) > 2:
            users.append(parts[1])
            texts.append(parts[2])
        else:
            users.append("Group Notification")
            texts.append(parts[0])

    df["Users"] = users
    df["Message"] = texts
    df.drop(columns="User Message", inplace=True)

    df["only_date"] = df["Date"].dt.date
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month_name()
    df["Month_Num"] = df["Date"].dt.month
    df["Day_Name"] = df["Date"].dt.day_name()
    df["Hour"] = df["Date"].dt.hour

    return df


