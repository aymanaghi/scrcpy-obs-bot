# scrcpy-obs-bot

Tiny Python helper that:
1) connects to OBS (WebSocket v5),
2) starts OBS recording,
3) launches `scrcpy --record` to capture Android,
4) stops both when you press ENTER.

## Quick start (Fedora)
- `sudo dnf install scrcpy android-tools obs-studio -y`
- `python3 -m venv .venv && source .venv/bin/activate`
- `pip install simpleobsws python-dotenv`
- copy `.env.example` to `.env` and set your OBS password
- `python record_android_obs.py`

**Never commit `.env`.**
