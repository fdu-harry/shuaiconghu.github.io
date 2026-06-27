from scholarly import scholarly
import json
import os
from datetime import datetime, timezone
from pathlib import Path


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


def main():
    output_dir = Path("results")
    output_dir.mkdir(exist_ok=True)

    print(f"Fetching Google Scholar data for: {SCHOLAR_ID}")

    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(
        author,
        sections=["basics", "indices", "counts", "publications"]
    )

    publications = []
    for pub in author.get("publications", []):
        bib = pub.get("bib", {})
        publications.append({
            "title": bib.get("title", ""),
            "year": bib.get("pub_year", ""),
            "venue": bib.get("venue", ""),
            "num_citations": pub.get("num_citations", 0),
            "author_pub_id": pub.get("author_pub_id", "")
        })

    data = {
        "name": author.get("name", ""),
        "scholar_id": SCHOLAR_ID,
        "updated": datetime.now(timezone.utc).isoformat(),
        "citedby": author.get("citedby", 0),
        "hindex": author.get("hindex", 0),
        "i10index": author.get("i10index", 0),
        "citedby5y": author.get("citedby5y", 0),
        "hindex5y": author.get("hindex5y", 0),
        "i10index5y": author.get("i10index5y", 0),
        "publications": publications
    }

    write_json(output_dir / "gs_data.json", data)

    write_json(
        output_dir / "gs_data_shieldsio.json",
        make_shieldsio_json("citations", data["citedby"], "green")
    )

    write_json(
        output_dir / "gs_hindex_shieldsio.json",
        make_shieldsio_json("h-index", data["hindex"], "orange")
    )

    write_json(
        output_dir / "gs_i10index_shieldsio.json",
        make_shieldsio_json("i10-index", data["i10index"], "blue")
    )

    print("Google Scholar data updated successfully.")
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
