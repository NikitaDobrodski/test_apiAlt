#!/usr/bin/env python3

import argparse
import json
from api_client import APIClient

def main():
    parser = argparse.ArgumentParser(description="Compare binary packages between sisyphus and p10 branches.")
    parser.add_argument("branch", choices=["sisyphus", "p10"], help="Branch to compare packages from")
    args = parser.parse_args()

    client = APIClient()
    branch_packages = client.get_branch_packages(args.branch)

    if branch_packages:
        other_branch = "sisyphus" if args.branch == "p10" else "p10"
        other_branch_packages = client.get_branch_packages(other_branch)

        if other_branch_packages:
            comparison_result = client.compare_packages(branch_packages, other_branch_packages)
            print("Comparison Result:")
            print(json.dumps(comparison_result, indent=4))
            print("Comparison completed successfully.")
        else:
            print(f"Failed to fetch packages for branch {other_branch}.")
    else:
        print(f"Failed to fetch packages for branch {args.branch}.")

if __name__ == "__main__":
    main()


