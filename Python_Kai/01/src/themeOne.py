from music import *

pitches1   = [F4, REST, AF4, REST, F4, F4, BF4, F4, EF4, F4, REST, C5, REST]
durations1 = [QN, QN, QN, EN, QN, EN, QN, QN, QN, QN, QN, QN, EN]
pitches2   = [F4, F4, DF5, C5, AF4, F4, C5, F5, F4, EF4, EF4, C4, G4, F4]
durations2 = [QN, EN, QN, QN, QN, QN, QN, QN, EN, QN, QN, DQN]

#create an empty phrase, and construct theme using the pitch and duration(s) data
theme = Phrase()
theme.addNoteList(pitches1, durations1)
theme.addNoteList(pitches2, durations2)
#now set the instrument and temp for the theme
theme.setInstrument(SYNTH_BASS_2)
theme.setTempo(220)

#play the theme
Play.midi(theme)
