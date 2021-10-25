from unittest import TestCase
from pygbmfg import read_maverick_func_br


class TestReadingFunction(TestCase):
    def test_read_std_file(self):
        df = read_maverick_func_br(file="datafiles/mav_correct_br.xlsx")
        self.assertEqual(len(df), 4)
