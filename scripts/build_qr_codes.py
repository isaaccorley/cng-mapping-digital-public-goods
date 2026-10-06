# /// script
# requires-python = ">=3.11"
# dependencies = ["qrcode[pil]==8.2"]
# ///
"""Build the checked-in QR images with `uv run scripts/build_qr_codes.py`."""

import json
from pathlib import Path

import qrcode

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    """Encode the direct project URLs with a four-module quiet zone."""
    output = ROOT / "assets" / "qr"
    output.mkdir(exist_ok=True)
    for project in json.loads((ROOT / "assets" / "project-links.json").read_text()):
        code = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=12,
            border=4,
        )
        code.add_data(project["url"])
        code.make(fit=True)
        code.make_image(fill_color="#3b1e1c", back_color="white").save(
            output / f"{project['id']}.png"
        )


if __name__ == "__main__":
    main()
