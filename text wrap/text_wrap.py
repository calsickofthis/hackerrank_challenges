import textwrap

def wrap(string, max_width):
    # Wrap this text.
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    for element in word_list:
        if element != 'None':
            print(element)
    return ''

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)