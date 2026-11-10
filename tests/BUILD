load("@rules_python//python:defs.bzl", "py_test")

package(default_visibility = ["//visibility:private"])

py_test(
    name = "existing_tests",
    srcs = [
        "test_angles.py",
        "test_chart.py",
        "test_main.py",
    ],
    imports = ["."],
    main = "test_main.py",
    python_version = "3.11",
    deps = ["//:flatlib"],
    legacy_create_init = 0,
)
