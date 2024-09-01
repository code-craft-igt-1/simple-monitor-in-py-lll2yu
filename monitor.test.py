import unittest
from unittest.mock import patch
from monitor import check_vital, vitals_ok, print_critical_message


class TestMonitor(unittest.TestCase):

    @patch('monitor.print_critical_message')
    def test_temperature_out_of_range_high(self, mock_print):
        result = check_vital('Temperature', 103, 95, 102)
        self.assertFalse(result)
        mock_print.assert_called_with('Temperature critical!', 12)

    @patch('monitor.print_critical_message')
    def test_temperature_out_of_range_low(self, mock_print):
        result = check_vital('Temperature', 94, 95, 102)
        self.assertFalse(result)
        mock_print.assert_called_with('Temperature critical!', 12)

    @patch('monitor.print_critical_message')
    def test_pulse_rate_out_of_range_high(self, mock_print):
        result = check_vital('Pulse Rate', 101, 60, 100)
        self.assertFalse(result)
        mock_print.assert_called_with('Pulse Rate is out of range!', 12)

    @patch('monitor.print_critical_message')
    def test_pulse_rate_out_of_range_low(self, mock_print):
        result = check_vital('Pulse Rate', 59, 60, 100)
        self.assertFalse(result)
        mock_print.assert_called_with('Pulse Rate is out of range!', 12)

    @patch('monitor.print_critical_message')
    def test_spo2_out_of_range_low(self, mock_print):
        result = check_vital('Oxygen Saturation', 89, 90, 100)
        self.assertFalse(result)
        mock_print.assert_called_with('Oxygen Saturation out of range!', 12)

    def test_all_vitals_ok(self):
        result = vitals_ok(98, 70, 95)
        self.assertTrue(result)

    @patch('monitor.print_critical_message')
    def test_vitals_not_ok_temperature(self, mock_print):
        result = vitals_ok(103, 70, 95)
        self.assertFalse(result)
        mock_print.assert_called_with('Temperature critical!', 12)

    @patch('monitor.print_critical_message')
    def test_vitals_not_ok_pulse_rate(self, mock_print):
        result = vitals_ok(98, 101, 95)
        self.assertFalse(result)
        mock_print.assert_called_with('Pulse Rate is out of range!', 12)

    @patch('monitor.print_critical_message')
    def test_vitals_not_ok_spo2(self, mock_print):
        result = vitals_ok(98, 70, 89)
        self.assertFalse(result)
        mock_print.assert_called_with('Oxygen Saturation out of range!', 12)

    @patch('sys.stdout.flush')
    @patch('builtins.print')
    @patch('monitor.sleep', return_value=None)
    def test_print_critical_message(self, mock_sleep, mock_print, mock_flush):
        print_critical_message("Test message", 12)
        self.assertEqual(mock_sleep.call_count, 12)
        mock_sleep.reset_mock()
        print_critical_message("Test message", 7)
        self.assertEqual(mock_sleep.call_count, 7)


if __name__ == '__main__':
    unittest.main()
