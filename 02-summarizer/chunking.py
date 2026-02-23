from nltk.tokenize import sent_tokenize

def sentence_based_chunking(
    text: str,
    max_chars: int = 1500,
    overlap_sentence: int = 1
) -> list[str]:
    
        

    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []

    for sentence in sentences:
        current_chunk.append(sentence)
        chunk_text = " ".join(current_chunk)

        if len(chunk_text) >= max_chars:
            chunks.append(chunk_text)

            # keep last N sentences for overlap
            current_chunk = current_chunk[-overlap_sentence:]

    # add remaining sentences as final chunk
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
