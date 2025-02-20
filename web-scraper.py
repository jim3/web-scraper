# =========================================
# Phone & Email Scraper
# =========================================
import sys
import pyperclip
import re
import requests


def phoneScraper(content):
    try:
        phoneRegex = re.compile(r"\d{3}-\d{3}-\d{4}")
        return phoneRegex.findall(content), None
    except (re.error, AttributeError) as e:
        return [], f"phone scraper error: {str(e)}"


def emailScraper(content):
    try:
        emailRegex = re.compile(r"[\w]+@[\w]+\.[\w]+")
        return emailRegex.findall(content), None
    except (re.error, AttributeError) as e:
        return [], f"email scraper error: {str(e)}"


def main():
    if len(sys.argv) < 2:
        print("Usage: " + sys.argv[0] + " <url>")
        sys.exit(1)
    url = sys.argv[1]
    try:
        # make a GET request with the argument as the URL
        r = requests.get(url)
        if r.status_code == 200:
            # read in the entire body
            body = r.text
            # copy the body to the clipboard
            pyperclip.copy(body)
        else:
            print(f"Error: {r.status_code}")
        # Read from clipboard to variable of type string
        content = pyperclip.paste()
        if not content or content.isspace():
            print("Error: Clipboard is empty")
            return
    except pyperclip.PyperclipException as e:
        print(f"clipboard error: {str(e)}")
        return
    # Get phone numbers
    phones, err = phoneScraper(content)
    if err:
        print(err)
        return
    # Get email addresses
    emails, err = emailScraper(content)
    if err:
        print(err)
        return
    if not phones and not emails:
        print("No phone numbers or email addresses found in clipboard")
        return
    # Print results
    print(f"Found phones: {phones}")
    print(f"Found emails: {emails}")


if __name__ == "__main__":
    main()
