""" Test Data Providers.
 - All variety of InputData options.
"""
from treescriptify.data.input_data import InputData


DEFAULT_INPUT = InputData()
EXCLUDE_HIDDEN_INPUT = InputData(ignore_hidden=True)
DIR_ONLY_INPUT = InputData(directories_only=True)
DIR_ONLY_HIDE_INPUT = InputData(directories_only=True, ignore_hidden=True)
PRUNE_DIR_INPUT = InputData(prune_dirs=True)
DIR_ONLY_PRUNE_INPUT = InputData(directories_only=True, prune_dirs=True)
EXCLUDE_HIDDEN_WITH_DIR_ONLY_PRUNE = InputData(
    ignore_hidden=True, directories_only=True, prune_dirs=True
)
DEPTH_1_INPUT = InputData(depth=1,)
DEPTH_2_INPUT = InputData(depth=2,)

DEPTH_1_PRUNE_DIR_INPUT = InputData(depth=1,prune_dirs=True)
DEPTH_2_PRUNE_DIR_INPUT = InputData(depth=2,prune_dirs=True)

DEPTH_1_DIR_ONLY_INPUT = InputData(depth=1,directories_only=True)
DEPTH_2_DIR_ONLY_INPUT = InputData(depth=2,directories_only=True)