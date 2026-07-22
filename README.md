# TuneWithin - Emotion-Aware Music Companion

TuneWithin is a web application that analyzes your emotions from diary entries and recommends personalized music to match or transform your mood.

## Playlist Information

TuneWithin uses curated Hindi-English mixed playlists from Spotify. These playlists have been verified to work correctly and provide a rich cultural music experience:

### Curated Spotify Playlists

1. **English x Hindi Remix/Mashups**
   - Spotify ID: `6ssT4PODIHKkfLjnNjTA0G`
   - Features a blend of English and Hindi mashups, including Lofi remixes and slowed + reverbed tracks.

2. **Hindi and English Mixed Playlist (Mashup Travel Songs)**
   - Spotify ID: `45ZExvV649m3IUwEu5Ie3Y`
   - A mix of Hindi and English tracks perfect for road trips and travel.

3. **Mix Lofi Songs (Hindi/English)**
   - Spotify ID: `7ykQM9HrZHvKRBvTL8Ebbc`
   - Lofi songs combining Hindi and English tracks, ideal for relaxation.

4. **Heartbroken/Romantic Hindi Playlist**
   - Spotify ID: `4C34CZdaGedDSVEJ4fyqmd`
   - A collection of romantic and heartbroken Hindi songs.

5. **Uplifting - English, Hindi, Tamil Mix**
   - Spotify ID: `31kiAehGU5xxZWuqehiUZP`
   - An energetic mix of English, Hindi, and Tamil songs to boost motivation.

## Features

- **Emotion Analysis**: Analyzes your diary entries to determine your mood
- **Personalized Recommendations**: Suggests playlists that match your current emotional state
- **Mood Transition**: Helps shift your mood in a positive direction
- **Voice Diary**: Record your thoughts through voice that gets transcribed
- **Sentiment Visualization**: Track your mood over time with interactive charts
- **Disorder Prediction** : Predicts if the user has GAD/Depression/Biplor disorder

## Technology Stack

- Flask (Python web framework)
- SQLite database
- TextBlob for sentiment analysis
- Chart.js for data visualization
- Spotify Web API for music integration
- Bootstrap for responsive design
- GRU for disorder prediction

TuneWithin — Emotion-Aware Music Companion
TuneWithin is an emotion-aware web application that analyzes your diary entries and recommends personalized music to match or transform your mood. Whether you're feeling joyful, heartbroken, or introspective, TuneWithin curates the perfect playlist experience tailored just for you.

Features
Emotion Analysis
Understand your emotions through intelligent sentiment analysis of diary entries.

Personalized Music Recommendations
Suggests curated playlists that resonate with your current mood.

Mood Transition Engine
Guides you through a gentle emotional shift using music-based therapy.

Voice Diary Support
Record your thoughts via voice — automatically transcribed and analyzed.

Sentiment Visualization
Track your emotional journey with dynamic, interactive mood charts.

Mental Health Disorder Prediction
Uses a GRU-based model to predict possibilities of:

Generalized Anxiety Disorder (GAD)
Depression
Bipolar Disorder
Curated Spotify Playlists
TuneWithin integrates hand-picked Spotify playlists for a rich and culturally resonant music experience:

Playlist Name	Description	Spotify ID
English x Hindi Remix/Mashups	A blend of Hindi and English mashups including Lofi, slowed + reverbed edits.	6ssT4PODIHKkfLjnNjTA0G
Mashup Travel Songs (Hindi-English)	Perfect road trip blend of Hindi and English tracks.	45ZExvV649m3IUwEu5Ie3Y
Mix Lofi Songs (Hindi/English)	Chill and relax with Lofi vibes across languages.	7ykQM9HrZHvKRBvTL8Ebbc
Heartbroken/Romantic Hindi Playlist	Emotional and romantic Hindi melodies.	4C34CZdaGedDSVEJ4fyqmd
Uplifting - English, Hindi, Tamil Mix	Energetic, multi-language tracks for motivation and positivity.	31kiAehGU5xxZWuqehiUZP
Technology Stack
Backend: Flask (Python)
Database: SQLite
Emotion Analysis: TextBlob
Data Visualization: Chart.js
Music Integration: Spotify Web API
Frontend: Bootstrap
ML Model: GRU (for mental health disorder prediction)
Setup & Installation
git clone https://github.com/your-username/TuneWithin.git
cd TuneWithin
pip install -r requirements.txt
python app.py
