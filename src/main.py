from read_save_file import read_input_file, save_to_html_file
from connect_with_api import connect_with_api, generate_prompt


def main():
    input_file = "../tresc_artykulu.txt"
    output_file = "../artykul.html"

    input_file_content = read_input_file(input_file)

    generated_prompt = generate_prompt(input_file_content)
    content_from_prompt = connect_with_api(generated_prompt)

    save_to_html_file(output_file, content_from_prompt)


if __name__ == "__main__":
    main()
