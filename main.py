import os
from openai import OpenAI

message_to_chatgpt = "hi this is a test, answer this riddle in 1 word: what is the role of the leader of the united states?"
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": message_to_chatgpt
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message.content)