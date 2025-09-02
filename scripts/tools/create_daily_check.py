# scripts/tools/create_daily_check.py
import os
import sys
import json
import argparse
from datetime import datetime, date
from zoneinfo import ZoneInfo
import urllib.request

GITHUB_API = "https://api.github.com"

TEMPLATE = """**오늘 배운 것(1-3줄):**
- 

**막힌 점(Blocker):**
- 

**내일 할 일(To-do):**
- 
"""

DEFAULT_LABELS = ["daily", "log"]

def gh_request(method: str, url: str, token: str, data: dict | None = None):
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        req.add_header("Content-Type", "application/json")
    else:
        body = None
    with urllib.request.urlopen(req, body) as resp:
        return json.loads(resp.read().decode("utf-8")) if resp.status != 204 else None

def ensure_labels(owner_repo: str, token: str, labels: list[str]):
    # Create labels if missing (idempotent-ish)
    owner, repo = owner_repo.split("/", 1)
    # get existing labels (paginated minimal)
    existing = set()
    page = 1
    while True:
        url = f"{GITHUB_API}/repos/{owner}/{repo}/labels?per_page=100&page={page}"
        res = gh_request("GET", url, token)
        if not res:
            break
        for lab in res:
            existing.add(lab["name"])
        if len(res) < 100:
            break
        page += 1

    for name in labels:
        if name in existing:
            continue
        payload = {"name": name, "color": "ededed", "description": "Auto-CVS daily log"}
        url = f"{GITHUB_API}/repos/{owner}/{repo}/labels"
        gh_request("POST", url, token, payload)

def create_issue(owner_repo: str, token: str, title: str, body: str, labels: list[str], assignees: list[str] | None):
    owner, repo = owner_repo.split("/", 1)
    url = f"{GITHUB_API}/repos/{owner}/{repo}/issues"
    payload = {
        "title": title,
        "body": body,
        "labels": labels,
    }
    if assignees:
        payload["assignees"] = assignees
    return gh_request("POST", url, token, payload)

def main():
    parser = argparse.ArgumentParser(description="Create a [Daily Check] issue in GitHub.")
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPO"), help="owner/repo (e.g., jhun5568/Auto-CVS-Project)")
    parser.add_argument("--token", default=os.environ.get("GITHUB_TOKEN"), help="GitHub token with repo scope")
    parser.add_argument("--date", help="YYYY-MM-DD (default: today in Asia/Seoul)")
    parser.add_argument("--title-prefix", default="[Daily Check]", help="Title prefix")
    parser.add_argument("--labels", nargs="*", default=DEFAULT_LABELS, help="Labels to attach")
    parser.add_argument("--assignees", nargs="*", default=None, help="GitHub usernames to assign")
    parser.add_argument("--no-create-labels", action="store_true", help="Do not auto-create missing labels")
    args = parser.parse_args()

    if not args.repo or not args.token:
        print("ERROR: --repo and --token (or env GITHUB_REPO/GITHUB_TOKEN) are required.", file=sys.stderr)
        sys.exit(1)

    # Date in Asia/Seoul
    if args.date:
        try:
            d = date.fromisoformat(args.date)
        except ValueError:
            print("ERROR: --date must be YYYY-MM-DD", file=sys.stderr)
            sys.exit(1)
    else:
        d = datetime.now(ZoneInfo("Asia/Seoul")).date()

    title = f"{args.title_prefix} {d.isoformat()}"

    # Body template
    body = TEMPLATE

    # Ensure labels
    if not args.no_create_labels:
        ensure_labels(args.repo, args.token, args.labels)

    issue = create_issue(args.repo, args.token, title, body, args.labels, args.assignees)
    url = issue.get("html_url", "")
    number = issue.get("number", "")
    print(f"✅ Created issue #{number}: {url}")

if __name__ == "__main__":
    main()
