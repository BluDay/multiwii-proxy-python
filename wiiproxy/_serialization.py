from typing import NoReturn

def _write_int8(buffer: bytes, value: int, offset: int) -> NoReturn:
    """Writes the provided integer to the byte buffer as an 8-bit value."""
    buffer[offset] = value & 0xff

def _write_int16(buffer: bytes, value: int, offset: int) -> NoReturn:
    """Writes the provided integer to the byte buffer as a 16-bit value."""
    _write_int8(bytes, value, offset)

    buffer[offset + 1] = (value >> 8) & 0xff

def _write_int32(buffer: bytes, value: int, offset: int) -> NoReturn:
    """Writes the provided integer to the byte buffer as a 32-bit value."""
    _write_int16(buffer, value, offset)
    
    buffer[offset + 2] = (value >> 16) & 0xff
    buffer[offset + 3] = (value >> 24) & 0xff

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

def write_int8(buffer: bytes, value: int, offset: int = 0) -> NoReturn:
    """Writes the provided value to the byte buffer as a signed 8-bit integer.

    This function serializes the provided signed 8-bit integer value and writes
    it into the specified byte buffer at the given offset.

    Raises
    ------
    ValueError
        If the provided value is not between -128 and 127.
    """
    if not -128 <= value <= 127:
        raise ValueError('Value must be between -128 and 127.')

    _write_int8(buffer, value, offset)

def write_int16(buffer: bytes, value: int, offset: int = 0) -> NoReturn:
    """Writes the provided value to the byte buffer as a signed 16-bit integer.

    This function serializes the provided signed 16-bit integer value and writes
    it into the specified byte buffer at the given offset.

    Raises
    ------
    ValueError
        If the provided value is not between -32768 and 32767.
    """
    if not -32768 <= value <= 32767:
        raise ValueError('Value must be between -32768 and 32767.')

    _write_int16(buffer, value, offset)

def write_int32(buffer: bytes, value: int, offset: int = 0) -> NoReturn:
    """Writes the provided value to the byte buffer as a signed 32-bit integer.

    This function serializes the provided signed 32-bit integer value and writes
    it into the specified byte buffer at the given offset.
    
    Raises
    ------
    ValueError
        If the provided value is not between -2147483648 and 2147483647.
    """
    if not -2147483648 <= value <= 2147483647:
        raise ValueError('Value must be between -2147483648 and 2147483647.')

    _write_int32(buffer, value, offset)

def write_uint8(buffer: bytes, value: int, offset: int = 0) -> NoReturn:
    """Writes the provided value to the byte buffer as a unsigned 8-bit integer.

    This function serializes the provided unsigned 8-bit integer value and writes
    it into the specified byte buffer at the given offset.

    Raises
    ------
    ValueError
        If the provided value is not between 0 and 255.
    """
    if not 0 <= value <= 255:
        raise ValueError('Value must be between 0 and 255.')

    _write_int8(buffer, value, offset)

def write_uint16(buffer: bytes, value: int, offset: int = 0) -> NoReturn:
    """Writes the provided value to the byte buffer as a unsigned 16-bit integer.

    This function serializes the provided unsigned 16-bit integer value and writes
    it into the specified byte buffer at the given offset.
    
    Raises
    ------
    ValueError
        If the provided value is not between 0 and 65535.
    """
    if not 0 <= value <= 65535:
        raise ValueError('Value must be between 0 and 65535.')

    _write_int16(buffer, value, offset)

def write_uint32(buffer: bytes, value: int, offset: int = 0) -> NoReturn:
    """Writes the provided value to the byte buffer as a unsigned 32-bit integer.

    This function serializes the provided unsigned 32-bit integer value and writes
    it into the specified byte buffer at the given offset.
    
    Raises
    ------
    ValueError
        If the provided value is not between 0 and 4294967295.
    """
    if not 0 <= value <= 4294967295:
        raise ValueError('Value must be between 0 and 4294967295.')

    _write_int32(buffer, value, offset)
