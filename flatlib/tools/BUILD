load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:private"])

py_library(
    name = "package",
    srcs = ["__init__.py"],
    imports = ["../.."],
    visibility = ["//:__pkg__"],
)

py_library(
    name = "chartdynamics",
    srcs = ["chartdynamics.py"],
    imports = ["../.."],
    deps = [
        "//:core",
        ":package",
        "//flatlib/dignities:essential",
    ],
    visibility = ["//:__pkg__", "//flatlib/dignities:__pkg__"],
)

py_library(
    name = "arabicparts",
    srcs = ["arabicparts.py"],
    imports = ["../.."],
    deps = [
        "//:core",
        ":package",
        "//flatlib/dignities:essential",
    ],
    visibility = ["//:__pkg__"],
)

py_library(
    name = "planetarytime",
    srcs = ["planetarytime.py"],
    imports = ["../.."],
    deps = [
        "//:core",
        ":package",
        "//flatlib/ephem:ephem",
    ],
    visibility = ["//:__pkg__", "//flatlib/protocols:__pkg__"],
)
