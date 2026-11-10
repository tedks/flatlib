load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:private"])

py_library(
    name = "protocols",
    srcs = [
        "__init__.py",
        "almutem.py",
        "behavior.py",
        "temperament.py",
    ],
    imports = ["../.."],
    deps = [
        "//:core",
        "//flatlib/dignities:essential",
        "//flatlib/tools:planetarytime",
    ],
    visibility = ["//:__pkg__"],
)
