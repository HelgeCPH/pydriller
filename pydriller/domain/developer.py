# Copyright 2018 Davide Spadini
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
This module includes only 1 class, Developer, representing a developer.
"""


from typing import Optional


class Developer:
    """
    This class represents a developer. We save the email and the name.
    """

    def __init__(self, name: Optional[str] = None, email: Optional[str] = None):
        """
        Class to identify a developer.

        :param str name: name and surname of the developer
        :param str email: email of the developer
        """
        self.name = name
        self.email = email

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Developer):
            return NotImplemented
        if self is other:
            return True

        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'Developer("{self.name}", "{self.email}")'

    def __str__(self):
        return f"{self.name}, <{self.email}>"
