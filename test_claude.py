import os
from litellm import completion, batch_completion
import json

with open("api_keys.json", "r") as f:
    api_keys = json.load(f)
    for k in api_keys:
        os.environ[k] = api_keys[k]

response = completion(
  model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0",
  #"bedrock/anthropic.claude-3-sonnet-20240229-v1:0",
  messages=[{ "content": "Hello, how are you?","role": "user"}]
)

print(response)

response = batch_completion(
    model="bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0",
    messages=[[{ "content": "Hello, how are you?","role": "user"}], [{ "content": "Hello, how are you?","role": "user"}]],
    temperature=1.0,
    max_tokens=4096,
    top_p=1,
)

print(response)