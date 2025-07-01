# ThreadSlayer
A tool for defanging and anonymizing Hacking Forum PDF dumps that serves the following purposes:

1. Defang URLs in the PDF.
2. Anonymize via redacting user account information, e.g. user name, user id, etc.
3. Redact date/time timestamps from the PDF applied by browsers when saving as PDF.

## Usage

1. Save a hacking forum thread as PDF via web browser print dialog, for example:

![SAVE AS PDF HOW TO](https://github.com/user-attachments/assets/38afc575-e0a7-4385-8aa6-7b3bb33a47fb)

2. Edit ThreadSlayer.py with any usernames, user ids, or other information you want to redact, otherwise the output PDF could expose your account info on the hacking forum.
2. Pass the PDF or a directory containing PDFs to ThreadSlayer. Note, the PDF will be overwritten, so you may want to make backups!

```
usage: ThreadSlayer.py [-h] [-f FILE] [-d DIRECTORY]

options:
  -h, --help            show this help message and exit
  -f, --file FILE
```
