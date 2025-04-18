from ollama import Client
import time

ollama_client = Client()

def llama(prompt,
          add_inst=True,
          model="llama3.2",
          temperature=0.0,
          max_tokens=1024,
          verbose=False,
          base = 2,
          max_tries=3):

    if add_inst:
        prompt = f"[INST]{prompt}[/INST]"

    if verbose:
        print(f"Prompt:\n{prompt}\n")
        print(f"model: {model}")

    messages = [{"role": "user", "content": prompt}]

    wait_seconds = [base**i for i in range(max_tries)]

    for num_tries in range(max_tries):
        try:
            response = ollama_client.chat(
                model=model,
                messages=messages,
                stream=False,
                options={'num_predict': max_tokens, 'generation_settings': {'temperature': temperature}}
            )
            return response['message']['content']
        except Exception as e:
            print(f"Ollama error (try {num_tries + 1}/{max_tries}): {e}")
            time.sleep(wait_seconds[num_tries])

    print(f"Tried {max_tries} times to get a response from ollama.")
    return None