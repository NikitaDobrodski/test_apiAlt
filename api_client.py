import requests
import json

class APIClient:
    def __init__(self):
        self.base_url = "https://rdb.altlinux.org/api"

    def get_branch_packages(self, branch):
        url = f"{self.base_url}/export/branch_binary_packages/{branch}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "packages" in data:
                return data["packages"]
            else:
                print("Response does not contain 'packages' field.")
                return None
        else:
            print(f"Failed to fetch packages for branch {branch}. Status code: {response.status_code}")
            return None

    def compare_packages(self, sisyphus_packages, p10_packages):
        comparison_result = {
            "packages_in_p10_not_in_sisyphus": [],
            "packages_in_sisyphus_not_in_p10": [],
            "packages_with_newer_version_in_sisyphus": []
        }

        if isinstance(sisyphus_packages, dict):
            for package in p10_packages:
                if package not in sisyphus_packages:
                    comparison_result["packages_in_p10_not_in_sisyphus"].append(package)
                else:
                    sisyphus_version = sisyphus_packages[package].get("version")
                    p10_version = p10_packages[package].get("version")
                    if sisyphus_version and p10_version and sisyphus_version > p10_version:
                        comparison_result["packages_with_newer_version_in_sisyphus"].append(package)

            for package in sisyphus_packages:
                if package not in p10_packages:
                    comparison_result["packages_in_sisyphus_not_in_p10"].append(package)
        else:
            print("sisyphus_packages is not a dictionary.")

        return comparison_result


