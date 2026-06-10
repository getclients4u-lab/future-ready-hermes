import base64
import json
from datetime import datetime
from typing import Any
import httpx

from app.config import settings


class GitHubStorage:
    """GitHub-backed storage layer for project artifacts, reports, and backups."""

    def __init__(self, token: str = None, repo: str = None):
        self.token = token or settings.github_token
        self.repo = repo or settings.github_repo
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "future-ready-hermes",
        }

    async def _request(self, method: str, path: str, data: dict = None) -> dict:
        url = f"{self.base_url}/repos/{self.repo}/contents/{path}"
        async with httpx.AsyncClient() as client:
            if method == "GET":
                resp = await client.get(url, headers=self.headers)
            elif method == "PUT":
                resp = await client.put(url, headers=self.headers, json=data)
            else:
                raise ValueError(f"Unsupported method: {method}")
            resp.raise_for_status()
            return resp.json()

    async def read_file(self, path: str, branch: str = "main") -> str:
        """Read a file from the repository. Returns decoded content."""
        data = await self._request("GET", f"{path}?ref={branch}")
        if "content" in data:
            return base64.b64decode(data["content"]).decode("utf-8")
        return ""

    async def write_file(
        self, path: str, content: str, message: str = None, branch: str = "main"
    ) -> dict:
        """Write or update a file in the repository."""
        encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")
        message = message or f"Update {path} via FutureReady API"

        # Try to get existing SHA for update
        try:
            existing = await self._request("GET", f"{path}?ref={branch}")
            sha = existing.get("sha")
        except Exception:
            sha = None

        payload = {
            "message": message,
            "content": encoded,
            "branch": branch,
        }
        if sha:
            payload["sha"] = sha

        return await self._request("PUT", path, payload)

    async def save_json(self, path: str, data: Any, message: str = None) -> dict:
        """Save a JSON-serializable object to a file."""
        content = json.dumps(data, indent=2, default=str)
        return await self.write_file(path, content, message)

    async def read_json(self, path: str, branch: str = "main") -> Any:
        """Read and parse a JSON file."""
        raw = await self.read_file(path, branch)
        return json.loads(raw)

    async def append_csv(self, path: str, row: dict, headers: list[str] = None) -> dict:
        """Append a row to a CSV file (creates if not exists)."""
        try:
            existing = await self.read_file(path)
        except Exception:
            existing = ""

        if not existing and headers:
            lines = [
                ",".join(headers),
                ",".join(str(row.get(h, "")) for h in headers),
            ]
        elif existing:
            lines = existing.strip().split("\n")
            if headers:
                lines.append(",".join(str(row.get(h, "")) for h in headers))
            else:
                lines.append(",".join(str(v) for v in row.values()))
        else:
            lines = [",".join(str(v) for v in row.values())]

        content = "\n".join(lines) + "\n"
        return await self.write_file(path, content, message=f"Append to {path}")
