# =========================================
# Phone & Email Scraper
# =========================================
import sys
import pyperclip
import re
import requests


def phoneScraper(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            body = r.text
            pyperclip.copy(body)
        else:
            print(f"Error: {r.status_code}")
        content = pyperclip.paste()
        if not content or content.isspace():
            print("Error: Clipboard is empty")
            return
    except pyperclip.PyperclipException as e:
        print(f"clipboard error: {str(e)}")
        return
    phoneRegex = re.compile(r"\d{3}-\d{3}-\d{4}")
    phoneNumbers = phoneRegex.findall(content)
    return phoneNumbers, None


def emailScraper(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            body = r.text
            pyperclip.copy(body)
        else:
            print(f"Error: {r.status_code}")
        content = pyperclip.paste()
        if not content or content.isspace():
            print("Error: Clipboard is empty")
            return
    except pyperclip.PyperclipException as e:
        print(f"clipboard error: {str(e)}")
        return
    emailRegex = re.compile(r"[\w]+@[\w]+\.[\w]+")
    emailAddresses = emailRegex.findall(content)
    return emailAddresses, None


def main():
    if len(sys.argv) < 2:
        print("Usage: " + sys.argv[0] + " <url>")
        sys.exit(1)
    url = sys.argv[1]
    phones, err = phoneScraper(url)
    if err:
        print(err)
        return
    emails, err = emailScraper(url)
    if err:
        print(err)
        return
    print(f"Found phones: {phones}")
    print(f"Found emails: {emails}")


if __name__ == "__main__":
    main()
