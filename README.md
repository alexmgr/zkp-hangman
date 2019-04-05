A hangman-like using crypto accumulators. Allows to build an interactive
 zero knowledge proof to validate that the initial word to guess does
 not change from underneath the guessing player during the game.
The aim is to prevent one player from changing the input word during the
game. E.g: you initially select "ripe". On a successful guess of the
letter "r" from the guessing player, switch your word to "pipe".

This is obviously a test implementation, a lot of things are incorrect
(accumulator parameters, prime mappings, input validation, ...)

This could be used in more interesting settings where an initial item
must be partially disclosed, but with guarantees as to it's future content.
E.g: guaranteeing the integrity of redacted documents. At the time of
redaction, publish the proof. At the time of (partial) disclosure,
publish the proof of what is not in the document. That would allow to
guarantee that the released portions are the ones redacted in the
initial document.
