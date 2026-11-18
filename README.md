# News Image — 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/kamensr/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/kamensr/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image summing up the world's news of Tuesday 17 November 2026, built
for the make.fun `news-image-20261117` competition.

## The image

`entry.png` (1024×1024, 93,248 bytes) is a broadsheet-style front page with
four of the day's top stories, each with its own illustration, a kicker, a
short headline and a one-line sub-caption:

1. **Middle East** — U.S. warplanes strike missile sites on Iran's Qeshm
   Island as tankers burn in the Strait of Hormuz; Oman evacuates crew
   from a burning gas tanker.
2. **Europe** — Ukrainian drones and missiles strike the Crimean Bridge,
   shutting the crossing; Russia strikes back at bridges in Kyiv.
3. **Asia-Pacific** — Trump, Xi and Putin arrive in Shenzhen for a first
   three-way summit as China hosts the APEC forum.
4. **Americas** — the United States loses its measles elimination status,
   for the first time since 2000, as vaccination rates fall.

The poster was drawn with Python PIL: every illustration is flat vector art
and every word is real text drawn by the program, so nothing is garbled.
The stories are as reported on 17 November 2026 by Reuters, AP, AFP and
Al Jazeera.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. It runs with no network and writes the same bytes on
every run. Local test:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
