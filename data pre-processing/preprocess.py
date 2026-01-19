from music21 import environment

us = environment.UserSettings()
us['musescoreDirectPNGPath'] = '/Applications/MuseScore 4.app/Contents/MacOS/mscore'
us['musicxmlPath'] = '/Applications/MuseScore 4.app/Contents/MacOS/mscore'

import os
import music21 as m21


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KERN_DATASET_PATH = os.path.join(BASE_DIR, "deutschl", "test")
dataset_path = KERN_DATASET_PATH
SAVE_DIR = "dataset"
os.makedirs(SAVE_DIR, exist_ok=True)

ACCEPTABLE_DURATIONS = [
    0.25,
    0.5,
    0.75,
    1.0,
    1.5,
    2,
    3,
    4
]



# kern, MIDI, MusicXML -> m21 -> kern, MIDI,...
def load_songs_in_kern(dataset_path):

    songs = []
    # go through all the files in dataset and load them with music21
    for path, subdirs, files in os.walk(dataset_path):
        for file in files:
            if file[-3:] == "krn":
                song = m21.converter.parse(os.path.join(path, file))
                songs.append(song)
    return songs

def has_acceptable_duration(song, acceptable_duration):
    for note in song.flat.notesAndRests:
        if note.duration.quarterLength not in acceptable_duration:
            return False
    return True

def transpose(song):
    
    # get key from the song
    parts = song.getElementsByClass(m21.stream.Part)
    measures_part0 = parts[0].getElementsByClass(m21.stream.Measure)
    key = measures_part0[0][4]

    # estimate key using music21

    if not isinstance(key, m21.key.Key):
        key = song.analyze("key")
    
    print(key)

    # get interval for transposition (Bmaj -> Cmaj)
    if key.mode == "major":
        interval = m21.interval.Interval(key.tonic, m21.pitch.Pitch("C"))
    elif key.mode == "minor":
        interval = m21.interval.Interval(key.tonic, m21.pitch.Pitch("A"))

    # transpose song by calculated interval
    transposed_song = song.transpose(interval)

    return transposed_song

def encode_song(song, time_step=0.25):
    # p = 60, d = 1.0 -> [60, "_", "_", "_"]

    encoded_song = []

    for event in song.flat.notesAndRests:

        # handle notes
        if isinstance(event, m21.note.Note):
            symbol = event.pitch.midi # 60
        #handle rests
        elif isinstance(event, m21.note.Rest):
            symbol = "r"

        # convert the note/rest into time series notation
        steps = int(event.duration.quarterLength / time_step)
        for step in range(steps):
            if step == 0:
                encoded_song.append(symbol)
            else:
                encoded_song.append("_")

    # cast encoded song to a str

    encoded_song = " ".join(map(str, encoded_song))

    return encoded_song

def preprocess(dataset_path):
    pass

    # load folk songs
    print("Loading songs...")
    songs = load_songs_in_kern(dataset_path)
    print(f"Loaded {len(songs)} songs.")

    for i, song in enumerate(songs):

        # filter out songs that have non-acceptable durations
        if not has_acceptable_duration(song, ACCEPTABLE_DURATIONS):
            continue

        # transpose songs into Cmaj/Amin
        song = transpose(song)

        # encode songs with music time series representations
        encoded_song = encode_song(song)

        # save songs to text file
        save_path = os.path.join(SAVE_DIR, str(i))
        with open(save_path, "w") as fp:
            fp.write(encoded_song)


if __name__ == "__main__":
    songs = load_songs_in_kern(KERN_DATASET_PATH)
    print(f"Loaded {len(songs)} songs.")
    song = songs[0]

    preprocess(KERN_DATASET_PATH)
    
    transposed_song = transpose(song)
    transposed_song.show()