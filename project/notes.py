import pretty_midi

def print_midi_notes(midi_file):
    pm = pretty_midi.PrettyMIDI(midi_file)
    for i, instr in enumerate(pm.instruments):
        print(f"Instrument {i} (Program {instr.program}):")
        for note in instr.notes:
            print(f"  Pitch: {note.pitch}, Start: {note.start:.2f}, End: {note.end:.2f}, Velocity: {note.velocity}")

print("Input MIDI Notes:")
print_midi_notes("Fantasy Girl.mid")  # or your input file name

print("\nOutput MIDI Notes:")
print_midi_notes("fantasy_output.mid")  # or your output file name
