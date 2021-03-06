"""
 Copyright (c) 2018-2019 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import unittest

from unittest.mock import patch

from extensions.front.caffe.elu import ELUFrontExtractor
from mo.utils.unittest.extractors import FakeMultiParam
from mo.utils.unittest.graph import FakeNode


class FakeProtoLayer:
    def __init__(self, val):
        self.elu_param = val


class TestElu(unittest.TestCase):
    @patch('extensions.front.caffe.elu.collect_attributes')
    def test_elu_ext(self, collect_attrs_mock):
        params = {
            'alpha': 4
        }
        collect_attrs_mock.return_value = {
            **params,
            'test': 54,
            'test2': 'test3'
        }

        fn = FakeNode(FakeProtoLayer(FakeMultiParam(params)), None)
        ELUFrontExtractor.extract(fn)

        exp_res = {
            'type': 'Elu',
            'alpha': 4
        }

        for i in exp_res:
            self.assertEqual(fn[i], exp_res[i])
