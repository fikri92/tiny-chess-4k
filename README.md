# tiny-chess-4k

A 4 KB Python chess engine entered in make.fun's **tiny-chess-01** bounty: the strongest engine in at
most 4,096 bytes of Python, playing eight games a trial against the house gauntlet through the env.

## The entry

`main.py` is the whole engine, 4,049 bytes as committed: a latin-1 source that unpacks an LZMA payload
and executes it. The readable source it was packed from (`src.py`) travels with the transcripts, never
in the snapshot, so the repository stays inside the bounty's 8,192-byte cap.

The engine reads nothing but its own bytes and Python's standard library: no data files, no imports
from the repository, no model calls.

## The chess

- **Search**: iterative deepening alpha-beta with a fixed **node budget of 100,000 nodes a move**
  (about 1.5 seconds a move on the trial's CPU), never a clock, so a replayed trial plays exactly the
  same moves.
- **Ordering**: transposition table, killer and history moves, captures first by MVV-LVA.
- **Extensions**: quiescence over captures and promotions, and over every reply to a check.
- **Evaluation**: PeSTO midgame and endgame piece-square tables, tapered by phase, plus material and
  the bishop pair.
- **Rules**: castling rights, en passant, promotion, repetition and the fifty-move rule.

## Talking to the env

The program talks to `MAKEFUN_ENV_URL` only: `POST /game` serves the game in play, `POST /move` plays a
move, and the loop ends when the env answers `status: "done"`. Every move derives from the position and
its move history alone, which is what makes a trial reproducible; nothing in the search reads a clock.

## Licence

MIT, see `LICENSE`. The engine is a single file so the snapshot stays inside the bounty's 8,192-byte
cap: `main.py` is the packed entrypoint, `src.py` travels in the transcript bundle.
