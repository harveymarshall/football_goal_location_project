# streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import VerticalPitch

# Background color
bg_color = "#0c0d0e"

# Load your full DataFrame here
df_all = pd.read_csv("../data/players_shots_data_EPL_2024_updated.csv")
# It should contain: Player, Shot X, Shot Y, xG_Per_Shot, goals

# Streamlit UI
st.set_page_config(layout="wide", page_title="Premier League Shot Map")
st.title("Premier League Shot Map 24/25")
player_name = st.selectbox("Select a player", df_all["Player Name"].unique())

# Filter data for selected player
df = df_all[df_all["Player Name"] == player_name]


actual_avg_dist = 120 - (df['Shot X'] * 1.2).mean()
points_avg_dist = df["Shot X"].mean()  # or set as constant if preferred

# Create figure
fig = plt.figure(figsize=(8, 12))
fig.patch.set_facecolor(bg_color)

# Top panel
ax1 = fig.add_axes([0, .7, 1, .2])
ax1.set_facecolor(bg_color)
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)

ax1.text(x=.5, y=.85, s=player_name, fontsize=20, fontweight='bold', color='white', ha='center')
ax1.text(x=.5, y=.75, s='Goals Premier League 24/25', fontsize=14, fontweight='bold', color='white', ha='center')
ax1.text(x=.22, y=.5, s='Low Quality Chance', fontsize=12, fontweight='bold', color='white', ha='center')
ax1.text(x=.78, y=.5, s='High Quality Chance', fontsize=12, fontweight='bold', color='white', ha='center')

# xG dot sizes
for i, size in enumerate(range(100, 600, 100)):
    ax1.scatter(x=.38 + i * .06, y=.53, s=size, color=bg_color, edgecolor='white', linewidth=.8)

# Goal and No Goal indicators
ax1.text(x=.45, y=.27, s='Goal', fontsize=10, fontweight='bold', color='white', ha='right')
ax1.scatter(x=.47, y=.3, s=100, color='red', edgecolor='white', linewidth=.8, alpha=.7)

ax1.scatter(x=.53, y=.3, s=100, color=bg_color, edgecolor='white', linewidth=.8)
ax1.text(x=.55, y=.27, s='No Goal', fontsize=10, fontweight='bold', color='white', ha='left')

# Pitch panel
ax2 = fig.add_axes([.05, .25, .9, .5])
ax2.set_facecolor(bg_color)

pitch = VerticalPitch(pitch_type='opta', half=True, pitch_color=bg_color,
                      pad_bottom=.5, line_color='white', linewidth=.75, axis=True, label=True)
pitch.draw(ax=ax2)

# Avg distance
ax2.scatter(x=90, y=points_avg_dist, s=100, color='white', linewidth=.8)
ax2.plot([90, 90], [100, points_avg_dist], color='white', linewidth=2)
ax2.text(x=90, y=points_avg_dist - 4, s=f'Avg Shot Distance \n {actual_avg_dist:.1f} yards',
         fontsize=8, fontweight='bold', color='white', ha='center')

# Plot shots
for x in df.to_dict(orient='records'):
    pitch.scatter(x['Shot X'], x['Shot Y'], s=x['xG_Per_Shot'] * 300, color='red' if x['Is Goal'] == True else bg_color, ax=ax2, edgecolor='white', linewidth=.8, alpha=.7)

# Show in Streamlit
st.pyplot(fig)
