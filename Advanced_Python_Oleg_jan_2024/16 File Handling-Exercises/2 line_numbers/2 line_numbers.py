from string import punctuation

with open("input_text.txt", "r") as input_file, open("output_text.txt", "w") as output_file:
    result = []
    for row, line in enumerate(input_file):
        letters_count = 0
        punct_count = 0
        for ch in line:
            if ch.isalpha():
                letters_count += 1
            elif ch in punctuation:
                punct_count += 1
        result.append(f"Line {row + 1}: {line[:-1]} ({letters_count})({punct_count})")
    output_file.write('\n'.join(result))