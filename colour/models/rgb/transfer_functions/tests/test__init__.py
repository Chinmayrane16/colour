# -*- coding: utf-8 -*-
"""
Defines unit tests for :mod:`colour.models.rgb.transfer_functions.common`
module.
"""

from __future__ import division, unicode_literals

import numpy as np
import unittest

from colour.models.rgb.transfer_functions import (
    encoding_cctf, decoding_cctf, DECODING_CCTFS, ENCODING_CCTFS, EOTFS,
    EOTFS_INVERSE, LOG_DECODING_CURVES, LOG_ENCODING_CURVES, OETFS,
    OETFS_INVERSE, OOTFS, OOTFS_INVERSE)

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2019 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Development'

__all__ = ['TestEncodingCCTF', 'TestDecodingCCTF', 'TestTransferFunctions']


class TestEncodingCCTF(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.encoding_cctf`
    definition unit tests methods.
    """

    def test_raise_exception_encoding_cctf(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.aces.\
log_encoding_ACESproxy` definition raised exception.
        """

        # TODO: Use "assertWarns" when dropping Python 2.7.
        encoding_cctf(0.18, 'ITU-R BT.2100 HLG')
        encoding_cctf(0.18, 'ITU-R BT.2100 PQ')


class TestDecodingCCTF(unittest.TestCase):
    """
    Defines :func:`colour.models.rgb.transfer_functions.decoding_cctf`
    definition unit tests methods.
    """

    def test_raise_exception_decoding_cctf(self):
        """
        Tests :func:`colour.models.rgb.transfer_functions.aces.\
log_encoding_ACESproxy` definition raised exception.
        """

        # TODO: Use "assertWarns" when dropping Python 2.7.
        decoding_cctf(0.18, 'ITU-R BT.2100 HLG')
        decoding_cctf(0.18, 'ITU-R BT.2100 PQ')


class TestTransferFunctions(unittest.TestCase):
    """
    Defines transfer functions unit tests methods.
    """

    def test_transfer_functions(self):
        """
        Tests transfer functions reciprocity.
        """

        ignored_transfer_functions = ('ACESproxy', 'DICOM GSDF',
                                      'Filmic Pro 6')

        decimals = {'D-Log': 1, 'F-Log': 4}

        reciprocal_mappings = [
            (LOG_ENCODING_CURVES, LOG_DECODING_CURVES),
            (OETFS, OETFS_INVERSE),
            (EOTFS, EOTFS_INVERSE),
            (ENCODING_CCTFS, DECODING_CCTFS),
            (OOTFS, OOTFS_INVERSE),
        ]

        samples = np.hstack(
            [np.linspace(0, 1, 1e5),
             np.linspace(0, 65504, 65504 * 10)])

        for encoding_mapping, _decoding_mapping in reciprocal_mappings:
            for name in encoding_mapping:
                if name in ignored_transfer_functions:
                    continue

                encoded_s = ENCODING_CCTFS[name](samples)
                decoded_s = DECODING_CCTFS[name](encoded_s)

                np.testing.assert_almost_equal(
                    samples, decoded_s, decimal=decimals.get(name, 7))


if __name__ == '__main__':
    unittest.main()
