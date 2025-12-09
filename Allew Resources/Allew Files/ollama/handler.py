import subprocess
import json

def run(model_name, prompt):
    process = subprocess.Popen(
        ["ollama", "run", model_name],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    process.stdin.write(prompt)
    process.stdin.close()

    output = process.stdout.read()
    process.wait()

    return output
