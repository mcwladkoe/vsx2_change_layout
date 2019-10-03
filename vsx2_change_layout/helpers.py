from .mapping import get_layout, get_full_mapping


def change_layout(
    source_str: 'str',
    source_layout: 'str'=None,
    destination_layout: 'str'='en_qwerty'
):
    if source_layout:
        source_map = get_layout(source_layout).mapping
    else:
        source_map = get_full_mapping()
    layout = get_layout(destination_layout)
    res = ''
    for char in source_str:
        idx = source_map.get(char)
        if idx:
            res += layout.get_char_by_position(idx)
        else:
            res += char
    return res
