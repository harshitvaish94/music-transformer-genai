
import numpy as np
import pickle
from tensorflow import keras
import pretty_midi

# Load model and mappings
model = keras.models.load_model('music_transformer_trained.keras')
with open('token_mappings.pkl', 'rb') as f:
    token_to_idx, idx_to_token = pickle.load(f)

def pad_sequence(seq, target_length=256, pad_value=0):
    if len(seq) >= target_length:
        return seq[-target_length:]
    else:
        return [pad_value] * (target_length - len(seq)) + seq

def sample_with_temperature(preds, temperature=1.2):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds + 1e-8) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    return np.random.choice(len(preds), p=preds)

def generate_music_sequence(model, seed_tokens, length=300, temperature=1.2):
    generated = list(seed_tokens)
    for _ in range(length):
        input_seq = np.array([pad_sequence(generated, 256)], dtype=np.int32)
        preds = model.predict(input_seq, verbose=0)[0, -1, :]
        next_token = int(sample_with_temperature(preds, temperature))
        generated.append(next_token)
    return generated

def event_list_to_midi(event_list, outfile='output.mid'):
    pm = pretty_midi.PrettyMIDI()
    inst = pretty_midi.Instrument(program=0)
    current_time = 0
    velocity = 64
    note_on = None

    for event in event_list:
        if event.startswith('PROGRAM_'):
            program_num = int(event[len('PROGRAM_'):])
            inst.program = program_num
        elif event.startswith('NOTE_ON_'):
            note_num = int(event[len('NOTE_ON_'):])
            note_on = note_num
        elif event.startswith('VELOCITY_'):
            velocity = int(event[len('VELOCITY_'):])
        elif event.startswith('DURATION_') and note_on is not None:
            duration = int(event[len('DURATION_'):]) / 1000
            note = pretty_midi.Note(velocity=velocity, pitch=note_on, start=current_time, end=current_time + duration)
            inst.notes.append(note)
            current_time += duration
            note_on = None
        elif event.startswith('TIME_SHIFT_'):
            shift = int(event[len('TIME_SHIFT_'):]) / 1000
            current_time += shift

    pm.instruments.append(inst)
    pm.write(outfile)
    print(f"MIDI saved as {outfile}")

# Main inference function
def ai_continue_midi(input_midi_path, output_midi_path, length=300, temperature=1.2):
    """Generate continuation of input MIDI using trained model"""
    pm = pretty_midi.PrettyMIDI(input_midi_path)
    
    # Convert MIDI to event list (adapt as per your tokenization)
    event_list = []
    for instrument in pm.instruments:
        event_list.append(f"PROGRAM_{instrument.program}")
        for note in instrument.notes:
            event_list.extend([
                f"NOTE_ON_{note.pitch}",
                f"VELOCITY_{note.velocity}",
                f"DURATION_{int((note.end - note.start) * 1000)}"
            ])
    
    # Use first 256 tokens as seed
    seed_tokens = [token_to_idx[e] for e in event_list[:256] if e in token_to_idx]
    
    # Generate continuation
    generated_tokens = generate_music_sequence(model, seed_tokens, length=length, temperature=temperature)
    generated_events = [idx_to_token[token] for token in generated_tokens]
    
    # Export output MIDI
    event_list_to_midi(generated_events, outfile=output_midi_path)
    return output_midi_path

if __name__ == "__main__":
    # Example usage
    ai_continue_midi("Blind_Man.mid", "blinddout.mid", length=300, temperature=1.2)
ai_continue_midi("Pacific_202.mid", "pacific_output.mid", length=300, temperature=1.2)

