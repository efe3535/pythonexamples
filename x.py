token = 'VdINGcwGZsIvUTbuZl3PRTvX2MhkdieXFk9cnNRA4J8hP-jw1obnY6KCfXpRJFTA'
import lyricsgenius

genius = lyricsgenius.Genius(token)
muzik = input("Şarkı sözü ara:")

song = genius.search_song(muzik)
print(song.lyrics)