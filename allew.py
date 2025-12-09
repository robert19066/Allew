import argparse
import importlib
import json
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv("Allew Resources/.env")

BASE_DIR = Path(__file__).parent
FILES_DIR = BASE_DIR / "Allew Resources" / "Allew Files"

# Load provider handler dynamically
def load_provider(provider_name):
    provider_path = FILES_DIR / provider_name

    if not provider_path.exists():
        raise ValueError(f"Provider '{provider_name}' does not exist.")

    handler_path = provider_path / "handler"
    module_name = f"Allew Files.{provider_name}.handler"

    spec = importlib.util.spec_from_file_location(
        module_name, str(provider_path / "handler.py")
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


# Run Model
def run_model(provider, model_name, method=None, use_cuda=False):
    handler = load_provider(provider)
    prompt = input("Prompt: ")

    if provider == "hugging-face":
        return handler.run(model_name, prompt, method=method, use_cuda=use_cuda)

    return handler.run(model_name, prompt)



# Download Local Model (for HF/Ollama/Foundery)
def download_model(provider, model_name):
    print(f"Downloading model '{model_name}' for provider '{provider}'...")

    if provider == "hugging-face":
        from transformers import AutoTokenizer, AutoModelForCausalLM

        AutoTokenizer.from_pretrained(model_name)
        AutoModelForCausalLM.from_pretrained(model_name)

        print("HuggingFace model downloaded successfully.")
        return

    print("Provider does not support downloading or is handled externally.")


# CLI Entry Point
def main():
    parser = argparse.ArgumentParser(description="Allew AI Model Runner")

    parser.add_argument("--provider", type=str, required=True, help="AI provider")
    parser.add_argument("--model", type=str, required=True, help="Model name")
    parser.add_argument("--dwmodel", action="store_true", help="Download model")
    parser.add_argument("--runmodel", action="store_true", help="Run model")
    parser.add_argument("--cudax", action="store_true", help="Enable CUDA acceleration")
    parser.add_argument("--method", type=str, choices=["local", "remote"], required=True,
                    help="Execution method: local or remote (HF only)")


    args = parser.parse_args()

    if args.dwmodel:
        download_model(args.provider, args.model)
    elif args.runmodel:
        output = run_model(args.provider, args.model, method=args.method, use_cuda=args.cudax)
        print("\n===== MODEL OUTPUT =====\n")
        print(output)
        print("\n========================\n")
    else:
        print("You must specify either --dwmodel or --runmodel.")


if __name__ == "__main__":
    main()
