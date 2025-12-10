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
Create the Allew Resources/.env file and add your API keys.
For OpenAI use OPENAI_API_KEY
For Google Gemeni, use GOOGLE_API_KEY
And for HugginngFace use HUGGINGFACE_ACCES_TOKEN

## How to use

To run a model, use the following command(works only for foundery,huggingface and ollama):
(not necesary)
Flags:
- `--provider<provider>` = specifies the provider.
- `--model<model>` = specifies the model
- `--dwmodel` = dowloads a model(only necesary for foundery)
- `--runmodel` = runs the model of course

**(ONLY FOR HUGGINGFACE)**
- `--cudax` = use CUDA hardware acceleration
- `--method<local or remote>` = specifies if the model shall be runned localy or remotely(using http)

Sorry for the inconvenience, but running remote models is curently not possible, as the api is compleately broken. Will be fixed in a future patch!
cudax means cuda acceleration.

# Known issues
- `--method remote` displaying a error message(the feature has been temporary disabled due to bugs, will be added back(maybe))
