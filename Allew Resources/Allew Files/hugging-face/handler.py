import os
from huggingface_hub import InferenceClient
import requests
import json

def run_remote(model_name, prompt):
    print("Sorry for the inconvenience. Remote inference is currently disabled due to API key issues. and btw its absolutely awfull so yeah :/")
        
def run(model_name, prompt, method="remote", use_cuda=False):
    if method == "local":
        return run_local(model_name, prompt, use_cuda)
    elif method == "remote":
        return run_remote(model_name, prompt)
    else:
        raise ValueError(f"Invalid method: {method}. Must be 'local' or 'remote'.")

def run_local(model_name, prompt, use_cuda=False):
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM  # ← Seq2SeqLM, not CausalLM
    import torch

    device = "cuda" if use_cuda and torch.cuda.is_available() else "cpu"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)  # Fixed here

    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_new_tokens=256)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
