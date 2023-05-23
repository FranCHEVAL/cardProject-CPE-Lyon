# Copyright 2015 gRPC authors.
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
"""Common resources used in the gRPC route guide example."""

import json

import card_pb2


def read_card_database():
    card_list = []
    with open("card_db.json") as card_db_file:
        for item in json.load(card_db_file):
            card = card_pb2.Card(
                name=item["name"],
                id=item["id"])
            card_list.append(card)
    return card_list
