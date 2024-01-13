from configs import base

# Аккаунт
ACCOUNT_NAME = "chips_insane"
ACCOUNT_SESSION = "chips_insane_session"
API_ID = 
API_HASH = ''

# Настройка поста
TEXT_FOR_REMOVE = [
    '🧠 О чём занятие?',
    '🧠 О чем занятие?'
]

EMOJIS_REPLACEMENT = {
    '👆': '🔼',
    '🔗': '📚',
    '🔭': '🚀',
    '🇷🇺': '🍒',
    '🏛': '📕',
    '⚖️': '🍊',
    '👨‍🎓': '✨',
    '💻': '🖥',
    '💿': '🥥',
    '📝': '🖋',
    '📖': '🗒',
    '📄': '🪄',
    '📐': '🪼',
    '🧬': '🌿',
    '🇬🇧': '🫕',
    '📏': '🍇',
    '🎭': '📚',
    '🗣': '🌊',
}

# Настройка связок каналов
CHANNELS_LINKS = {
    -1002100608337: {
        'target': [-1002101057337, -1002064216109],
        'pdf_watermark': {
            -1002101057337: base.PDF_INSANE_WATERMARK,
            -1002064216109: base.PDF_INBLACK_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001878810415: {
        'target': [-1002118967843],
        'pdf_watermark': {
            -1002118967843: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002089326924: {
        'target': [-1002064525407],
        'pdf_watermark': {
            -1002064525407: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002129053757: {
        'target': [-1001950974270],
        'pdf_watermark': {
            -1001950974270: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002038754224: {
        'target': [-1002140024403],
        'pdf_watermark': {
            -1002140024403: base.PDF_INBLACK_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },

    -1002140354840: {
        'target': [-1002101629483, -1001824470981],
        'pdf_watermark': {
            -1002101629483: base.PDF_INSANE_WATERMARK,
            -1001824470981: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002029276392: {
        'target': [-1002037268961, -1001990321789],
        'pdf_watermark': {
            -1002037268961: base.PDF_INSANE_WATERMARK,
            -1001990321789: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002015899398: {
        'target': [-1001990941015, -1002088504178],
        'pdf_watermark': {
            -1001990941015: base.PDF_INSANE_WATERMARK,
            -1002088504178: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001737802302: {
        'target': [-1002124570931, -1002059335740],
        'pdf_watermark': {
            -1002124570931: base.PDF_INSANE_WATERMARK,
            -1002059335740: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002095518859: {
        'target': [-1001990937171, -1001976975096],
        'pdf_watermark': {
            -1001990937171: base.PDF_INSANE_WATERMARK,
            -1001976975096: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001668683757: {
        'target': [-1002087784082, -1002050827740],
        'pdf_watermark': {
            -1002087784082: base.PDF_INSANE_WATERMARK,
            -1002050827740: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002112976596: {
        'target': [-1002096788234, -1002104376805],
        'pdf_watermark': {
            -1002096788234: base.PDF_INSANE_WATERMARK,
            -1002104376805: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002121602961: {
        'target': [-1002066865248, -1002079709374],
        'pdf_watermark': {
            -1002066865248: base.PDF_INSANE_WATERMARK,
            -1002079709374: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002096262333: {
        'target': [-1002087010315, -1001938907223],
        'pdf_watermark': {
            -1002087010315: base.PDF_INSANE_WATERMARK,
            -1001938907223: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001902661742: {
        'target': [-1002035259752, -1002073101732],
        'pdf_watermark': {
            -1002035259752: base.PDF_INSANE_WATERMARK,
            -1002073101732: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001997008802: {
        'target': [-1002087605726, -1002096106413],
        'pdf_watermark': {
            -1002087605726: base.PDF_INSANE_WATERMARK,
            -1002096106413: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002057697944: {
        'target': [-1002142705971, -1002146162020],
        'pdf_watermark': {
            -1002142705971: base.PDF_INSANE_WATERMARK,
            -1002146162020: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002135927329: {
        'target': [-1002044088944, -1002102055007],
        'pdf_watermark': {
            -1002044088944: base.PDF_INSANE_WATERMARK,
            -1002102055007: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002077332944: {
        'target': [-1002074471970, -1002079709374],
        'pdf_watermark': {
            -1002074471970: base.PDF_INSANE_WATERMARK,
            -1002079709374: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
}
