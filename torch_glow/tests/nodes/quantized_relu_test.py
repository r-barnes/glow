# Copyright (c) Glow Contributors. See CONTRIBUTORS file.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pyre-ignore-all-errors

from __future__ import absolute_import, division, print_function, unicode_literals

import torch
from glow.glow.torch_glow.tests.tests import utils


class SimpleQuantizedReluModel(torch.nn.Module):
    def __init__(self, scale, zero_point, dtype):
        super(SimpleQuantizedReluModel, self).__init__()
        self.scale = scale
        self.zero_point = zero_point
        self.dtype = dtype

    def forward(self, tensor):
        quantize = torch.nn.quantized.Quantize(
            scale=self.scale, zero_point=self.zero_point, dtype=self.dtype
        )
        dequantize = torch.nn.quantized.DeQuantize()
        relu = torch.nn.ReLU()
        return dequantize(relu(quantize(tensor)))


class TestQuantizedRelu(utils.TorchGlowTestCase):
    def test_quantized_relu(self):
        """Basic test of the PyTorch quantized::relu Node on Glow."""

        utils.compare_tracing_methods(
            SimpleQuantizedReluModel(1.0 / 128, 3, torch.quint8),
            torch.randn([5, 5]),
            fusible_ops={"aten::relu", "aten::quantize_per_tensor", "aten::dequantize"},
        )

    def test_quantized_relu_cut_dq(self):
        """Basic test of the PyTorch quantized::relu Node on Glow, with quantize and dequantize excluded."""

        utils.compare_tracing_methods(
            SimpleQuantizedReluModel(1.0 / 128, 3, torch.quint8),
            torch.randn([5, 5]),
            fusible_ops={"aten::relu", "aten::quantize_per_tensor"},
            fusion_blocklist=["aten::dequantize"],
        )
