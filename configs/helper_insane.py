from configs import base

# Аккаунт
ACCOUNT_NAME = "helper_insane"
ACCOUNT_SESSION = "helper_insane_session"
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
    -1002021191245: {
        'target': [-1002047029343, -1002129911279],
        'pdf_watermark': {
            -1002047029343: base.PDF_INSANE_WATERMARK,
            -1002129911279: base.PDF_INBLACK_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001907076507: {
        'target': [-1002009738876, -1002019438834],
        'pdf_watermark': {
            -1002009738876: base.PDF_INSANE_WATERMARK,
            -1002019438834: base.PDF_INBLACK_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001906649363: {
        'target': [-1002118304903, -1001913794737],
        'pdf_watermark': {
            -1002118304903: base.PDF_INSANE_WATERMARK,
            -1001913794737: base.PDF_INBLACK_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001980004382: {
        'target': [-1002145263420, -1002032966024],
        'pdf_watermark': {
            -1002145263420: base.PDF_INSANE_WATERMARK,
            -1002032966024: base.PDF_INBLACK_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002069969587: {
        'target': [-1002115717802, -1002026785703],
        'pdf_watermark': {
            -1002115717802: base.PDF_INSANE_WATERMARK,
            -1002026785703: base.PDF_INBLACK_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002026471360: {
        'target': [-1002033288438, -1002101017714],
        'pdf_watermark': {
            -1002033288438: base.PDF_INSANE_WATERMARK,
            -1002101017714: base.PDF_INBLACK_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1001875008224: {
        'target': [-1001850139609, -1002126954655],
        'pdf_watermark': {
            -1001850139609: base.PDF_INSANE_WATERMARK,
            -1002126954655: base.PDF_INBLACK_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
    -1002077332944: {
        'target': [-1002122994781, -1002068405417],
        'pdf_watermark': {
            -1002122994781: base.PDF_INSANE_WATERMARK,
            -1002068405417: base.PDF_INBLACK_WATERMARK,
        },
        'emojis_for_replace': EMOJIS_REPLACEMENT,
        'text_for_remove': TEXT_FOR_REMOVE,
        'send_missed_messages': {'enable': True, 'count': 50}
    },
}
