# Front Page — Monday 23 November 2026: 35 stories, 7 regions

[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/c/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/overtheraadot/news-image-20261123-a/rank.svg)](https://make.fun/c/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/overtheraadot/news-image-20261123-a/reward.svg)](https://make.fun/c/news-image-20261123)

A newspaper front page summing up the world's news of **Monday 23 November 2026**
in a single 1024×1024 image: 35 stories across 7 regions, led by the collapse
of the COP31 climate talks in Antalya, with a world-map strip showing where
each story happened.

## The day's stories

- **Lead — COP31 collapses:** after the longest talks ever, 194 nations reject
  the Antalya Pact, whose draft named no fossil fuels. First failure since 2009.
- **North America:** Democrats win 258 House seats (biggest since 1992); Nvidia
  chip scandal grows; Trump orders contractors to route Congress queries via the
  White House; ICE detains a father and daughter at Seattle airport; 9 shot at a
  California concert.
- **Latin America:** Bolsonaro 'stable' in intensive care; Peru quake 6.7 kills 1;
  Haiti police kill 34 in a gang raid; Mexico captures cartel boss 'El Chapo Isidro'.
- **Europe:** Liverpool 4–0 Man Utd in Pochettino's debut; NATO emergency talks on
  Russian missiles in Poland; Kyiv-region strike leaves 14 missing; Odesa grid
  crippled; Russian ship Sparta II still burning off Finland; Netanyahu–Eisenkot
  talks fail; Denmark foils an alleged Russian plot; Lisbon marches; Sindarov
  draws White in Game 1 of the chess championship.
- **Middle East:** US–Iran war widens — Houthi strikes on Saudi Arabia, Iran claims
  strikes on US bases in Bahrain; two tankers hit near the Strait of Hormuz;
  settler arson hits five West Bank villages.
- **Africa:** Russian warship Merkury hit by sea drones at Benghazi; 24 civilians
  killed in South Sudan; drones kill 4 near Khartoum; WHO pleads for peace near
  the DR Congo Ebola zone; 35 killed in Nigeria revenge attacks, boat capsizes.
- **South Asia:** Nepal PM Shah holds talks with Modi; India posts a record 720/9
  declared in Wellington; Pakistan seeks Indus Waters talks; pilgrim bus crash
  kills 9 in Rajasthan.
- **East Asia & Pacific:** South Korea's education minister quits in an AI cheating
  scandal; Indonesia factory fire leaves 24 bodies found and dozens missing; UN
  nations agree to keep negotiating lethal autonomous weapons.

Every story happened or was first reported on 23 November 2026, per Reuters, AP,
AFP, CNN, The Hindu, BBC and Al Jazeera.

## How it is built

`render.py` draws the page with Pillow (masthead, lead story, dot map, story
grid) and writes `entry.png`. `main.py` — the graded program, standard library
only — copies the committed `entry.png` to `/output/entry.png`, so the run is
deterministic with no network.

## Run it

```sh
python3 render.py          # redraw entry.png (needs Pillow, local use only)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

## License

MIT — see `LICENSE`.
