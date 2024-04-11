from typing import Final

class MultiWiiCommands(object):
    """An enum-like class with all MSP command codes."""

    # Get commands.
    MSP_IDENT:      Final[int] = 100
    MSP_STATUS:     Final[int] = 101
    MSP_RAW_IMU:    Final[int] = 102
    MSP_SERVO:      Final[int] = 103
    MSP_MOTOR:      Final[int] = 104
    MSP_RC:         Final[int] = 105
    MSP_RAW_GPS:    Final[int] = 106
    MSP_COMP_GPS:   Final[int] = 107
    MSP_ATTITUDE:   Final[int] = 108
    MSP_ALTITUDE:   Final[int] = 109
    MSP_ANALOG:     Final[int] = 110
    MSP_RC_TUNING:  Final[int] = 111
    MSP_PID:        Final[int] = 112
    MSP_BOX:        Final[int] = 113
    MSP_MISC:       Final[int] = 114
    MSP_MOTOR_PINS: Final[int] = 115
    MSP_BOXNAMES:   Final[int] = 116
    MSP_PIDNAMES:   Final[int] = 117
    MSP_WP:         Final[int] = 118
    MSP_BOXIDS:     Final[int] = 119
    MSP_SERVO_CONF: Final[int] = 120

    # Set commands.
    MSP_SET_RAW_RC:      Final[int] = 200
    MSP_SET_RAW_GPS:     Final[int] = 201
    MSP_SET_PID:         Final[int] = 202
    MSP_SET_BOX:         Final[int] = 203
    MSP_SET_RC_TUNING:   Final[int] = 204
    MSP_ACC_CALIBRATION: Final[int] = 205
    MSP_MAG_CALIBRATION: Final[int] = 206
    MSP_SET_MISC:        Final[int] = 207
    MSP_RESET_CONF:      Final[int] = 208
    MSP_SET_HEAD:        Final[int] = 211
    MSP_SET_SERVO_CONF:  Final[int] = 212
    MSP_SET_MOTOR:       Final[int] = 214
    MSP_BIND:            Final[int] = 240
    MSP_EEPROM_WRITE:    Final[int] = 250

class MultiWiiMessageDirection(object):
    """An enum-like class for message direction characters."""

    """The error character."""
    ERROR: Final[str] = '!'
    
    """The incoming direction character."""
    INCOMING: Final[str] = '<'

    """The outgoing direction character."""
    OUTGOING: Final[str] = '>'
    
    """A serialized error character."""
    SERIALIZED_ERROR: Final[int] = int() # serialize_to_int8(ERROR)

    """A serialized incoming direction character."""
    SERIALIZED_INCOMING: Final[int] = int() # serialize_to_int8(INCOMING)

    """A serialized outgoing direction character."""
    SERIALIZED_OUTGOING: Final[int] = int() # serialize_to_int8(OUTGOING)

class MultiWiiMessageHeader(object):
    """The class for managing and analyzing MultiWii messages."""

    """The fixed MSP v1 preamble used for all messages."""
    PREAMBLE: Final[str] = '$M'

    """The incoming header."""
    INCOMING: Final[str] = f'{PREAMBLE}{MultiWiiMessageDirection.INCOMING}'

    """The outgoing header."""
    OUTGOING: Final[str] = f'{PREAMBLE}{MultiWiiMessageDirection.OUTGOING}'

    """ A serialized preamble."""
    SERIALIZED_PREAMBLE: Final[bytes] = int() # encode(PREAMBLE)

    """A serialized incoming header."""
    SERIALIZED_INCOMING: Final[bytes] = int() # encode(INCOMING)

    """A serialized outgoing header."""
    SERIALIZED_OUTGOING: Final[bytes] = int() # encode(OUTGOING)

class MultiWiiMessagePayload(object):
    """A utility with various payload-related methods."""

    # ------------------------------------- STATIC METHODS -------------------------------------

    @staticmethod
    def calculate_checksum(payload: bytes) -> int:
        """Calculates the checksum for the payload using an XOR CRC (cyclic redundancy check).

        Parameters:
            payload (bytes): The serialized message payload.

        Returns:
            int: The checksum value.
        """
        checksum = 0

        for byte in payload: checksum ^= byte

        return checksum & 0xff
