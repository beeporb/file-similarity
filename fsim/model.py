"""Contains the model for data to be included in Elasticsearch."""

class File:
    attrib_mime_type: str
    attrib_size_bytes: int
    attrib_shannon_entropy: float
    hash_md5: str
    hash_sha1: str
    hash_sha256: str
    hash_ssdeep: str
    content_unique_strings: list[str]
    metadata_filename: str