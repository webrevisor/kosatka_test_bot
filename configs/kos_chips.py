from configs import base

# Аккаунт
ACCOUNT_NAME = "kos_chips"
ACCOUNT_SESSION = "kos_chips_session"
API_ID = 28450705
API_HASH = 'a1b36bee6eabbc1da8685f87e713c123'

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
    -1002076759704: {
        'target': [-1002122544680, -1002095523939],
        'pdf_watermark': {
            -1002122544680: base.PDF_INSANE_WATERMARK,
            -1002095523939: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 3}
    },
    -1002060896068: {
        'target': [-1002041200636, -1002043792372],
        'pdf_watermark': {
            -1002041200636: base.PDF_INSANE_WATERMARK,
            -1002043792372: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 3}
    },
    -1002140354840: {
        'target': [-1002101629483, -1001824470981],
        'pdf_watermark': {
            -1002101629483: base.PDF_INSANE_WATERMARK,
            -1001824470981: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002029276392: {
        'target': [-1002037268961, -1001990321789],
        'pdf_watermark': {
            -1002037268961: base.PDF_INSANE_WATERMARK,
            -1001990321789: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002015899398: {
        'target': [-1001990941015, -1002088504178],
        'pdf_watermark': {
            -1001990941015: base.PDF_INSANE_WATERMARK,
            -1002088504178: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002096262333: {
        'target': [-1002087010315, -1001938907223],
        'pdf_watermark': {
            -1002087010315: base.PDF_INSANE_WATERMARK,
            -1001938907223: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001902661742: {
        'target': [-1002035259752, -1002073101732],
        'pdf_watermark': {
            -1002035259752: base.PDF_INSANE_WATERMARK,
            -1002073101732: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001875008224: {
        'target': [-1001850139609, -1002126954655],
        'pdf_watermark': {
            -1001850139609: base.PDF_INSANE_WATERMARK,
            -1002126954655: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002077332944: {
        'target': [-1002122994781, -1002068405417],
        'pdf_watermark': {
            -1002122994781: base.PDF_INSANE_WATERMARK,
            -1002068405417: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001737802302: {
        'target': [-1002124570931, -1002059335740],
        'pdf_watermark': {
            -1002124570931: base.PDF_INSANE_WATERMARK,
            -1002059335740: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002095518859: {
        'target': [-1001990937171, -1001976975096],
        'pdf_watermark': {
            -1001990937171: base.PDF_INSANE_WATERMARK,
            -1001976975096: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001668683757: {
        'target': [-1002087784082, -1002050827740],
        'pdf_watermark': {
            -1002087784082: base.PDF_INSANE_WATERMARK,
            -1002050827740: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002112976596: {
        'target': [-1002096788234, -1002104376805],
        'pdf_watermark': {
            -1002096788234: base.PDF_INSANE_WATERMARK,
            -1002104376805: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002121602961: {
        'target': [-1002066865248, -1002079709374],
        'pdf_watermark': {
            -1002066865248: base.PDF_INSANE_WATERMARK,
            -1002079709374: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001997008802: {
        'target': [-1002087605726, -1002096106413],
        'pdf_watermark': {
            -1002087605726: base.PDF_INSANE_WATERMARK,
            -1002096106413: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002021191245: {
        'target': [-1002047029343, -1002129911279],
        'pdf_watermark': {
            -1002047029343: base.PDF_INSANE_WATERMARK,
            -1002129911279: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001907076507: {
        'target': [-1002009738876, -1002019438834],
        'pdf_watermark': {
            -1002009738876: base.PDF_INSANE_WATERMARK,
            -1002019438834: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001906649363: {
        'target': [-1002118304903, -1001913794737],
        'pdf_watermark': {
            -1002118304903: base.PDF_INSANE_WATERMARK,
            -1001913794737: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001980004382: {
        'target': [-1002145263420, -1002032966024],
        'pdf_watermark': {
            -1002145263420: base.PDF_INSANE_WATERMARK,
            -1002032966024: base.PDF_INBLACK_WATERMARK
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
}
