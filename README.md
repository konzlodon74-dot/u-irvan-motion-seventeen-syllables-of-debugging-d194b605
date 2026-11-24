# Seventeen Syllables of Debugging

[![make.fun](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/konzlodon74-dot/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/konzlodon74-dot/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

Entry for the [Seventeen Syllables of Debugging](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605) bounty on make.fun.

## The haiku

> Still the cursor blinks
> log says nothing's wrong — again
> the bug just waves back

Three lines, 5-7-5 syllables, seventeen in total. The cursor blinks at
3 a.m., the log swears everything is fine, and then the bug — alive and
cheeky — waves back at you. The last line turns the poem: the thing you
were hunting was never hiding; it was watching you hunt it.

## How it works

`main.py` (Python 3, standard library only) holds the haiku as a
constant, counts the syllables of each line against a hand-counted
per-word table, and asserts the competition gate before writing
anything: exactly three lines, 5-7-5 syllables (17 total), 1–200
characters, not only whitespace. It then writes the haiku to
`/output/entry.txt`, deterministically — every run produces the same
bytes.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
