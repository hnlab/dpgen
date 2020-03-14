import os,sys,json,glob,shutil
import dpdata
import numpy as np
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
__package__ = 'generator'
from .context import check_bad_conf

class TestCheckBadConf(unittest.TestCase):
    def test_length_ratio(self):
        dirname = os.path.dirname(__file__)
        conf_bad = os.path.join(dirname, 'check_bad_conf', 'bad.length.lammpstrj')
        conf_good = os.path.join(dirname, 'check_bad_conf', 'good.lammpstrj')
        self.assertTrue(check_bad_conf(conf_bad, 'length_ratio:5'))
        self.assertFalse(check_bad_conf(conf_good, 'length_ratio:5'))

    def test_height_ratio(self):
        dirname = os.path.dirname(__file__)
        conf_bad = os.path.join(dirname, 'check_bad_conf', 'bad.height.POSCAR')
        self.assertTrue(check_bad_conf(conf_bad, 'height_ratio:5', fmt = 'vasp/POSCAR'))
        self.assertFalse(check_bad_conf(conf_bad, 'length_ratio:5', fmt = 'vasp/POSCAR'))
