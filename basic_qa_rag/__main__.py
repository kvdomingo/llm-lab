from .basic_qa_rag import BasicQaRag, CliArguments

if __name__ == "__main__":
    import asyncio
    from argparse import ArgumentParser

    parser = ArgumentParser(
        description="Run a question answering chatbot in the terminal connecting to a locally hosted Ollama server."
    )
    parser.add_argument(
        "-m",
        "--model",
        default=None,
        help="Ollama chat model name",
        type=str,
    )
    parser.add_argument(
        "-e",
        "--embedding-model",
        default=None,
        help="Ollama embedding model name",
        type=str,
    )
    parser.add_argument(
        "-c",
        "--collection-name",
        default="basic_qa_rag",
        help="Chroma/document collection name",
        type=str,
    )
    parsed = parser.parse_args()
    validated = CliArguments.model_validate(parsed)

    qa = BasicQaRag(validated)
    asyncio.run(qa())
