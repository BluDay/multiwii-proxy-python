from ..config import MultiWiiCapability, MultiWiiMultitype, MultiWiiSensor

from dataclasses import dataclass
from typing      import Self

@dataclass
class MspAnalog:
    """Represents data values for the MSP_ANALOG command.

    This class encapsulates the analog telemetry data from the MultiWii flight controller.
    It provides information about the system's voltage, power meter, RSSI, and amperage.

    Attributes
    ----------
    voltage : float
        The voltage of the system, measured in volts. This value is derived by dividing
        the raw data by 10.0.
    power_meter_sum : int
        The accumulated power consumption, measured in arbitrary units.
    rssi : int
        The Received Signal Strength Indicator (RSSI), representing the signal strength.
    amperage : int
        The current amperage drawn, measured in milliamps.
    """
    voltage: float

    power_meter_sum: int

    rssi: int

    amperage: int

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """Parses a tuple of data values obtained from `struct.unpack` and returns an
        instance of the `MspAnalog` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspAnalog
            An instance of the `MspAnalog` class populated with the parsed data.
        """
        return cls(
            voltage=data[0] / 10.0,
            power_meter_sum=data[1],
            rssi=data[2],
            amperage=data[3]
        )

@dataclass
class MspIdent:
    """Represents data values for the MSP_IDENT command.

    This class encapsulates the identification data from the MultiWii flight controller.
    It provides information about the firmware version, multitype, capabilities, and
    navigation version.

    Attributes
    ----------
    version : int
        The firmware version of the flight controller.
    multitype : MultiWiiMultitype
        The vehicle configuration type.
    capabilities : tuple[MultiWiiCapability]
        A tuple representing the capabilities of the flight controller.
    navi_version : int
        The navigation version of the firmware.
    """
    version: int

    multitype: MultiWiiMultitype

    capabilities: tuple[MultiWiiCapability]

    navi_version: int

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """Parses a tuple of data values obtained from `struct.unpack` and returns an
        instance of the `MspIdent` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspIdent
            An instance of the `MspIdent` class populated with the parsed data.
        """
        capabilitites = ()

        for capability in MultiWiiCapability:
            if capability & data[2]:
                capabilities += (capability,)

        return cls(
            version=data[0],
            multitype=MultiWiiMultitype(data[1]),
            capabilities=capabilities,
            navi_version=data[3]
        )

@dataclass
class MspMisc:
    """Represents data values for the MSP_MISC command.

    This class encapsulates miscellaneous configuration and status data from the MultiWii
    flight controller. It includes information about power triggers, throttle settings,
    battery warnings, and other miscellaneous parameters.

    Attributes
    ----------
    power_trigger : int
        The power trigger value.
    throttle_failsafe : int
        The throttle failsafe value.
    throttle_idle : int
        The idle throttle value.
    throttle_min : int
        The minimum throttle value.
    throttle_max : int
        The maximum throttle value.
    plog_arm : int
        The power logger arm value.
    plog_lifetime : int
        The power logger lifetime value.
    mag_declination : float
        The magnetic declination value, measured in degrees.
    battery_scale : int
        The battery scale value.
    battery_warn_1 : float
        The first battery warning level, measured in volts.
    battery_warn_2 : float
        The second battery warning level, measured in volts.
    battery_critical : float
        The critical battery level, measured in volts.
    """
    power_trigger: int

    throttle_failsafe: int

    throttle_idle: int

    throttle_min: int

    throttle_max: int

    plog_arm: int

    plog_lifetime: int

    mag_declination: float

    battery_scale: int

    battery_warn_1: float

    battery_warn_2: float

    battery_critical: float

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """Parses a tuple of data values obtained from `struct.unpack` and returns an
        instance of the `MspMisc` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspMisc
            An instance of the `MspMisc` class populated with the parsed data.
        """
        return cls(
            power_trigger=data[0],
            throttle_failsafe=data[1],
            throttle_idle=data[2],
            throttle_min=data[3],
            throttle_max=data[4],
            plog_arm=data[5],
            plog_lifetime=data[6],
            mag_declination=data[7] / 10.0,
            battery_scale=data[8],
            battery_warn_1=data[9] / 10.0,
            battery_warn_2=data[10] / 10.0,
            battery_critical=data[11] / 10.0
        )

@dataclass
class MspSetMisc:
    """Represents data values for the MSP_SET_MISC command.

    This class encapsulates miscellaneous configuration data to be set on the MultiWii
    flight controller. It includes information about power triggers, throttle settings,
    battery warnings, and other miscellaneous parameters.

    Attributes
    ----------
    power_trigger : int
        The power trigger value.
    throttle_min : int
        The minimum throttle value.
    throttle_max : int
        The maximum throttle value.
    min_command : int
        The minimum command value.
    throttle_failsafe : int
        The throttle value for failsafe.
    power_logger_arm : int
        The power logger arm value.
    power_logger_lifetime : int
        The power logger lifetime value.
    magnetometer_declination : float
        The magnetic declination value, measured in degrees.
    battery_scale : int
        The battery scale value.
    battery_warning_1 : float
        The first battery warning level, measured in volts.
    battery_warning_2 : float
        The second battery warning level, measured in volts.
    battery_critical : float
        The critical battery level, measured in volts.
    """
    power_trigger: int

    throttle_min: int

    throttle_max: int

    min_command: int

    throttle_failsafe: int

    power_logger_arm: int

    power_logger_lifetime: int

    magnetometer_declination: float

    battery_scale: int

    battery_warning_1: float

    battery_warning_2: float

    battery_critical: float

@dataclass
class MspStatus:
    """Represents data values for the MSP_STATUS command.

    This class encapsulates the status data from the MultiWii flight controller.
    It provides information about cycle time, I2C errors, sensors, flags, and
    global configuration.

    Attributes
    ----------
    cycle_time : int
        The cycle time in microseconds.
    i2c_errors : int
        The count of I2C errors.
    sensors : tuple[MultiWiiSensor]
        A tuple representing the sensors' status.
    status_flag : int
        The status flag.
    global_config : int
        The global configuration value.
    """
    cycle_time: int

    i2c_errors: int

    sensors: tuple[MultiWiiSensor]

    status_flag: int

    global_config: int

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """Parses a tuple of data values obtained from `struct.unpack` and returns an
        instance of the `MspStatus` class.

        Parameters
        ----------
        data : tuple
            A tuple containing unpacked data values.

        Returns
        -------
        MspStatus
            An instance of the `MspStatus` class populated with the parsed data.
        """
        sensors = ()

        for sensor in cls:
            if sensor | data[2]:
                sensors += (sensor,)

        return cls(
            cycle_time=data[0],
            i2c_errors=data[1],
            sensors=sensors,
            status_flag=data[3],
            global_config=data[4]
        )
