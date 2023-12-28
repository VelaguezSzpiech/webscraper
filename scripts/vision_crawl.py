from openai import OpenAI
import subprocess
import base64
import json
import os

api_key = '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'
model = OpenAI(api_key=api_key)

model.timeout = 10

def image_b64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

prompt = input("You: ")

# Use a variable for the image file path
screenshot_path = "E:/Ai_Systems/pythonwebscraper/image/image.jpg"

messages = [
    {
        "role": "system",
        "content": "You are a web crawler. Your job is to give the user a URL to go to in order to find the answer to the question. Go to a direct URL that will likely have the answer to the user's question. Respond in the following JSON format: {\"url\": \"<put url here>\"}",
    },
    {
        "role": "user",
        "content": prompt,
    }
]

while True:
    while True:
        response = model.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages,
            max_tokens=1024,
            response_format={"type": "json_object"},
            seed=2232,
        )

        message = response.choices[0].message
        message_json = json.loads(message.content)
        url = message_json["url"]

        messages.append({
            "role": "assistant",
            "content": message.content,
        })

        print(f"Crawling {url}")

        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)

        result = subprocess.run(
            ["node", "E:/Ai_Systems/pythonwebscraper/scripts/js/screenshot.js", url],
            capture_output=True,
            text=True
        )

        exitcode = result.returncode
        output = result.stdout

        if not os.path.exists(screenshot_path):
            print("ERROR: Trying different URL")
            messages.append({
                "role": "user",
                "content": "I was unable to crawl that site. Please pick a different one."
            })
        else:
            break

    b64_image = image_b64(screenshot_path)

    response = model.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "system",
                "content": "Your job is to answer the user's question based on the given screenshot of a website. Answer the user as an assistant, but don't tell that the information is from a screenshot or an image. Pretend it is information that you know. If you can't answer the question, simply respond with the code `ANSWER_NOT_FOUND` and nothing else.",
            }
        ] + messages[1:] + [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": f"data:image/jpeg;base64,{b64_image}",
                    },
                    {
                        "type": "text",
                        "text": prompt,
                    }
                ]
            }
        ],
        max_tokens=1024,
    )

    message = response.choices[0].message
    message_text = message.content

    if "ANSWER_NOT_FOUND" in message_text:
        print("ERROR: Answer not found")
        messages.append({
            "role": "user",
            "content": "I was unable to find the answer on that website. Please pick another one"
        })
    else:
        print(f"GPT: {message_text}")
        prompt = input("\nYou: ")
        messages.append({
            "role": "user",
            "content": prompt,
        })
