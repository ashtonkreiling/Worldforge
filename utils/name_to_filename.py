import unicodedata

def to_filename(name: str) -> str:
    # Normalize unicode (é → e, — → -)
    name = unicodedata.normalize("NFKD", name)
    name = name.encode("ascii", "ignore").decode("ascii")

    result = []
    prev_underscore = False

    for ch in name.lower():
        if ch.isalnum():
            result.append(ch)
            prev_underscore = False
        else:
            # Convert any non-alphanumeric run into a single underscore
            if not prev_underscore:
                result.append("_")
                prev_underscore = True

    # Join and trim leading/trailing underscores
    return "".join(result).strip("_")