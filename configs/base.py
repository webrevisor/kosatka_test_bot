from os.path import dirname, abspath

# Path
ROOT_PATH = dirname(dirname(abspath(__file__)))
STORAGE_PATH = ROOT_PATH + '/storage'
DOWNLOAD_PATH = STORAGE_PATH + '/downloads'

# PDF
PDF_DPI = 230
PDF_INSANE_WATERMARK = {
    'path': STORAGE_PATH + '/watermarks/insane.png',
    'scale': 0.32,
    'angle': 0,
    'opacity': 0.59,
}
PDF_INBLACK_WATERMARK = {
    'path': STORAGE_PATH + '/watermarks/inblack.png',
    'scale': 0.93,
    'angle': 45,
    'opacity': 0.21,
}

SYNC_MESSAGES_COUNT = 50
