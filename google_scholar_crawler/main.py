import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup


SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID", "worq2P0AAAAJ")


def write_json(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def make_shieldsio_json(label: str, message: str, color: str):
    return {
        "schemaVersion": 1,
        "label": label,
        "message": str(message),
        "color": color
    }


def fetch_google_scholar_stats(scholar_id: str):
    url = f"https://scholar.google.com/citations?user={scholar_id}&hl=en"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    print(f"Requesting: {url}", flush=True)
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    html = response.text

    if "recaptcha" in html.lower() or "unusual traffic" in html.lower():
        raise RuntimeError("Google Scholar returned captcha / unusual traffic page.")

    soup = BeautifulSoup(html, "html.parser")

    name_tag = soup.select_one("#gsc_prf_in")
    name = name_tag.get_text(strip=True) if name_tag else ""

    rows = soup.select("table#gsc_rsb_st tbody tr")

    stats = {}
    for row in rows:
        cells = row.select("td")
        if len(cells) >= 2:
            key = cells[0].get_text(strip=True).lower()
            value_text = cells[1].get_text(strip=True)
            value = int(re.sub(r"[^\d]", "", value_text) or 0)

            if "citation" in key:
                stats["citedby"] = value
            elif "h-index" in key:
                stats["hindex"] = value
            elif "i10-index" in key:
                stats["i10index"] = value

    if not stats:
        raise RuntimeError("Failed to parse Google Scholar statistics table.")

    return {
        "name": name,
        "scholar_id": scholar_id,
        "updated": datetime.now(timezone.utc).isoformat(),
        "citedby": stats.get("citedby", 0),
        "hindex": stats.get("hindex", 0),
        "i10index": stats.get("i10index", 0)
    }


def main():
    output_dir = Path("results")
    output_dir.mkdir(exist_ok=True)

    print(f"Fetching Google Scholar stats for: {SCHOLAR_ID}", flush=True)

    data = fetch_google_scholar_stats(SCHOLAR_ID)

    write_json(output_dir / "gs_data.json", data)

    write_json(
        output_dir / "gs_data_shieldsio.json",
        make_shieldsio_json("Citations", data["citedby"], "green")
    )

    write_json(
        output_dir / "gs_hindex_shieldsio.json",
        make_shieldsio_json("h-index", data["hindex"], "orange")
    )

    write_json(
        output_dir / "gs_i10index_shieldsio.json",
        make_shieldsio_json("i10-index", data["i10index"], "blue")
    )

    print("Google Scholar data updated successfully.", flush=True)
    print(json.dumps(data, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
