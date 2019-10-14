#!/bin/bash

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

set -euxo pipefail

# CHECK: zebra_340\.png: 340$
# cat_285.png is wrongly classified as 281
# CHECK: dog_207\.png: 207$
cd $MODELS_DIR
$BIN/resnet-runtime $IMAGES_DIR/imagenet --num-devices=1 -backend=CPU
