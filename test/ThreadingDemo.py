from threading import Thread
import time

class GenerationClass(Thread):

    def __init__(self, i):
        Thread.__init__(self)
        self.song = 0
        self.i = i
        self.daemon=True

    def run(self):
        time.sleep(5)
        self.song = self.i
        print("song generated")

    def get_generated_song(self):
        return self.song


# generate starting song and wait
starting_song_thread = GenerationClass(3)
starting_song_thread.start()
print("starting song generation")
starting_song_thread.join()
print("starting song generated: ", starting_song_thread.get_generated_song())

current_song = starting_song_thread.get_generated_song()
# current_song = starting_song_thread.get_generated_song()

while True:

    print("playing song, generating new one")

    new_song_thread = GenerationClass(5)
    new_song_thread.start()

    for i in range(3):
        time.sleep(1)
    print("song finished, waiting for new song to finish generating")
    new_song_thread.join()
    current_song = new_song_thread.get_generated_song()

    # play starting song ad at the same time, generate next song



