import board
import busio
import time
from rich.live import Live
from rich.table import Table
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)

left_thrusters = ADS.ADS1015(i2c, address=0x48)
right_thrusters = ADS.ADS1015(i2c, address=0x49)
voltage_channels = ADS.ADS1015(i2c, address=0x4A)

ads_pins = [ADS.P0, ADS.P1, ADS.P2, ADS.P3]

SHUNT_VALUE = 0.0033
AMP_FACTOR = 50

# Voltage amplification factors for each channel
VOLTAGE_GAINS = {
    ADS.P0: 19.8,  # expects ~48V
    ADS.P1: 5.273,  # expects ~12V
    ADS.P2: 2.0,   # expects ~5V
    ADS.P3: 2.0,   # expects ~3.3V
}

VOLTAGE_TARGETS = {
    "V0": 48.0,
    "V1": 12.0,
    "V2": 5.0,
    "V3": 3.3,
}

def read_all_channels():
    """Read from all thruster and voltage channels."""
    readings = {}

    # Thruster current channels
    for name, ads in [("L", left_thrusters), ("R", right_thrusters)]:
        for i, pin in enumerate(ads_pins):
            chan = AnalogIn(ads, pin)
            current = chan.voltage / (SHUNT_VALUE * AMP_FACTOR)
            readings[f"{name}{i}"] = current

    # Voltage channels
    for i, pin in enumerate(ads_pins):
        chan = AnalogIn(voltage_channels, pin)
        voltage = chan.voltage * VOLTAGE_GAINS[pin]
        readings[f"V{i}"] = voltage

    return readings


def make_table(readings):
    """Create a rich table showing thruster currents and voltages."""
    table = Table(title="Current & Voltage Monitor", expand=True)

    table.add_column("Channel", justify="center", style="bold cyan")
    table.add_column("Reading", justify="center", style="bold yellow")

    for label, value in readings.items():
        if label.startswith(("L", "R")):
            # Current channels
            unit = "A"
            color = "green"
            if abs(value) > 10:
                color = "red"
            elif abs(value) > 5:
                color = "yellow"
            display = f"[{color}]{value:7.2f} {unit}[/{color}]"
        else:
            # Voltage channels
            unit = "V"
            target = VOLTAGE_TARGETS[label]
            deviation = abs(value - target) / target
            if deviation < 0.05:
                color = "green"
            elif deviation < 0.10:
                color = "yellow"
            else:
                color = "red"
            display = f"[{color}]{value:7.2f} {unit}[/{color}]"

        table.add_row(label, display)

    return table


# --- Live updating display ---
with Live(auto_refresh=False, screen=True) as live:
    while True:
        readings = read_all_channels()
        table = make_table(readings)
        live.update(table, refresh=True)
        time.sleep(0.2)
