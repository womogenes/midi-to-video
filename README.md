# Automatic MIDI to video creator

This was quick project that I more or less threw together over a weekend. As such, it's not quite ready for public use yet. I've tried to be as comprehensive as I can with this documentation, but it's possible that there are details missing on how to use this. I'll try to make it more complete over time.

## What does this do?

Inspired by TwoSet Violin's ["1% Violin Skills 99% Editing Skills"](https://youtu.be/_r6j9rD_j5I) video, in which a piece of music is recorded as a sequence of chromatic notes stitched together as opposed to one continuous take.

See the video that I generated with this project here: [insert link]

## How can I make my own video?

This project is meant to recreate the Bach double violin concerto, so I'll be detailing the process of how I made that. Code can be tweaked to play arbitrary pieces, but =====

, and I hope to create a generalized

### Environment setup

Requires Python (I used Python 3.10.5, will probably work with older versions).

Requires the Python [moviepy](https://github.com/Zulko/moviepy) library, which you can install via

```
pip install moviepy
```

[ImageMagick](https://imagemagick.org/index.php) is required to put text labels onto the videos. Follow [these instructions](https://zulko.github.io/moviepy/install.html#other-optional-but-useful-dependencies) from the moviepy docs.

Also requires [numpy](https://numpy.org/) for generating the accelerando when creating the jumpcutted chromatic scale in `stitcher.ipynb`.

Requires [Jupyter notebook](https://docs.jupyter.org/en/latest/) to execute `stitcher.ipynb` and `merger.ipynb`. If you're not familiar with it, either 1. read up on Jupyter notebooks (link includes some helpful guides) or 2. wait for me to create a plain Python version :)

### Concrete steps

These might be incomplete or incorrect. Please submit an issue if there's anything missing.

These are the steps I did:

1. Record yourself playing a chromatic scale
2. Using external editing software, cut out the `33` notes from `G3` to `D6` and save them to `data/recordings/violin_1/raw`. Each recording should have the note, then some additional silence.
   1. **Naming convention:** name a note file `<note_name>.mp4`, e.g. `data/recordings/violin_1/raw/A4.mp4` should contain a 2-3 second clip of A4 being played.
3. Record ~30s of rest (e.g. standing still) and put that in `data/recordings/violin_1/raw/rest.mp4`
4. Execute `apply_note_text.py` to get note name labels onto the clips you recorded. Details about this script's arguments are in the source for the script. This will generate new clips in `data/recordings/violin_1/text` that are named identically to `data/recordings/violin_1/raw`, but the clips themselves contain text now!
5. Repeat steps 2-4 for violin 2.
6. Run `stitcher.py`. Arguments aren't implemented yet, go tinker with the source code. This should put a final video for the first violin part in `output/output.mp4`. (`output/` doesn't exist yet.)
7. Run `stitcher.py` again, but change arguments to do the second violin part.
8. Run `merger.ipynb` to

This documentation is actually quite incomplete, so I'll be finishing it off later. Some notes:

1. Music source is in `data/sequence/bach_double/violin_X.txt`. Explain how to create this from MIDI
