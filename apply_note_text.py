"""
Applies text to clips.
- Clips must be in a "raw" directory within the parent directory.
- Text clips will be put into a "text" directory.
- Specified position is of the form <x>,<y> (comma-separated pair)

Examples:
python apply_note_text.py -d ./data/recordings/violin_1 -p 1260,70
python apply_note_text.py -d ./data/recordings/violin_2 -p 380,70
"""

import argparse
import os
import moviepy.editor as mpe
import moviepy as mp
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir")
parser.add_argument("-p", "--position")
args = parser.parse_args()

recording_dir = args.dir
text_pos = tuple(map(int, args.position.split(",")))

files = os.listdir(os.path.join(recording_dir, "raw"))


def create_text_clip(file, position):
    clip = mpe.VideoFileClip(os.path.join(recording_dir, "raw", file))
    text = os.path.splitext(file)[0]

    if text == "rest":
        return clip

    text = text[:-1]
    text_clip = mp.video.VideoClip.TextClip(
        text,
        fontsize=144,
        font="Arial-bold",
        color="black"
    ).set_position(position).set_duration(clip.duration)

    return mpe.CompositeVideoClip([clip, text_clip])


print("Creating text-overlay clips...")
os.makedirs(os.path.join(recording_dir, "text"), exist_ok=True)
for file in tqdm(files):
    create_text_clip(file, text_pos).write_videofile(
        os.path.join(recording_dir, "text", file), logger=None)
