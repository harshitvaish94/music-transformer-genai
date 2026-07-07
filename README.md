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

## 📊 Dataset & Training Empirical Results

The model was trained on a massive, serialized dataset using a custom, memory-safe sliding-window generator to handle long-term musical dependencies without RAM bottlenecks.

### 📁 Dataset Profile
* **Source Dataset:** Lakh MIDI Clean Dataset
* **Total Audio Files Tracked:** 17,219 cleaned MIDI files
* **Total Tokenized Musical Events:** 399,137,225 tokens
* **Vocabulary Vocabulary Dimensions:** 2,753 unique tokens (Encoding: `PROGRAM_X`, `TIME_SHIFT_X`, `VELOCITY_X`, `NOTE_ON_X`, `DURATION_X`)

### 🧠 Model Scale & Architectural Hyperparameters
* **Framework:** Keras Functional API / TensorFlow
* **Total Trainable Parameters:** 972,481 (~3.71 MB)
* **Context / Sequence Window Size:** 256 tokens
* **Internal Layers:** 2x Transformer Blocks
* **Attention Mechanism:** Multi-Head Self-Attention (4 Heads, Key Dimension = 32)
* **Hidden Dimension ($d_{model}$):** 128

### 📈 Training Performance & Optimization Track
The final "deep training" optimization pass scaled the iterations across large token chunks with a batch size of 32:

| Metric | Baseline (Epoch 1, 100 steps) | Final Deep Run (Epoch 5, 750 steps) |
| :--- | :--- | :--- |
| **Training Cross-Entropy Loss** | 6.5664 | **3.6503** |
| **Next-Token Prediction Accuracy** | 8.58% | **18.55%** |
| **Average Hardware Step Latency** | ~2.00 seconds / step | ~1.93 seconds / step |
| **Total Computation Time** | ~3.3 minutes | **~2.0 Hours Total** (~24 mins / epoch) |

*Note on Evaluation: In generative music modeling with a vocabulary of 2,753 discrete tokens, a next-token prediction accuracy of 18.55% represents performance >500x better than a uniform random baseline selection (0.036%), capturing strong structural, harmonic, and rhythmic token-to-token dependencies.*
---

## Author
**Harshit Vaish**
