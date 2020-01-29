# Copyright © 2019 Province of British Columbia
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
"""Test Suite for all of the filing validations."""


def lists_are_equal(list_1, list_2) -> bool:
    """Assert that the unordered lists contain the same elements."""
    if len(list_1) != len(list_2):
        return False
    found = False
    for i in list_1:
        for j in list_2:
            if i == j:
                found = True
                break
            else:
                found = False
    return found
