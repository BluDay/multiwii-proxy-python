def read_int8(buffer: bytes, offset: int = 0) -> int:
    """Deserializes the provided bytes to a signed 8-bit integer."""
    return buffer[offset]

def read_int16(buffer: bytes, offset: int = 0) -> int:
    """Deserializes the provided bytes to a signed 16-bit integer."""
    return buffer[offset] + (buffer[offset + 1] << 8)

def read_int32(buffer: bytes, offset: int = 0) -> int:
    """Deserializes the provided bytes to a signed 32-bit integer."""
    return (
        buffer[offset]
        + (buffer[offset + 1] << 8)
        + (buffer[offset + 2] << 16)
        + (buffer[offset + 3] << 24)
    )

def read_uint8(buffer: bytes, offset: int = 0) -> int:
    """Deserializes the provided bytes to a unsigned 8-bit integer."""
    return read_int8(buffer, offset) & 0xff

def read_uint16(buffer: bytes, offset: int = 0) -> int:
    """Deserializes the provided bytes to a signed 16-bit integer."""
    return read_int16(buffer, offset) & 0xffff

def read_uint32(buffer: bytes, offset: int = 0) -> int:
    """Deserializes the provided bytes to a signed 32-bit integer."""
    return read_int16(buffer, offset) & 0xffffffff

def write_int8(buffer: bytes, offset: int = 0) -> bytes:
    """Serializes the provided bytes to a signed 8-bit integer."""
    pass

def write_int16(buffer: bytes, offset: int = 0) -> bytes:
    """Serializes the provided bytes to a signed 16-bit integer."""
    pass

def write_int32(buffer: bytes, offset: int = 0) -> bytes:
    """Serializes the provided bytes to a signed 32-bit integer."""
    pass

def write_uint8(buffer: bytes, offset: int = 0) -> bytes:
    """Serializes the provided bytes to a unsigned 8-bit integer."""
    pass

def write_uint16(buffer: bytes, offset: int = 0) -> bytes:
    """Serializes the provided bytes to a signed 16-bit integer."""
    pass

def write_uint32(buffer: bytes, offset: int = 0) -> bytes:
    """Serializes the provided bytes to a signed 32-bit integer."""
    pass
