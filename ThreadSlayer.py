"""
Title: ThreadSlayer
Author: YungBinary
Description: Sanitize the contents of PDF files extracted
    from OSINT or closed source hacking forum threads.
Key Features:
    1. Defang embedded URLs
    2. Redact user identifiers, or other sensitive info.
"""
import argparse
import re
import os

try:
    import pymupdf
except ImportError:
    raise ImportError("Please run the following command: pip3 install pymupdf")

# Regex formatted user name, user id, or other sensitive info
# to redact from the output PDF
REDACT_LIST = [
    r"johnsmith"
]

def sanitize_pdf(input_pdf_path):
    doc = pymupdf.open(input_pdf_path)

    url_pattern = re.compile(
        r'http[s]*://',
        re.IGNORECASE
    )

    date_time_pattern = re.compile(
        r'\d{1,2}\/\d{1,2}\/\d{2},\s\d{1,2}:\d{2}\s(?:AM|PM)',
        re.IGNORECASE
    )

    username_pattern = re.compile(
        '|'.join(REDACT_LIST),
        re.IGNORECASE
    )

    patterns = [
        url_pattern,
        date_time_pattern,
        username_pattern
    ]

    # Iterate over each page of the document
    for page in doc:
        for link in page.links():
            if 'uri' not in link:
                continue

            redact_link = False
            for redact_pattern in REDACT_LIST:
                if redact_pattern in link['uri']:
                    redact_link = True
                    break
            if redact_link:
                page.add_redact_annot(link['from'])
            else:
                link['uri'] = link['uri'].replace('http', "hxxp").replace('mailto:', 'dontmailto:')
                page.delete_link(link)
                page.insert_link(link)


        page_text = page.get_text("text")
        for pattern in patterns:
            matches = pattern.finditer(page_text)
            for match in matches:
                matched_text = match.group(0)
                text_rects = page.search_for(matched_text)
                for rect in text_rects:
                    page.add_redact_annot(rect)

        page.apply_redactions()


    doc.save(input_pdf_path + "_temp", garbage=4, incremental=False)
    doc.close()
    os.replace(input_pdf_path + "_temp", input_pdf_path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file')
    parser.add_argument('-d', '--directory')
    args = parser.parse_args()

    if not args.file and not args.directory:
        parser.error("At least one of --file or --directory is required.")
    
    if args.file:
        sanitize_pdf(args.file)
        print(f"Finished sanitizing '{args.file}'")
    elif args.directory:
        for subdir, dirs, filenames in os.walk(args.directory):
            for filename in filenames:
                if filename.lower().endswith('.pdf'):
                    file_path = os.path.join(subdir, filename)
                    print(f"Sanitizing '{file_path}'")
                    sanitize_pdf(file_path)
                    print(f"Finished sanitizing '{file_path}'")

if __name__ == "__main__":
    main()