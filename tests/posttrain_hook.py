###############################################################################
# Copyright (c) 2026, Advanced Micro Devices, Inc. All rights reserved.
#
# See LICENSE for license information.
###############################################################################
"""The posttrain conversion hook (01_convert_checkpoints.py) for tests: its path and a
fresh module of it. The hook is a script, not a package module, so tests load it by
path."""

import importlib.util
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
HOOK = REPO / "runner/helpers/hooks/train/posttrain/megatron/01_convert_checkpoints.py"


def load_hook(name="convert_checkpoints_hook"):
    """A newly executed module of the hook (tests may monkeypatch it freely)."""
    spec = importlib.util.spec_from_file_location(name, HOOK)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
