def print_box(text):
    text_length = len(text)
    print('+' + '-'*(text_length+2) + '+')
    print('| ' + text + ' |')
    print('+' + '-'*(text_length+2) + '+')

print_box("Hello World")
