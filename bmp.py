"""A module for dealing with BMP bitmap image files."""

def write_grayscale(filename, pixels):
    """Creates and writes a grayscale BMP file.

    Args:
        filename: The name of the BMP file to me created.

        pixels: A rectangular image stored as a sequence of rows.
            Each row must be an iterable series of integer in the
            range 0-255.

    Raises:
        OSError: If the file couldn't be written.
    """

    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        # BMP Header
        bmp.write(b'BM')

        size_bookmark = bmp.tell()      # Return the file's current position
        bmp.write(b'\x00\x00\x00\x00')      # Little-endian integer.

        bmp.write(b'\x00\x00')
        bmp.write(b'\x00\x00')

        pixel_offset_bookmark = bmp.tell()
        bmp.write(b'\x00\x00\x00\x00')

        # Image Header
        bmp.write(b'\x28\x00\x00\x00')
        bmp.write(_int32_to_bytes(width)) 
        bmp.write(_int32_to_bytes(height))
        bmp.write(b'\x01\x00')
        bmp.write(b'\x08\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')

        # Color palette - a linear grayscale
        for c in range(256):
            bmp.write(bytes((c, c, c, 0))) # Blue, Green, Red, Zero
            
        # Pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):
            row_data = bytes(row)
            bmp.write(row_data)
            padding = b'\x00' * (4 - (len(row) % 4 ))
            bmp.write(padding)

        # End of file
        eof_bookmark = bmp.tell()

        # Fill in file size placeholder
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        # Fill in pixel offset placeholder
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))

def _int32_to_bytes(i):
    """Convert an integer to four bytes in little-endian format."""
    return bytes((i & 0xff,
                  i >> 8 & 0xff,
                  i >> 16 & 0xff,
                  i >> 24 & 0xff))




