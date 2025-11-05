from obswebsocket import obsws, requests

host = "localhost"
port = 4455   # change if yours is different
password = ""

try:
    ws = obsws(host, port, password)
    ws.connect()
    print("✅ Connected to OBS WebSocket")

    # test command: get current scene
    scene = ws.call(requests.GetCurrentProgramScene())
    print("🎬 Current Scene:", scene.getName())

    ws.disconnect()
    print("🔌 Disconnected")
except Exception as e:
    print("❌ Connection failed:", e)
