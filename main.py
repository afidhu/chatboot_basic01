import sys
from ollama import Client


def main():
    # Ensure Windows console prints UTF-8 and avoids cp1252 encoding errors.
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    """Sample Ollama chat call."""
    try:
        client = Client()

        model_name = "llama3"
        try:
            models = client.list().models
            if models:
                model_name = models[0].model
        except Exception:
            pass

        print(f"Using model: {model_name}")

        response = client.chat(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say hello in a friendly way."},
            ],
        )

        # `response` is typically a ChatResponse object with `message` and/or simple fields.
        print("Model output:")
        if hasattr(response, "message") and response.message is not None:
            # `response.message` is a Message object with `content`.
            content = getattr(response.message, "content", None)
            if content is not None:
                print(content)
                return

        # Fallback for iterators / chunks
        if hasattr(response, "__iter__"):
            for chunk in response:
                text = getattr(chunk, "content", None) or getattr(chunk, "message", None)
                if isinstance(text, str):
                    print(text, end="")
            return

        print("Unable to extract content from response.")

    except Exception as e:
        print("Error:", type(e).__name__, str(e))


if __name__ == "__main__":
    main()