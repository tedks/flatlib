load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:private"])

py_library(
    name = "essential",
    srcs = [
        "__init__.py",
        "essential.py",
        "tables.py",
    ],
    imports = ["../.."],
    deps = ["//:core"],
    visibility = [
        "//:__pkg__",
        "//flatlib/predictives:__pkg__",
        "//flatlib/protocols:__pkg__",
        "//flatlib/tools:__pkg__",
    ],
)

py_library(
    name = "accidental",
    srcs = ["accidental.py"],
    imports = ["../.."],
    deps = [
        "//:core",
        ":essential",
        "//flatlib/tools:chartdynamics",
    ],
    visibility = ["//:__pkg__", "//flatlib/tools:__pkg__"],
)
