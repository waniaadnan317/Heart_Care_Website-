
import os
import csv
import xml.etree.ElementTree as ET

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))

XML_FOLDER = (
    r"C:\Users\SM Computer\Downloads"
    r"\MedQuAD-master\8_NHLBI_QA_XML"
)

OUTPUT_FILE = os.path.join(
    BASE_FOLDER, "medquad_heart_qa.csv"
)

def get_text(parent, tag):
    element = parent.find(tag)
    if element is None:
        return ""
    return " ".join("".join(element.itertext()).split())

def main():
    if not os.path.isdir(XML_FOLDER):
        print("ERROR: MedQuAD folder not found.")
        return

    records = []
    seen = set()

    for filename in os.listdir(XML_FOLDER):
        if not filename.lower().endswith(".xml"):
            continue

        path = os.path.join(XML_FOLDER, filename)

        try:
            root = ET.parse(path).getroot()
        except (ET.ParseError, OSError):
            continue

        for pair in root.findall(".//QAPair"):
            question = get_text(pair, "Question")
            answer = get_text(pair, "Answer")

            if not question or not answer:
                continue

            key = (question.casefold(), answer.casefold())
            if key in seen:
                continue

            seen.add(key)
            records.append({
                "question": question,
                "answer": answer,
                "source": "MedQuAD"
            })

    with open(
        OUTPUT_FILE, "w", newline="", encoding="utf-8-sig"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["question", "answer", "source"]
        )
        writer.writeheader()
        writer.writerows(records)

    print("MedQuAD records saved:", len(records))
    print("CSV location:", OUTPUT_FILE)

if __name__ == "__main__":
    main()
