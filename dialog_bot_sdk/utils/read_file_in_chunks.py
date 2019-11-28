def read_file_in_chunks(file, chunk_size=1024*1024):
    """File chunks generator

    :param file: path to file
    :param chunk_size: size of a chunk
    :return: generator object that iterates over file chunks
    """

    file_object = open(file, 'rb')
    while True:
        data = file_object.read(chunk_size)
        if not data:
            file_object.close()
            break
        yield data
