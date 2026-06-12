from PySide6.QtCore import QThread, Signal
from deep_translator import GoogleTranslator

class TranslateWorker(QThread):
    result = Signal(str)
    error  = Signal(str)

    def __init__(self, text, target="vi"):
        super().__init__()
        self.text = text
        self.target = target

    def run(self):
        try:
            translated = GoogleTranslator(
                source="auto",
                target=self.target
            ).translate(self.text)
            self.result.emit(translated)
        except Exception as e:
            self.error.emit(str(e))