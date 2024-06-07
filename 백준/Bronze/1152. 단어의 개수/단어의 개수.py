str = input()


sentences = str.split(' ')

if sentences[-1] == '':
    sentences.pop()

if sentences[0] == '':
    sentences.pop(0)

print(len(sentences))