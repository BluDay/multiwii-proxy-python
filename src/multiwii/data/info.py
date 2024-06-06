from ..config import MultiWiiCapability, MultiWiiMultitype, MultiWiiSensor

from dataclasses import dataclass
from typing      import Self

@dataclass
class MspAnalog:
    """
    Represents data values for the MSP_ANALOG command.

    This class encapsulates the analog telemetry data from the MultiWii flight controller. It
    provides information about the system's voltage, power meter, RSSI, and amperage.
    """
    voltage: float
    """float: The voltage of the system, measured in volts."""
    
    power_meter_sum: int
    """int: The accumulated power consumption, measured in arbitrary units."""

    rssi: int
    """int: The Received Signal Strength Indicator (RSSI), representing the signal strength."""

    amperage: int
    """int: The current amperage drawn, measured in milliamps."""

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """
        Parses a tuple of data values obtained from `struct.unpack` and returns an instance
        of the `MspAnalog` class.

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
    """
    Represents data values for the MSP_IDENT command.

    This class encapsulates the identification data from the MultiWii flight controller. It
    provides information about the firmware version, multitype, capabilities, and navigation
    version.
    """
    version: int
    """int: The firmware version of the flight controller."""

    multitype: MultiWiiMultitype
    """MultiWiiMultitype: The vehicle configuration type."""

    capabilities: tuple[MultiWiiCapability]
    """tuple[MultiWiiCapability]: A tuple with available flight capabilities."""

    navigation_version: int
    """The navigation version of the firmware."""

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """
        Parses a tuple of data values obtained from `struct.unpack` and returns an instance of
        the `MspIdent` class.

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

        available_capabilities = data[2]

        for capability in MultiWiiCapability:
            if capability & available_capabilities == capability:
                capabilities += (capability,)

        return cls(
            version=data[0],
            multitype=MultiWiiMultitype(data[1]),
            capabilities=capabilities,
            navigation_version=data[3]
        )

@dataclass
class MspMisc:
    """
    Represents data values for the MSP_MISC command.

    This class encapsulates miscellaneous configuration and status data from the MultiWii
    flight controller. It includes information about power triggers, throttle settings,
    battery warnings, and other miscellaneous parameters.
    """
    power_trigger: int
    """int: The power trigger value."""

    throttle_failsafe: int
    """int: The throttle failsafe value."""

    throttle_idle: int
    """int: The idle throttle value."""

    throttle_min: int
    """int: The minimum throttle value."""

    throttle_max: int
    """int: The maximum throttle value."""

    power_logger_arm: int
    """int: The power logger arm value."""

    power_logger_lifetime: int
    """int: The power logger lifetime value."""

    magnetometer_declination: float
    """float: The magnetic declination value, measured in degrees."""

    battery_scale: int
    """int: The battery scale value."""

    battery_warning_1: float
    """float: The first battery warning level, measured in volts."""

    battery_warning_2: float
    """float: The second battery warning level, measured in volts."""

    battery_critical: float
    """float: The critical battery level, measured in volts."""

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """
        Parses a tuple of data values obtained from `struct.unpack` and returns an instance of
        the `MspMisc` class.

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
            power_logger_arm=data[5],
            power_logger_lifetime=data[6],
            magnetometer_declination=data[7] / 10.0,
            battery_scale=data[8],
            battery_warning_1=data[9] / 10.0,
            battery_warning_2=data[10] / 10.0,
            battery_critical=data[11] / 10.0
        )

@dataclass
class MspSetMisc:
    """
    Represents data values for the MSP_SET_MISC command.

    This class encapsulates miscellaneous configuration data to be set on the MultiWii flight
    controller. It includes information about power triggers, throttle settings, battery
    warnings, and other miscellaneous parameters.
    """
    power_trigger: int
    """int: The power trigger value."""

    throttle_min: int
    """int: The minimum throttle value."""

    throttle_max: int
    """int: The maximum throttle value."""

    min_command: int
    """int: The minimum command value."""

    throttle_failsafe: int
    """int: The throttle value for failsafe."""

    power_logger_arm: int
    """int: The power logger arm value."""

    power_logger_lifetime: int
    """int: The power logger lifetime value."""

    magnetometer_declination: float
    """float: The magnetic declination value, measured in degrees."""

    battery_scale: int
    """int: The battery scale value."""

    battery_warning_1: float
    """float: The first battery warning level, measured in volts."""

    battery_warning_2: float
    """float: The second battery warning level, measured in volts."""

    battery_critical: float
    """float: The critical battery level, measured in volts."""

    def as_serializable(self) -> tuple[int]:
        """
        Returns a tuple with integer values to be used for serialization.

        Returns
        -------
        tuple[int]
            A tuple with serializable integer values.
        """
        return (
            self.power_trigger,
            self.throttle_min,
            self.throttle_max,
            self.min_command,
            self.throttle_failsafe,
            self.power_logger_arm,
            self.power_logger_lifetime,
            int(self.magnetometer_declination * 10),
            self.battery_scale,
            int(self.battery_warning_1 * 10),
            int(self.battery_warning_2 * 10),
            int(self.battery_critical * 10)
        )

@dataclass
class MspStatus:
    """
    Represents data values for the MSP_STATUS command.

    This class encapsulates the status data from the MultiWii flight controller. It provides
    information about cycle time, I2C errors, sensors, flags, and global configuration.
    """
    cycle_time: int
    """int: The cycle time in microseconds."""

    i2c_errors: int
    """int: The count of I2C errors."""

    sensors: tuple[MultiWiiSensor]
    """tuple[MultiWiiSensor]: A tuple representing the sensors' status."""

    status_flag: int
    """int: The status flag."""

    global_config: int
    """int: The global configuration value."""

    @classmethod
    def parse(cls, data: tuple) -> Self:
        """
        Parses a tuple of data values obtained from `struct.unpack` and returns an instance of
        the `MspStatus` class.

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

        available_sensors = data[2]

        for sensor in MultiWiiSensor:
            if sensor & available_sensors == sensor:
                sensors += (sensor,)

        return cls(
            cycle_time=data[0],
            i2c_errors=data[1],
            sensors=sensors,
            status_flag=data[3],
            global_config=data[4]
        )
