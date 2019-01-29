#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/testing")

class BoostProtoConan(base.BoostBaseConan):
    name = "boost_proto"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_proto"
    lib_short_names = ["proto"]
    header_only_libs = ["proto"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_fusion",
        "boost_mpl",
        "boost_preprocessor",
        "boost_range",
        "boost_static_assert",
        "boost_type_traits",
        "boost_typeof",
        "boost_utility"
    ]
