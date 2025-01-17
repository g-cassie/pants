# Copyright 2021 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# NB: The project names must follow the naming scheme at
#  https://www.python.org/dev/peps/pep-0503/#normalized-names.
DEFAULT_MODULE_MAPPING = {
    "ansicolors": ("colors",),
    "apache-airflow": ("airflow",),
    "attrs": ("attr",),
    "beautifulsoup4": ("bs4",),
    "djangorestframework": ("rest_framework",),
    "enum34": ("enum",),
    "paho-mqtt": ("paho",),
    "protobuf": ("google.protobuf",),
    "pycrypto": ("Crypto",),
    "pyopenssl": ("OpenSSL",),
    "python-dateutil": ("dateutil",),
    "python-jose": ("jose",),
    "pyyaml": ("yaml",),
    "pymongo": ("bson", "gridfs"),
    "pytest-runner": ("ptr",),
    "setuptools": ("easy_install", "pkg_resources", "setuptools"),
}

DEFAULT_TYPE_STUB_MODULE_MAPPING = {
    "djangorestframework-types": ("rest_framework",),
    "types-enum34": ("enum34",),
    "types-protobuf": ("google.protobuf",),
    "types-pycrypto": ("Crypto",),
    "types-pyopenssl": ("OpenSSL",),
    "types-pyyaml": ("yaml",),
    "types-python-dateutil": ("dateutil",),
    "types-setuptools": ("easy_install", "pkg_resources", "setuptools"),
}
