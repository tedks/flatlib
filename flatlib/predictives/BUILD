load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:private"])

py_library(
    name = "predictives",
    srcs = [
        "__init__.py",
        "primarydirections.py",
        "profections.py",
        "returns.py",
    ],
    imports = ["../.."],
    deps = [
        "//:chart",
        "//:core",
        "//flatlib/dignities:essential",
        "//flatlib/ephem:ephem",
    ],
    visibility = ["//:__pkg__"],
)
