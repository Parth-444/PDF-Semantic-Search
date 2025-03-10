text = "and he went on to kill the whole fucking village, god was with him so that he was able to escape alive"
def chunk_by_words(texts,  chunk_size=5, overlap=2):
    words = texts.split()
    chunks=[]
    start = 0

    while start< len(words):
        end = min(start + chunk_size, len(words))
        chunk = ' '.join(words[start:end])
        chunks.append(chunk)
        # start = end-overlap
        if start<0:
            start=0
        new_start = end-overlap
        if new_start==start:
            break
        else:
            start=new_start

    return chunks

print(chunk_by_words(text))