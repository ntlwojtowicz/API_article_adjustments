from openai import OpenAI
from dotenv import load_dotenv


def generate_prompt(input_file_content: str):
    """
    This function generates prompt to read input file and make specified adjustments
    :param input_file_content: content of input file
    :return: generated prompt
    """
    return ("Make following adjustments:"
            "1. Use HTML tags to structure given content."
            "2. Specify places to add graphics (e.g. after each paragraph). "
            "Don't place graphics after text starting with '*' - it's the end of article."
            "3. Add <img> tags with src='image_placeholder.jpg' attributes to places specified in step 2.."
            "4. Add alt attribute to each image with detailed description which can be used to generate graphics."
            "5. Place captions under each graphics using the appropriate HTML tag."
            "6. Don't add CSS and Javascript code. "
            "8. Don't add <html>, <head> and <body> tags."
            "9. Make changes in that way that text only contains content between <body> and </body> tags,"
            "but don't add <body> tags."
            "10. Don't add '''html tags''."
            f"to following text: {input_file_content}.")


def connect_with_api(prompt: str):
    """
    This function connects to API OpenAI and return response from given prompt
    :param prompt: prompt to API
    :return: response from API
    """

    load_dotenv()
    client = OpenAI()

    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o-mini",
    )

    return completion.choices[0].message.content
