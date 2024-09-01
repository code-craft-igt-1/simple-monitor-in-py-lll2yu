from time import sleep
import sys


def print_critical_message(message, seconds_to_showmessage):
    print(f"\n{message}")
    full_cycles = seconds_to_showmessage // 2
    remaining_seconds = seconds_to_showmessage % 2
    for _ in range(full_cycles):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)

    if remaining_seconds:
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)


def check_vital(vital_name, vital_value,
                lower_limit_for_vital, upper_limit_for_vital):
    if (
        vital_value < lower_limit_for_vital
        or vital_value > upper_limit_for_vital
    ):
        messages = {
            'Temperature': 'Temperature critical!',
            'Pulse Rate': 'Pulse Rate is out of range!',
            'Oxygen Saturation': 'Oxygen Saturation out of range!'
        }

        message = messages.get(vital_name, f'{vital_name} is out of range!')
        print_critical_message(message, 12)
        return False
    return True


def vitals_ok(temperature_inF, pulse_rate, spo2):
    return all([
        check_vital('Temperature', temperature_inF, 95, 102),
        check_vital('Pulse Rate', pulse_rate, 60, 100),
        check_vital('Oxygen Saturation', spo2, 90, 100)
    ])
