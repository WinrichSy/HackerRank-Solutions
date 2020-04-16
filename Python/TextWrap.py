#Text Wrap
#https://www.hackerrank.com/challenges/text-wrap/problem

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(max_width)
    word_list = wrapper.wrap(text=string)
    return '\n'.join(word_list)
