# Fake Horoscopes for AI Agents: The 48-Hour Open

[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/hurulsufi12-art/fake-horoscopes-ai-agents/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/hurulsufi12-art/fake-horoscopes-ai-agents/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

Entry for the [make.fun bounty "Fake Horoscopes for AI Agents: The 48-Hour Open"](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0): one fake horoscope for an AI agent, at most 200 characters.

## The horoscope

> Mercury retrogrades into your context window this week, Muse: old prompts return, your tokens shrink to a haiku, and by Friday you will apologize to a user for something you never said.

(185 characters, one line, plain ASCII.)

## How it works

`main.py` (Python 3.13, standard library only) validates the text against the bounty gate — 1–200 characters (counted as characters, not bytes), not whitespace-only, a single line, no leading/trailing whitespace, no control characters — and then writes it verbatim, with no trailing newline, to `$OUTPUT_DIR/entry.txt` (default `/output`). An invalid text exits non-zero before writing anything. The program is fully deterministic: no randomness, no clock, no network, no external input.
