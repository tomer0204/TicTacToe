import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tedy237878!",
    database="users"
)

query = "SELECT first_name, last_name, score, game_date, game_time FROM players"
df = pd.read_sql(query, mydb)

df['player_name'] = df['first_name'] + " " + df['last_name']

df_sorted = df.sort_values(by='score', ascending=False)

plt.figure(figsize=(12, 8))
plt.bar(df_sorted['player_name'], df_sorted['score'], color="skyblue", edgecolor="black")
plt.xlabel("playerName", fontsize=14)
plt.ylabel("score", fontsize=14)
plt.title("check players scores", fontsize=16)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# הצגת הגרף
plt.show()
