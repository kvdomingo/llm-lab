# GenAI Lab

## Prerequisites

- [ ] [Mise](https://mise.jdx.dev)
- [ ] Docker
- [ ] Recent graphics drivers + CUDA support

## Running locally

```shell
# Install prerequisites
mise install

# Enter Poetry shell
poetry shell

# Start the Ollama backend and Chroma vector database
task

# Run the chatbot
python -m vanilla
```

The chatbot uses the  `llama3.2` (3B) model by default. To change the model, get the model name from
the Ollama [models](https://ollama.com/library) list and pass it to the `-m`/`--model` argument.

```shell
python -m vanilla -- --model gemma2
```
