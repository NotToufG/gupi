def midi_to_freq(midi):
    return 440*2**((midi-69)/12)