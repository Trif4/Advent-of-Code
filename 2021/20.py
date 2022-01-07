from aocd import data, submit

algorithm, input_image = data.split('\n\n')


def enhance(image, out_of_bounds_char):
    lines = image.splitlines()
    new_image = ''

    for y in range(-1, len(lines)+1):
        for x in range(-1, len(lines[0]) + 1):
            binary = ''
            for j in (-1, 0, 1):
                ny = y + j
                for i in (-1, 0, 1):
                    nx = x + i
                    if 0 <= nx < len(lines[0]) and 0 <= ny < len(lines):
                        c = lines[ny][nx]
                    else:
                        c = out_of_bounds_char
                    binary += '1' if c == '#' else '0'
            new_image += algorithm[int(binary, 2)]
        new_image += '\n'

    next_oob_char = algorithm[0] if out_of_bounds_char == '.' else '.'

    return new_image, next_oob_char


# Part 1
image, oob_char = enhance(input_image, '.')
image, oob_char = enhance(image, oob_char)

# submit(image.count('#'))

# Part 2
for _ in range(48):
    image, oob_char = enhance(image, oob_char)

submit(image.count('#'))