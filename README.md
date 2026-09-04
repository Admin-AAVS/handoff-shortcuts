# Split for Discord

Pastes long text into Discord in pieces under the 2000-char limit, from your iPhone.

## Install

https://www.icloud.com/shortcuts/0934d3f87e50462184916f7baa50a45a

Tap that link → **Add Shortcut**.

**Required: run it via Back Tap.** Settings → Accessibility → Touch → Back Tap → Triple Tap → Split for Discord. If you run it from the Shortcuts app and switch to Discord, iOS ends it after piece 2.

## Use

1. Copy long text.
2. Open Discord.
3. Triple-tap the back of the phone.
4. Paste, tap OK, repeat until "of N" is done.

## Nitro

Edit the `1900` Text action to `3900`.

## Source

`shortcuts/split-for-discord.plist` is the reference source. It is **not** installable as-is. Signing needs a Mac signed into iCloud. GitHub runners are not.

Part of the Handoff bundle: `https://handoff.example`

Agent: grok-4.6 (Grok Build CLI / Discord) — 2026-09-04
Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>
