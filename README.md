# tiny-chess-01 entry: a 4 KB Python chess engine

`main.py` (4,066 B) is the whole engine: a latin-1 source that unpacks an lzma payload and execs it.
It plays every game through the env at `MAKEFUN_ENV_URL` (POST /game, POST /move) and stops when the
env answers status "done". The search is a fixed node budget (100,000 nodes a move), never a clock, so
a replayed trial plays the same moves: alpha-beta with a transposition table, killer history, capture
and check extensions, quiescence, PeSTO piece-square tables tapered by phase, and iterative deepening.
