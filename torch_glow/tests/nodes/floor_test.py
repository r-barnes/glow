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


class SimpleFloorModule(torch.nn.Module):
    def forward(self, a, b):
        c = a + b
        return torch.floor(c)


class TestFloor(utils.TorchGlowTestCase):
    def test_floor(self):
        """Basic test of the PyTorch floor Node on Glow."""

        x = torch.randn(3, 4, 5)
        y = torch.randn(3, 4, 5)
        utils.compare_tracing_methods(
            SimpleFloorModule(), x, y, fusible_ops={"aten::floor"}
        )
