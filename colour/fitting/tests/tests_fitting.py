# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**tests_fitting.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines units tests for :mod:`colour.fitting` package.

**Others:**

"""

from __future__ import unicode_literals

import sys

import numpy as np


if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

import colour.fitting

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2013 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["M1",
           "M2",
           "TestFirstOrderColourFit"]

M1 = np.array([
    [0.1722480953, 0.09170660377, 0.06416938454],
    [0.4918964505, 0.2780205011, 0.2192339897],
    [0.1099975109, 0.1865894645, 0.2993861139],
    [0.1166611984, 0.1432790458, 0.05713804066],
    [0.1898887902, 0.1822764874, 0.3605624735],
    [0.1250132918, 0.422234416, 0.3702744544],
    [0.6478560567, 0.2239678204, 0.03365194052],
    [0.06761093438, 0.1107689589, 0.3977913857],
    [0.4910179675, 0.09448929131, 0.1162383854],
    [0.1162238568, 0.04425752908, 0.1446998566],
    [0.3686794639, 0.4454523027, 0.06028680503],
    [0.6163293719, 0.3232390583, 0.02437088825],
    [0.03016472235, 0.06153243408, 0.2901459634],
    [0.1110365465, 0.3055306673, 0.08149136603],
    [0.4116218984, 0.05816655606, 0.04845933989],
    [0.7333920598, 0.530751884, 0.02475212328],
    [0.4734771848, 0.08834791929, 0.3031031489],
    [0, 0.2518701553, 0.3506245017],
    [0.7680963874, 0.7848623991, 0.7780829668],
    [0.5382239223, 0.5430799723, 0.547108829],
    [0.3545852602, 0.3531841934, 0.3552443087],
    [0.1797670424, 0.180005312, 0.1799148768],
    [0.09351416677, 0.09510602802, 0.0967502743],
    [0.03405071422, 0.03295076638, 0.03702046722]])

M2 = np.array([
    [0.1557955891, 0.09715754539, 0.07514556497],
    [0.3911314011, 0.2594341934, 0.2126670778],
    [0.1282482147, 0.1846356988, 0.3150802255],
    [0.1202897355, 0.1345565915, 0.0740839988],
    [0.1936898828, 0.2115894556, 0.3795596361],
    [0.199574247, 0.3608543873, 0.4067812264],
    [0.4889660478, 0.2069168836, 0.05816533044],
    [0.09775521606, 0.1671069264, 0.4714772403],
    [0.3935864866, 0.1223340034, 0.1052642539],
    [0.1078033224, 0.07258529216, 0.1615147293],
    [0.2750267088, 0.3470545411, 0.09728099406],
    [0.439804405, 0.2688055933, 0.05430532619],
    [0.05887211859, 0.1112627164, 0.3855246902],
    [0.1270582527, 0.2578786016, 0.1356646419],
    [0.3561292887, 0.0793325752, 0.05118732154],
    [0.4813197553, 0.4208284318, 0.07120611519],
    [0.3466558456, 0.1517071426, 0.2496980429],
    [0.08261115849, 0.2458871603, 0.4870773256],
    [0.6605490446, 0.6594113708, 0.6637641191],
    [0.4805150926, 0.4787029624, 0.482300818],
    [0.3304535449, 0.3290418386, 0.3322888613],
    [0.1800130457, 0.1797856688, 0.1800441593],
    [0.102839753, 0.1042467952, 0.1038497463],
    [0.04742204025, 0.04772202671, 0.04914225638]])


class TestFirstOrderColourFit(unittest.TestCase):
    """
    Defines :func:`colour.fitting.first_order_colour_fit` definition units tests methods.
    """

    def test_first_order_colour_fit(self):
        """
        Tests :func:`colour.fitting.first_order_colour_fit` definition.
        """

        np.testing.assert_almost_equal(
            colour.fitting.first_order_colour_fit(M1, M2),
            np.array([[1.40431285, 0.01128059, -0.20297103],
                         [-0.09989111, 1.50122142, -0.18564796],
                         [0.22483693, -0.07672362, 1.04960133]]),
            decimal=7)


if __name__ == "__main__":
    unittest.main()
