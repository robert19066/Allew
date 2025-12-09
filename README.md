# What is Allew?

Allew is a open-source tool for running and managing AI models. It provides simple yet powerfull CLI,and compatability with various AI providers like Google,OpenAI, HuggingFace, Foundery(windows), etc.

## Providers

### ^ means local models only

- OpenAI
- Google
- HuggingFace(can run both local and remote models)
- ^Foundery (Windows only)

# Setup

## Requirements

pip install openai google-generativeai transformers accelerate torch,huggingface_hub python-dotenv requests

or for torch for cpu: pip install torch --index-url https://download.pytorch.org/whl/cpu


## Dotenv

To use OpenAI,Google and HuggingFace(api) models,you need to set up environment variables.
Edit the Allew Resources/.env file and add your API keys.

## How to use

To run a model, use the following command(works only for foundery,huggingface and ollama):

```bash
python allew.py --provider <provider> --model <model> --dwmodel
```

To run a model:

```bash
python allew.py --provider <prov> --model <model> --runmodel
```

(ONLY FOR HUGGINGFACE)
To run a model with cuda support:

```bash
python allew.py --provider <prov> --model <model> --runmodel --cudax
```

cudax means cuda acceleration.
