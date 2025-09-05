import zlib
def crc32(data):
    return zlib.crc32(data.encode())