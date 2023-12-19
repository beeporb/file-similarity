# file-similarity
Experimenting with SSDeep, TLSH hashing, and other distance metrics alongside Neo4J.

# The goal

Write some scripts that generate different signatures for files, and compare different generated signatures against each other using distance metrics. Examples include SSDeep hashes, TLSH hashes, and tokenised file content.

Store the file metadata in something like Elasticsearch, and store the distances between files on the edges of a graph in Neo4J.

See if anything cool can be done from doing this!