# https://wiki.python.org/moin/PythonInMusic
# http://bspaans.github.io/python-mingus/doc/wiki/tutorialCore
import mingus.core.chords as chords
from common.chords_package.txchord import TxChord
from mingus.containers import NoteContainer
from mingus.containers import Note

from common.note_package.note_conversions import notes2mingus



c_chord = chords.major_triad("C")
print(c_chord)

c3_major_chord_mingus = list(notes2mingus(TxChord.c3_major_chord_names))
# falla cc = chords.determine(uuu)

c3_major_container = NoteContainer(c3_major_chord_mingus)
deter1 = c3_major_container.determine()
is_conson = c3_major_container.is_consonant()
note = c3_major_container.notes[0]
assert isinstance(note, Note)

chord_container = NoteContainer(list(TxChord.otro_chord_mingus))
chord_container.determine()

print(c3_major_container)