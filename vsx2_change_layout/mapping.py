from memoized_property import memoized_property


class LayoutError(Exception):
    pass


class Layout:
    def __init__(self, char_seq, skip_in_all=False):
        self.char_seq = char_seq
        self.skip_in_all = skip_in_all

    @memoized_property
    def mapping(self):
        return dict(zip(self.char_seq, range(len(self.char_seq))))

    def get_char_by_position(self, position):
        try:
            return self.char_seq[position]
        except IndexError as e:
            raise LayoutError(e)


LAYOUT_S = {
    'en_qwerty': Layout(
        '`1234567890-=' +
        '~!@#$%^&*()_+' +
        'qwertyuiop[]\\' +
        'QWERTYUIOP{}|' +
        'asdfghjkl;\'' +
        'ASDFGHJKL:"' +
        'zxcvbnm,./' +
        'ZXCVBNM<>?'
    ),
    'ru_qwerty': Layout(
        'ё1234567890-=' +
        'Ё!"№;%:?*()_+' +
        'йцукенгшщзхъ\\' +
        'ЙЦУКЕНГШЩЗХЪ|' +
        'фывапролджэ' +
        'ФЫВАПРОЛДЖЭ' +
        'ячсмитьбю.' +
        'ЯЧСМИТЬБЮ,'
    ),
    'ua_qwerty': Layout(
        '`1234567890-=' +
        '~!"№;%:?*()_+' +
        'йцукенгшщзхїґ' +
        'ЙЦУКЕНГШЩЗХЇҐ' +
        'фівапролджє' +
        'ФІВАПРОЛДЖЄ' +
        'ячсмитьбю.' +
        'ЯЧСМИТЬБЮ,'
    ),
    'en_dvorak': Layout(
        '`1234567890[]' +
        '~!@#$%^&*(){}' +
        '\',.pyfgcrl/=\\' +
        '"<>PYFGCRL?+|' +
        'aoeuidhtns-' +
        'AOEUIDHTNS_' +
        ';qjkxbmwvz' +
        ':QJKXBMWVZ', skip_in_all=True),
}


def get_layout(layout_name):
    try:
        return LAYOUT_S[layout_name]
    except KeyError:
        raise LayoutError("Layout not found.")


def get_full_mapping():
    res_d = {}
    for layout in LAYOUT_S.values():
        if not layout.skip_in_all:
            res_d.update(layout.mapping)
    return res_d


def get_all_layouts():
    return LAYOUT_S.keys()
