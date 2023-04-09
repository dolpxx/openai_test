import openai
def dolpGPT(prompt: str) -> dict:
    response: dict = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    return ("\nGPT3.5: " + response["choices"][0]["message"]["content"] + '\n')