import asyncio
import simpleobsws

OBS_HOST = "localhost"
OBS_PORT = 4455
OBS_PASSWORD = "zyJ0vfo9rpf94syx"  # set this to your real one

async def main():
    url = f"ws://{OBS_HOST}:{OBS_PORT}"
    params = simpleobsws.IdentificationParameters(ignoreNonFatalRequestChecks=False)
    ws = simpleobsws.WebSocketClient(url=url, password=OBS_PASSWORD, identification_parameters=params)

    await ws.connect()
    await ws.wait_until_identified()
    print("✅ Connected to OBS v5")

    # get version info (fixed syntax)
    req = simpleobsws.Request("GetVersion")
    resp = await ws.call(req)
    print("🎥 OBS Version:", resp.responseData)

    # optional: start & stop recording test
    # await ws.call(simpleobsws.Request("StartRecord"))
    # await asyncio.sleep(3)
    # await ws.call(simpleobsws.Request("StopRecord"))

    await ws.disconnect()
    print("🔌 Disconnected cleanly")

if __name__ == "__main__":
    asyncio.run(main())
