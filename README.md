#  Music Generation using Transformer (GenAI)
A Transformer-based generative AI project that learns musical patterns from MIDI files and generates new music sequences. 
The system tokenizes musical elements and produces playable MIDI outputs using temperature-based sampling.
# problem statement 
Generating coherent and creative music requires understanding long-range patterns such as rhythm, melody, and timing. 
Traditional rule-based systems struggle with this, motivating a data-driven generative approach.
# Approach 
- MIDI files are converted into discrete tokens (pitch, duration, velocity, time-shift)
- A Transformer model is trained to predict the next musical token
- New music is generated from a short seed sequence
- Generated tokens are converted back into MIDI format
#tech stack
- Python
- TensorFlow / Keras
- PrettyMIDI
- NumPy
#project structure
├── inference.py        # Music generation logic
├── train.py            # Model training pipeline
├── docs/               # Project explanation
├── examples/           # Sample generated outputs
├── requirements.txt
└── README.md
#result
The model generates MIDI files that can be played and evaluated by listening. Outputs show learned musical structure such as note continuity and rhythmic patterns.
**Author:** Harshit Vaish


