import asyncio
import subprocess
import datetime
import simpleobsws
import signal
import time
from pathlib import Path

OBS_HOST = "localhost"
OBS_PORT = 4455
OBS_PASSWORD = ""  # use the same as your OBS settings

async def main():
    # connect to OBS
    url = f"ws://{OBS_HOST}:{OBS_PORT}"
    params = simpleobsws.IdentificationParameters(ignoreNonFatalRequestChecks=False)
    ws = simpleobsws.WebSocketClient(url=url, password=OBS_PASSWORD, identification_parameters=params)

    await ws.connect()
    await ws.wait_until_identified()
    print("✅ Connected to OBS")

    # start recording
    await ws.call(simpleobsws.Request("StartRecord"))
    print("🎥 OBS recording started")

    # start scrcpy
    output_dir = Path.home() / "Videos"
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    video_path = output_dir / f"android_{timestamp}.mp4"
    scrcpy_cmd = ["scrcpy", "--record", str(video_path)]
    proc = subprocess.Popen(scrcpy_cmd)
    print(f"📱 scrcpy launched and recording to {video_path}")

    try:
        input("💬 Press ENTER to stop recording...")
    finally:
        # stop scrcpy
        proc.send_signal(signal.SIGINT)
        time.sleep(1)
        if proc.poll() is None:
            proc.terminate()
        print("📴 scrcpy stopped")

        # stop OBS recording
        await ws.call(simpleobsws.Request("StopRecord"))
        print("🟥 OBS recording stopped")

        await ws.disconnect()
        print("🔌 Disconnected from OBS")

if __name__ == "__main__":
    asyncio.run(main())
