"""Flatlib source graph, split at Python package and dependency boundaries."""

load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:private"])

py_library(
    name = "core",
    srcs = [
        "flatlib/__init__.py",
        "flatlib/angle.py",
        "flatlib/aspects.py",
        "flatlib/const.py",
        "flatlib/datetime.py",
        "flatlib/geopos.py",
        "flatlib/lists.py",
        "flatlib/object.py",
        "flatlib/props.py",
        "flatlib/utils.py",
    ],
    imports = ["."],
    visibility = [
        "//flatlib/dignities:__pkg__",
        "//flatlib/ephem:__pkg__",
        "//flatlib/predictives:__pkg__",
        "//flatlib/protocols:__pkg__",
        "//flatlib/tools:__pkg__",
        "//tests:__pkg__",
    ],
)

py_library(
    name = "chart",
    srcs = ["flatlib/chart.py"],
    imports = ["."],
    deps = [
        ":core",
        "//flatlib/ephem:ephem",
    ],
    visibility = [
        "//flatlib/dignities:__pkg__",
        "//flatlib/ephem:__pkg__",
        "//flatlib/predictives:__pkg__",
        "//flatlib/protocols:__pkg__",
        "//flatlib/tools:__pkg__",
        "//tests:__pkg__",
    ],
)

filegroup(
    name = "ephemeris_data",
    srcs = ["flatlib/resources/README.md"] + glob(["flatlib/resources/swefiles/*"]),
    visibility = ["//flatlib/ephem:__pkg__"],
)

py_library(
    name = "flatlib",
    deps = [
        ":chart",
        ":core",
        "//flatlib/dignities:accidental",
        "//flatlib/dignities:essential",
        "//flatlib/predictives:predictives",
        "//flatlib/protocols:protocols",
        "//flatlib/tools:arabicparts",
        "//flatlib/tools:chartdynamics",
        "//flatlib/tools:planetarytime",
    ],
    visibility = ["//visibility:public"],
)
