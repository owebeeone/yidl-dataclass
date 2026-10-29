"""Keep repository links useful without publishing implementation or dev records."""

from pathlib import Path
import re
from urllib.parse import quote, urlsplit

LINK = re.compile(r"(!?\[[^\]]*\]\()([^\s)]+)(\))")


def on_page_markdown(markdown, *, page, config, **kwargs):
    docs = Path(config.docs_dir).resolve()
    repository = docs.parent

    def rewrite(match):
        prefix, target, suffix = match.groups()
        url = urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            return match.group(0)
        destination = (Path(page.file.abs_src_path).parent / url.path).resolve()
        if destination.is_relative_to(docs):
            return match.group(0)
        if not destination.is_relative_to(repository) or not destination.is_file():
            raise ValueError(f"Invalid repository link: {page.file.src_uri}: {target}")
        relative = destination.relative_to(repository).as_posix()
        link = config.repo_url.rstrip("/") + "/blob/main/" + quote(relative)
        if url.fragment:
            link += "#" + url.fragment
        return prefix + link + suffix

    return LINK.sub(rewrite, markdown)
