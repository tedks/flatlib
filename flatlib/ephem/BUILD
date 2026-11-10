load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:private"])

py_library(
    name = "ephem",
    srcs = [
        "__init__.py",
        "eph.py",
        "ephem.py",
        "swe.py",
        "tools.py",
    ],
    imports = ["../.."],
    data = ["//:ephemeris_data"],
    deps = [
        "//:core",
        "@flatlib_pypi//pyswisseph",
    ],
    visibility = [
        "//:__pkg__",
        "//flatlib/dignities:__pkg__",
        "//flatlib/predictives:__pkg__",
        "//flatlib/protocols:__pkg__",
        "//flatlib/tools:__pkg__",
    ],
)
