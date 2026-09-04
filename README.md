# handoff-shortcuts

iOS Shortcut that splits a long clipboard into Discord-sized pieces (1900 characters, cut at paragraph breaks). Pair it with the Handoff Discord bot, which copies a thread *out* of Discord. This shortcut is how you paste a long prompt *in*.

## Install on iPhone

1. Open the latest [Release](https://github.com/Admin-AAVS/handoff-shortcuts/releases/latest) in Safari.
2. Tap `Split-for-Discord.shortcut`.
3. iOS asks **Add Shortcut**. Add it.
4. Or save the file in Files, then tap it there → Add Shortcut.

Unsigned imports were removed in iOS 15. This file is signed on a GitHub macOS runner (`shortcuts sign --mode anyone`) so you do not need a Mac.

## Use it

1. Copy a long note (try ~6,000 characters).
2. Run **Split for Discord**.
3. You get **Piece 1 of N copied**. Paste into Discord, tap OK, repeat.
4. A notification says `Done. N pieces.` when it finishes. Cancel on any alert to stop.

## Nitro

The limit is the Text action named `Limit`, currently `1900`. Discord Nitro can take 4000; edit `Limit` to `3900` so emoji and punctuation still fit.

## Handoff bot

The bot that exports a Discord thread as a clean `.md` / `.txt` file is not public yet. Placeholder: `https://handoff.example` (replace when the landing page ships).

## Build

Push to `main` (or a `v*` tag) runs `.github/workflows/sign.yml` on `macos-14`. It lints the unsigned plist, signs it, uploads the artifact, and on a `v*` tag attaches it to a GitHub Release.

```
python scripts/lint_plist.py shortcuts/split-for-discord.plist
```

Agent: grok-4.6 (Grok Build CLI / Discord) — 2026-09-04
Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
