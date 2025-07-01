# ThreadSlayer
A tool for defanging and anonymizing Hacking Forum PDF dumps that serves the following purposes:

1. Defang URLs in the PDF.
2. Anonymize via redacting user account information, e.g. user name, user id, etc.
3. Redact date/time timestamps from the PDF applied by browsers when saving as PDF.

## Usage

1. Save a hacking forum thread as PDF via web browser.
2. Pass the PDF or a directory containing PDFs to ThreadSlayer.

```
usage: ThreadSlayer.py [-h] [-f FILE] [-d DIRECTORY]

options:
  -h, --help            show this help message and exit
  -f, --file FILE
```
