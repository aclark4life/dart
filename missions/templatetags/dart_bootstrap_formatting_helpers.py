# Copyright 2024 Lockheed Martin Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def testCaseStatusToBootstrapClass(value, arg):
    """
    Translates the test case status value to the appropriate class to trigger the right color highlighting
    :param arg: the boolean value of test_case_include_flag
    """

    if not arg:
        return "info"
    else:
        translations = {
            "NEW": "",
            "IN_WORK": "danger",
            "REVIEW": "warning",
            "FINAL": "success",
        }

        return translations[value]
