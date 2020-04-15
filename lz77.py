from math import log2, ceil

text = list(str(input()))

window = ['.' for i in range(9)]
buffer = text[0:5]
lines_count = 0


def print_all(wind, buff, dis, cnt, let):
    for j in wind:
        print(j, end='')
    print('\t', end='')
    for k in buff:
        print(k, end='')
    print('\t<{}, {}, \'{}\'>'.format(dis, cnt, let))


print('сөздік(9)\tбуфер(5)\tкод')

while buffer[0] != '.':
    if not text[len(text) - 1] in buffer:
        flag = True
        for i in range(5, len(text)):

            if not flag:
                flag = True
                continue

            if buffer[0] in window:
                window_r = list(reversed(window))

                dist = (len(window_r) - window_r.index(buffer[0])) - 1
                count = window.count(buffer[0])
                letter = buffer[1]

                print_all(window, buffer, dist, count, letter)
                lines_count += 1

                window.pop(0)
                window.pop(0)
                window.append(buffer[0])
                window.append(buffer[1])
                buffer.pop(0)
                buffer.pop(0)
                buffer.append(text[i])
                buffer.append(text[i+1])
                flag = False
            else:
                dist = 0
                count = 0
                letter = buffer[0]

                print_all(window, buffer, dist, count, letter)
                lines_count += 1

                window.pop(0)
                window.append(buffer[0])
                buffer.pop(0)
                buffer.append(text[i])
    else:
        if buffer[0] in window:
            window_r = list(reversed(window))

            dist = len(window_r) - window_r.index(buffer[0]) - 1
            count = window.count(buffer[0])
            letter = buffer[1]

            print_all(window, buffer, dist, count, letter)
            lines_count += 1

            window.pop(0)
            window.pop(0)
            window.append(buffer[0])
            window.append(buffer[1])
            buffer.pop(0)
            buffer.pop(0)
            buffer.append('.')
            buffer.append('.')
        else:
            dist = 0
            count = 0
            letter = buffer[0]

            print_all(window, buffer, dist, count, letter)
            lines_count += 1

            window.pop(0)
            window.append(buffer[0])
            buffer.pop(0)
            buffer.append('.')

ML = lines_count * (ceil(log2(len(window) - 1)) + ceil(log2(len(buffer) + 1)) + 8)
print('\nML = {} бит'.format(ML))
