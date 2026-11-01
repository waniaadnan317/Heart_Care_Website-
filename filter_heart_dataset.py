
import os
import csv
import xml.etree.ElementTree as ET

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))

XML_FILE = os.path.join(
    BASE_FOLDER,
    "mplus_topics_2026-10-24.xml"
)

OUTPUT_FILE = os.path.join(
    BASE_FOLDER,
    "heart_medical_qa.csv"
)

HEART_TERMS = [
    "heart", "cardiac", "cardiovascular",
    "coronary", "arrhythmia", "atrial fibrillation",
    "heart valve", "myocardial", "angina",
    "pericarditis", "endocarditis", "myocarditis",
    "cardiomyopathy", "aortic stenosis",
    "blood pressure", "heart failure",
    "heart attack", "congenital heart"
]

def clean_text(element):
    if element is None:
        return ""
    return " ".join("".join(element.itertext()).split())

def main():
    if not os.path.isfile(XML_FILE):
        print("ERROR: XML file not found:", XML_FILE)
        return

    records = []
    seen = set()

    print("Reading MedlinePlus XML...")

    try:
        root = ET.parse(XML_FILE).getroot()
    except (ET.ParseError, OSError) as error:
        print("Could not read XML:", error)
        return

    for topic in root.iter():
        if not topic.tag.lower().endswith("healthtopic"):
            continue

        title = clean_text(topic.find("title"))
        url = clean_text(topic.find("url"))
        summary = clean_text(topic.find("fullsummary"))

        if not title or not summary:
            continue

        text_to_check = (title + " " + url).casefold()

        if not any(term in text_to_check for term in HEART_TERMS):
            continue

        key = (title.casefold(), summary.casefold())
        if key in seen:
            continue
        seen.add(key)

        records.append({
            "topic": title,
            "question": "What is " + title + "?",
            "answer": summary,
            "source": "MedlinePlus",
            "source_url": url
        })

    with open(
        OUTPUT_FILE, "w", newline="", encoding="utf-8-sig"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "topic", "question", "answer",
                "source", "source_url"
            ]
        )
        writer.writeheader()
        writer.writerows(records)

    print("Heart-related topic records:", len(records))
    print("CSV saved at:", OUTPUT_FILE)
    print("Note: These are topic summaries, not original Q&A pairs.")

if __name__ == "__main__":
    main()
