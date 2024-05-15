def read_int8(buffer: bytes, offset: int = 0) -> int:
    """Deserializes the provided bytes to a signed 8-bit integer.

    This function reads a signed 8-bit integer from the specified byte buffer
    starting at the given offset. The integer is interpreted using little-endian
    byte order.
    """
    return buffer[offset]

def read_int16(buffer: bytes, offset: int = 0) -> int:
    """Deserializes the provided bytes to a signed 16-bit integer.
    
    This function reads a signed 16-bit integer from the specified byte buffer
    starting at the given offset. The integer is interpreted using little-endian
    byte order.
    """
    return buffer[offset] + (buffer[offset + 1] << 8)

def read_int32(buffer: bytes, offset: int = 0) -> int:
    """Deserializes the provided bytes to a signed 32-bit integer.

    This function reads a signed 32-bit integer from the specified byte buffer
    starting at the given offset. The integer is interpreted using little-endian
    byte order.
    """
    return (
        buffer[offset]
        + (buffer[offset + 1] << 8)
        + (buffer[offset + 2] << 16)
        + (buffer[offset + 3] << 24)
    )

def read_uint8(buffer: bytes, offset: int = 0) -> int:
    """Deserializes the provided bytes to a unsigned 8-bit integer.

    This function reads a unsigned 8-bit integer from the specified byte buffer
    starting at the given offset. The integer is interpreted using little-endian
    byte order.
    """
    return read_int8(buffer, offset) & 0xff

def read_uint16(buffer: bytes, offset: int = 0) -> int:
    """Deserializes the provided bytes to a usigned 16-bit integer.
    
    This function reads a unsigned 16-bit integer from the specified byte buffer
    starting at the given offset. The integer is interpreted using little-endian
    byte order.
    """
    return read_int16(buffer, offset) & 0xffff

def read_uint32(buffer: bytes, offset: int = 0) -> int:
    """Deserializes the provided bytes to a unsigned 32-bit integer.

    This function reads a unsigned 32-bit integer from the specified byte buffer
    starting at the given offset. The integer is interpreted using little-endian
    byte order.
    """
    return read_int32(buffer, offset) & 0xffffffff

def write_int8(buffer: bytes, value: int, offset: int = 0) -> bytes:
    """Writes the provided value to the byte buffer as a signed 8-bit integer.

    This function serializes the provided signed 8-bit integer value and writes
    it into the specified byte buffer at the given offset.
    """
    buffer[offset] = value

def write_int16(buffer: bytes, value: int, offset: int = 0) -> bytes:
    """Writes the provided value to the byte buffer as a signed 16-bit integer.

    This function serializes the provided signed 16-bit integer value and writes
    it into the specified byte buffer at the given offset.
    """
    pass

def write_int32(buffer: bytes, value: int, offset: int = 0) -> bytes:
    """Writes the provided value to the byte buffer as a signed 32-bit integer.

    This function serializes the provided signed 32-bit integer value and writes
    it into the specified byte buffer at the given offset.
    """
    pass

def write_uint8(buffer: bytes, value: int, offset: int = 0) -> bytes:
    """Writes the provided value to the byte buffer as a unsigned 8-bit integer.

    This function serializes the provided unsigned 8-bit integer value and writes
    it into the specified byte buffer at the given offset.
    """
    write_int8(value & 0xff)

def write_uint16(buffer: bytes, value: int, offset: int = 0) -> bytes:
    """Writes the provided value to the byte buffer as a unsigned 16-bit integer.

    This function serializes the provided unsigned 16-bit integer value and writes
    it into the specified byte buffer at the given offset.
    """
    write_int16(value & 0xffff)

def write_uint32(buffer: bytes, value: int, offset: int = 0) -> bytes:
    """Writes the provided value to the byte buffer as a unsigned 32-bit integer.

    This function serializes the provided unsigned 32-bit integer value and writes
    it into the specified byte buffer at the given offset.
    """
    write_int32(value & 0xffffff)
