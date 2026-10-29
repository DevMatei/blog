import shutil
import sys
from datetime import date, datetime, timezone
from email.utils import format_datetime
from pathlib import Path

import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parent
POSTS_DIR = ROOT / "posts"
TEMPLATES_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"
DIST_DIR = ROOT / "dist"

WORDS_PER_MINUTE = 200
REQUIRED_FIELDS = ("title", "date", "description")
DATE_FORMATS = ("%Y-%m-%d", "%B %d, %Y", "%b %d, %Y")

MD_EXTENSIONS = ["fenced_code", "tables", "toc"]
MD_CONFIG = {"toc": {"baselevel": 2}}


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def parse_date(value):
    if isinstance(value, datetime):
        parsed = value
    elif isinstance(value, date):
        parsed = datetime(value.year, value.month, value.day)
    else:
        text = str(value).strip()
        parsed = None
        for fmt in DATE_FORMATS:
            try:
                parsed = datetime.strptime(text, fmt)
                break
            except ValueError:
                continue
        if parsed is None:
            raise ValueError(f"can't read the date {text!r}, use 2026-08-30")
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def load_posts():
    posts = []
    for path in sorted(POSTS_DIR.glob("*.md")):
        source = frontmatter.load(path)
        meta = source.metadata

        if meta.get("draft"):
            print(f"skipping draft: {path.name}")
            continue

        missing = [field for field in REQUIRED_FIELDS if not meta.get(field)]
        if missing:
            fail(f"{path.name} is missing frontmatter: {', '.join(missing)}")

        try:
            published = parse_date(meta["date"])
        except ValueError as err:
            fail(f"{path.name}: {err}")

        tags = meta.get("tags") or []
        if isinstance(tags, str):
            tags = [tag.strip() for tag in tags.split(",") if tag.strip()]

        words = len(source.content.split())

        posts.append(
            {
                "slug": path.stem,
                "title": str(meta["title"]),
                "description": str(meta["description"]),
                "tags": [str(tag) for tag in tags],
                "body": markdown.markdown(
                    source.content,
                    extensions=MD_EXTENSIONS,
                    extension_configs=MD_CONFIG,
                ),
                "read_time": max(1, round(words / WORDS_PER_MINUTE)),
                "date": published,
                "date_iso": published.date().isoformat(),
                "date_display": f"{published.strftime('%b').lower()} {published.day}, {published.year}",
                "date_rfc822": format_datetime(published),
            }
        )

    posts.sort(key=lambda post: post["date"], reverse=True)  # newest first
    return posts


def write(path, html):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


def main():
    if not POSTS_DIR.is_dir():
        fail(f"no posts folder at {POSTS_DIR}")

    posts = load_posts()
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), autoescape=True)

    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir()
    if STATIC_DIR.is_dir():
        shutil.copytree(STATIC_DIR, DIST_DIR, dirs_exist_ok=True)

    post_template = env.get_template("post.html")
    for i, post in enumerate(posts):
        newer = posts[i - 1] if i > 0 else None
        older = posts[i + 1] if i < len(posts) - 1 else None
        html = post_template.render(post=post, older=older, newer=newer)
        write(DIST_DIR / "blog" / f"{post['slug']}.html", html)

    write(DIST_DIR / "index.html", env.get_template("index.html").render(posts=posts))
    write(DIST_DIR / "rss.xml", env.get_template("rss.xml").render(posts=posts))

    print(f"built {len(posts)} posts into {DIST_DIR}")


if __name__ == "__main__":
    main()