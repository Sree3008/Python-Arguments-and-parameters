from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re
import mysql.connector

# Spotify API setup
sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id='2f442a5864084e01872ec29890466d2e',
        client_secret='02230fd6498a4cc480c078c61e3d99f7'
    )
)

# Spotify track URL
track_url = "https://open.spotify.com/track/003vvx7Niy0yvhvHt4a68B"

# Extract track ID
track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

# Fetch track details
track = sp.track(track_id)

# Database configuration (spotify_db)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'sree@3008',
    'database': 'spotify_db'
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    popularity INT,
    duration_minutes FLOAT
)
""")

# Extract metadata
track_data = (
    track['name'],
    track['artists'][0]['name'],
    track['album']['name'],
    track['popularity'],
    track['duration_ms'] / 60000
)

# Insert data into spotify_db
cursor.execute("""
INSERT INTO tracks (track_name, artist, album, popularity, duration_minutes)
VALUES (%s, %s, %s, %s, %s)
""", track_data)

connection.commit()
print("✅ Track data inserted into spotify_db")

# Convert to DataFrame
df = pd.DataFrame([{
    'Track Name': track_data[0],
    'Artist': track_data[1],
    'Album': track_data[2],
    'Popularity': track_data[3],
    'Duration (minutes)': track_data[4]
}])

print(df)

# Save to CSV
df.to_csv('spotify_track_data.csv', index=False)

# Visualization
plt.figure(figsize=(8, 5))
plt.bar(['Popularity', 'Duration'], [track_data[3], track_data[4]])
plt.title(f"Track Metadata for '{track_data[0]}'")
plt.ylabel("Value")
plt.show()

cursor.close()
connection.close()

