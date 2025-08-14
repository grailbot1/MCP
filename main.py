from fastapi import FastAPI, Request
import subprocess, os

app = FastAPI()

@app.post("/run")
async def run_command(request: Request):
    data = await request.json()
    cmd = data.get("cmd")
    if not cmd:
        return {"error": "No command provided"}
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
        return {"stdout": result.stdout, "stderr": result.stderr}
    except Exception as e:
        return {"error": str(e)}
