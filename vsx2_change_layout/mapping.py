from collections import defaultdict

LAYOUT_S = {
    'en_qwerty': '`1234567890-=~!@#$%^&*()_+qwertyuiop[]\\QWERTYUIOP{}|asdfghjkl;\'ASDFGHJKL:"zxcvbnm,./ZXCVBNM<>?',
    'ru_qwerty': 'ё1234567890-=Ё!"№;%:?*()_+йцукенгшщзхъ\\ЙЦУКЕНГШЩЗХЪ|фывапролджэФЫВАПРОЛДЖЭячсмитьбю.ЯЧСМИТЬБЮ,',
    'ua_qwerty': '`1234567890-=~!"№;%:?*()_+йцукенгшщзхїґЙЦУКЕНГШЩЗХЇҐфівапролджєФІВАПРОЛДЖЄячсмитьбю.ЯЧСМИТЬБЮ,'
}

CACHE_D = defaultdict(dict)


def get_mapping(layout):
    layout_str = LAYOUT_S.get(layout)
    if not LAYOUT_S.get(layout):
        raise NotImplementedError()
    if not CACHE_D.get(layout):
        CACHE_D[layout] = dict(zip(layout_str, range(len(layout_str))))
    return CACHE_D[layout]


def get_layout_str(layout):
    return LAYOUT_S[layout]


def get_full_mapping():
    res_d = {}
    for i in LAYOUT_S.keys():
        res_d.update(get_mapping(i))
    return res_d
