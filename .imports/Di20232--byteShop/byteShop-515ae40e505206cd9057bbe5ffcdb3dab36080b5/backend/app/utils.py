import re
import unicodedata

from sqlalchemy import select
from sqlalchemy.orm import Session


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def unique_slug(db: Session, model, name: str, ignore_id: int | None = None) -> str:
    base = slugify(name)
    slug = base
    counter = 2
    while True:
        stmt = select(model).where(model.slug == slug)
        if ignore_id is not None:
            stmt = stmt.where(model.id != ignore_id)
        if not db.scalar(stmt):
            return slug
        slug = f"{base}-{counter}"
        counter += 1
