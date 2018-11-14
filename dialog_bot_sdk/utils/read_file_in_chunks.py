def read_file_in_chunks(file, chunk_size=1024*1024):
    file_object = open(file)
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data
