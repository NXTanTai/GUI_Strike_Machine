import json
from pathlib import Path

_TRANSLATIONS: dict[str, dict[str, str]] = {}
_TRANS_CACHE_FILE = Path(__file__).parent / "translations_cache.json"

def _load_translation_cache():
    global _TRANSLATIONS
    if _TRANS_CACHE_FILE.exists():
        try:
            _TRANSLATIONS = json.loads(_TRANS_CACHE_FILE.read_text(encoding="utf-8"))
        except Exception:
            _TRANSLATIONS = {}

def _save_translation_cache():
    try:
        _TRANS_CACHE_FILE.write_text(
            json.dumps(_TRANSLATIONS, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
    except Exception:
        pass

def tr(self, text: str) -> str:
    if self._current_lang == "en":
        return text

    cached = _TRANSLATIONS.get(text, {}).get(self._current_lang)
    if cached:
        return cached

    try:
        import urllib.request, json as _json
        payload = _json.dumps({
            "model": "claude-haiku-4-5-20251001",
            "max_tokens": 100,
            "messages": [{
                "role": "user",
                "content": (
                    f"Translate this UI text to {'Chinese' if self._current_lang == 'cn' else self._current_lang}. "
                    f"Return ONLY the translated text, nothing else:\n{text}"
                )
            }]
        }).encode()

        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=payload,
            headers={
                "Content-Type": "application/json",
                "x-api-key": "YOUR_API_KEY",
                "anthropic-version": "2023-06-01"
            }
        )
        with urllib.request.urlopen(req, timeout=3) as resp:
            result = _json.loads(resp.read())
            translated = result["content"][0]["text"].strip()
    except Exception:
        translated = text

    if text not in _TRANSLATIONS:
        _TRANSLATIONS[text] = {}
    _TRANSLATIONS[text][self._current_lang] = translated
    _save_translation_cache()
    return translated