# Stitch a MIDI file together

import moviepy.editor as mpe
import moviepy as mp
from tqdm import tqdm
import os

# Arguments
note_clip_dir = f"./data/recordings/violin_1/text"
sequence_dir = f"./data/sequence/bach_double/violin_1.txt"
output_dir = f"./output"

os.makedirs(output_dir, exist_ok=True)

# Grab note names
with open("../data/note_names.txt") as fin:
    items = [line.split(",") for line in fin.read().strip().split("\n")]
    name2code = {name: int(code) for name, code in items}
    code2name = {int(code): name for name, code in items}

note_names = [name for name, _ in items]

# Load all clips
# Takes ~30 seconds
print(f"Loading all note clips...")
note2clip = {}
for note in tqdm(note_names, ncols=100):
    note2clip[note] = mpe.VideoFileClip(
        os.path.join(note_clip_dir, f"{note}.mp4"))
print()


# Grab piece data
notes = []
with open(sequence_dir) as fin:
    notes = [tuple(map(int, line.split(",")))
             for line in fin.read().strip().split("\n")]


# Render the video
# https://stackoverflow.com/questions/28758474/how-to-concatenate-videos-in-moviepy
all_clips = []
note_duration = 0.15
for timestamp, code, duration in notes:
    all_clips.append(
        note2clip[code2name[code]].subclip(0, duration * note_duration)
        # .fx(mp.audio.fx.all.audio_fadeout, note_duration * 0.5)
        # .fx(mp.audio.fx.all.audio_fadein, note_duration * 0.5)
    )

# ~50 seconds
print(f"Concatenating clips...")
concat_clips = mp.editor.concatenate_videoclips(all_clips[1:10])
print()


# ~30 seconds for building
# ~5-6 minutes for writing
print(f"Building final video...")
concat_clips.write_videofile(os.path.join(output_dir, "output.mp4"))
