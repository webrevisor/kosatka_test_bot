from configs import base

# Аккаунт
ACCOUNT_NAME = "second"
ACCOUNT_SESSION = "second_session"
API_ID = 25837489
API_HASH = 'e5f3b968ea235e26b34426a5d387c4be'

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
    -1002013251075: {
        'target': [-1002076944436],
        'pdf_watermark': {
            -1002076944436: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001998465549: {
        'target': [-1002111722777],
        'pdf_watermark': {
            -1002111722777: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002054250629: {
        'target': [-1002096269102],
        'pdf_watermark': {
            -1002096269102: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002049685804: {
        'target': [-1002123925051],
        'pdf_watermark': {
            -1002123925051: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002139989415: {
        'target': [-1002042354500],
        'pdf_watermark': {
            -1002042354500: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001990673290: {
        'target': [-1002108904341],
        'pdf_watermark': {
            -1002108904341: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002072496306: {
        'target': [-1002136186563],
        'pdf_watermark': {
            -1002136186563: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002065732379: {
        'target': [-1001997934406],
        'pdf_watermark': {
            -1001997934406: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002028370847: {
        'target': [-1001533677410],
        'pdf_watermark': {
            -1001533677410: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002038583572: {
        'target': [-1002069166245],
        'pdf_watermark': {
            -1002069166245: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001947258382: {
        'target': [-1001882135193],
        'pdf_watermark': {
            -1001882135193: base.PDF_INSANE_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002073136433: {
        'target': [-1001845840377],
        'pdf_watermark': {
            -1001845840377: base.PDF_INSANE_WATERMARK,
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
}
