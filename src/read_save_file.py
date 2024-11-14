def read_input_file(input_file_path: str):
    """
    This function reads input file and returns its content.
    :param input_file_path: path to input file
    :return: content od input file
    """
    with open(input_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content


def save_to_html_file(output_file: str, content: str):
    """
    This function saves the given content to a html file.
    :param output_file:
    :param content:
    :return:
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
            print(f"HTML file saved to {output_file}")
    except Exception as e:
        print(e)
