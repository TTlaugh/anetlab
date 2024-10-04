import lib.utils

lib.utils.vendor_loader()

from prompt_toolkit import prompt

answer = prompt('Give me some input: ')
print('You said: %s' % answer)
