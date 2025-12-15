
# src/redaction.py
import re

def redact(text: str) -> str:
    # Replace model numbers, vendor names with placeholders
    text = re.sub(r"Vendor[A-Za-z0-9]+", "VendorX", text)
    text = re.sub(r"[A-Z]{2,}-\d{3,}", "MODEL-XXX", text)
    return text
