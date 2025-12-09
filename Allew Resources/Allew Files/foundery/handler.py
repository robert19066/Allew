import subprocess

def run(model_name, prompt):
    cmd = ["foundry", "run", "--model", model_name, "--prompt", prompt]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
