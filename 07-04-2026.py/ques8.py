#music player with composition
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.duration}s)"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def get_total_duration(self):
        return sum(song.duration for song in self.songs)

    def show_playlist(self):
        print("Playlist:", self.name)

        for i, song in enumerate(self.songs, 1):
            print(f"{i}. {song}")

        print("Total Duration:", self.get_total_duration(), "seconds")


# Test
playlist = Playlist("My Favorites")

song1 = Song("Bohemian Rhapsody", "Queen", 355)
song2 = Song("Imagine", "John Lennon", 183)

playlist.add_song(song1)
playlist.add_song(song2)

playlist.show_playlist()