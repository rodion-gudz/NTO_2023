def solve(source: str, mask: str):
    result = ""
    new_data = ""

    last_index = len(source) - 1
    mask_index = len(mask) - 1

    reserved_value = 0

    for i in range(len(source)):
        print("-------------------")
        print(source[last_index - i])
        print(mask[mask_index - i])
        if new_data == "" and source[last_index - i] != mask[mask_index - i]:
            result += "0"
            new_data += "0"
        elif new_data == "" and source[last_index - i] == mask[mask_index - i]:
            result += "1"
            new_data = source + new_data
        elif source[last_index - i] != mask[mask_index - i]:
            result += "0"
            new_data += "0"

    return result[::-1]


source = "10001"
mask = "11111111110"
print(solve(source, mask))