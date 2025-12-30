#  Music Generation using Transformer (GenAI)

A Transformer-based generative AI project that learns musical patterns from MIDI files and generates new music sequences. The system tokenizes musical elements and produces playable MIDI outputs using temperature-based sampling.

---

## Problem Statement
Generating coherent and creative music requires understanding long-range patterns such as rhythm, melody, and timing. Traditional rule-based systems struggle with this, motivating a data-driven generative approach.

---

## Approach
- MIDI files are converted into discrete tokens (pitch, duration, velocity, time-shift)
- A Transformer model is trained to predict the next musical token
- New music is generated from a short seed sequence
- Generated tokens are converted back into MIDI format for listening

---

## Tech Stack
- Python  
- TensorFlow / Keras  
- PrettyMIDI  
- NumPy  

---

## Project Structure

project/

├── MusicGen.ipynb # Data preprocessing, training, and experiments

├── inference.py # Music generation logic

├── notes.py # Helper / experimentation code

├── .gitignore

└── README.md

---

## Results
The model generates MIDI files that can be played and evaluated by listening. Outputs show learned musical structure such as note continuity and rhythmic consistency.

---

## Author
**Harshit Vaish**
