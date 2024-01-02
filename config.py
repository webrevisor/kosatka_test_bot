# Telegram API
API_ID = 28450705
API_HASH = 'a1b36bee6eabbc1da8685f87e713c123'

# Логирование
LOG_FILE = 'telegram_bot.log'
LOG_FORMAT = '[%(levelname)s %(asctime)s] %(message)s'

PDF_DPI = 230
PDF_DOWNLOAD_DIRECTORY = 'downloads'

FIRST_CHANNELS_WATERMARK = {
    'path': 'watermarks/insane.png',
    'scale': 0.32,
    'angle': 0,
    'opacity': 0.59,
}

SECOND_CHANNELS_WATERMARK = {
    'path': 'watermarks/inblack.png',
    'scale': 0.93,
    'angle': 45,
    'opacity': 0.21,
}

DEFAULT_TEXTS_REMOVE = '🧠 О чём занятие?'

DEFAULT_EMOJIS_REPLACEMENT = {
    '😂': '😄',
    '😳': '😭',
    '😊': '😏',
}

# Список исходных каналов
CHANNELS_LINKS = [
    {
        'source': [-1002076759704],
        'target': [-1002122544680, -1002095523939],
        'pdf_watermark': {
            -1002122544680: FIRST_CHANNELS_WATERMARK,
            -1002095523939: SECOND_CHANNELS_WATERMARK
        },
        'emojis_replacement': DEFAULT_EMOJIS_REPLACEMENT,
        'text_remove': DEFAULT_TEXTS_REMOVE,
        'send_missed_messages': {
            'enable': True,
            'count': 3,
        }
    },
    # {
    #     'source': [-1002140354840],
    #     'target': [-1002101629483, -1001824470981],
    #     'pdf_watermark': {
    #         -1002101629483: FIRST_CHANNELS_WATERMARK,
    #         -1001824470981: SECOND_CHANNELS_WATERMARK
    #     },
    #     'emojis_replacement': DEFAULT_EMOJIS_REPLACEMENT,
    #     'text_remove': DEFAULT_TEXTS_REMOVE,
    #     'send_missed_messages': {
    #         'enable': True,
    #         'count': 3,
    #     }
    # },
    #
    # {
    #     'source': [-1002029276392],
    #     'target': [-1002037268961, -1001990321789],
    #     'pdf_watermark': {
    #         -1002037268961: FIRST_CHANNELS_WATERMARK,
    #         -1001990321789: SECOND_CHANNELS_WATERMARK
    #     },
    #     'emojis_replacement': DEFAULT_EMOJIS_REPLACEMENT,
    #     'text_remove': DEFAULT_TEXTS_REMOVE,
    #     'send_missed_messages': {
    #         'enable': True,
    #         'count': 10,
    #     }
    # },
    #
    #
    #
    # {
    #     'source': [-1002015899398],
    #     'target': [-1001990941015, -1002088504178],
    #     'pdf_watermark': {
    #         -1001990941015: FIRST_CHANNELS_WATERMARK,
    #         -1002088504178: SECOND_CHANNELS_WATERMARK
    #     },
    #     'emojis_replacement': DEFAULT_EMOJIS_REPLACEMENT,
    #     'text_remove': DEFAULT_TEXTS_REMOVE,
    #     'send_missed_messages': {
    #         'enable': True,
    #         'count': 10,
    #     }
    # },
    #
    #
    #
    # {
    #     'source': [-1002096262333],
    #     'target': [-1002087010315, -1001938907223],
    #     'pdf_watermark': {
    #         -1002087010315: FIRST_CHANNELS_WATERMARK,
    #         -1001938907223: SECOND_CHANNELS_WATERMARK
    #     },
    #     'emojis_replacement': DEFAULT_EMOJIS_REPLACEMENT,
    #     'text_remove': DEFAULT_TEXTS_REMOVE,
    #     'send_missed_messages': {
    #         'enable': True,
    #         'count': 10,
    #     }
    # },
    #
    #
    # {
    #     'source': [-1001902661742],
    #     'target': [-1002035259752, -1002073101732],
    #     'pdf_watermark': {
    #         -1002035259752: FIRST_CHANNELS_WATERMARK,
    #         -1002073101732: SECOND_CHANNELS_WATERMARK
    #     },
    #     'emojis_replacement': DEFAULT_EMOJIS_REPLACEMENT,
    #     'text_remove': DEFAULT_TEXTS_REMOVE,
    #     'send_missed_messages': {
    #         'enable': True,
    #         'count': 10,
    #     }
    # },
    #
    #
    #
    # {
    #     'source': [-1001875008224],
    #     'target': [-1001850139609, -1002126954655],
    #     'pdf_watermark': {
    #         -1001850139609: FIRST_CHANNELS_WATERMARK,
    #         -1002126954655: SECOND_CHANNELS_WATERMARK
    #     },
    #     'emojis_replacement': DEFAULT_EMOJIS_REPLACEMENT,
    #     'text_remove': DEFAULT_TEXTS_REMOVE,
    #     'send_missed_messages': {
    #         'enable': True,
    #         'count': 10,
    #     }
    # },
    # {
    #     'source': [-1002077332944],
    #     'target': [-1002122994781, -1002068405417],
    #     'pdf_watermark': {
    #         -1002122994781: FIRST_CHANNELS_WATERMARK,
    #         -1002068405417: SECOND_CHANNELS_WATERMARK
    #     },
    #     'emojis_replacement': DEFAULT_EMOJIS_REPLACEMENT,
    #     'text_remove': DEFAULT_TEXTS_REMOVE,
    #     'send_missed_messages': {
    #         'enable': True,
    #         'count': 10,
    #     }
    # }
]
