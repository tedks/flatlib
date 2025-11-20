load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "flatlib",
    srcs = glob(["flatlib/**/*.py"]),
    imports = ["."],
    deps = [
        "@pypi//pyswisseph",
    ],
    data = glob(["flatlib/resources/swefiles/*"]),
)
