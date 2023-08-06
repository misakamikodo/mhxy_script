from mhxy import *

try:
    import pytesseract
except ImportError:
    pass


def ocr(region, type=None):
    # 识别汉字
    img = pyautogui.screenshot(
        region=(winRelativeX(region[0]), winRelativeY(region[1]), winRelativeX(region[2]), winRelativeY(region[3])))
    # 只检测数字
    config = None
    # 中文
    lang = 'chi_sim'
    if type == 'number':
        config = r'-c tessedit_char_whitelist=0123456789 --psm 6'
    elif type == "eng":
        lang = 'eng'
    text = pytesseract.image_to_string(img, lang=lang, config=config)
    return text
