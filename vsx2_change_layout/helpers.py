from .mapping import get_layout_str, get_mapping, get_full_mapping


def change_layout(
    source_str: 'str',
    source_layout: 'str'=None,
    destination_layout: 'str'='en_qwerty'
):
    if source_layout:
        source_map = get_mapping(source_layout)
    else:
        source_map = get_full_mapping()
    destination_str = get_layout_str(destination_layout)
    res = ''
    for char in source_str:
        idx = source_map.get(char)
        if idx:
            res += destination_str[idx]
        else:
            res += char
    return res
