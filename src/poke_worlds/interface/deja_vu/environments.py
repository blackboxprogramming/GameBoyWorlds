from typing import Optional, Dict, Any, List, Tuple

from gymnasium import spaces

from poke_worlds.emulation.deja_vu.base_metrics import CoreDejaVuMetrics
from poke_worlds.utils import load_parameters, log_dict, log_info
from poke_worlds.emulation.deja_vu.emulators import DejaVuEmulator
from poke_worlds.emulation.deja_vu.trackers import (
    DejaVuOCRTracker,
    CoreDejaVuTracker,
    # DejaVuEnterCastleTestTracker,
)
from poke_worlds.emulation.deja_vu.parsers import AgentState
from poke_worlds.interface.environment import (
    DummyEnvironment,
    Environment,
    TestEnvironmentMixin,
)
from poke_worlds.interface.controller import Controller


class DejaVuEnvironment(DummyEnvironment):
    """
    A basic Deja Vu Environment.
    
    Deja Vu is a detective mystery game focused on investigation and puzzle-solving.
    The game mechanics include exploration, dialogue interactions, and deduction puzzles.
    """

    REQUIRED_EMULATOR = DejaVuEmulator
    REQUIRED_STATE_TRACKER = CoreDejaVuMetrics


class DejaVuOCREnvironment(DejaVuEnvironment):
    """
    A Deja Vu Environment that includes OCR region captures and agent state.
    
    Provides screen pixels and agent state information for vision-based agents.
    Agent state includes: Free Roam, In Dialogue, In Menu, In Puzzle.
    """

    REQUIRED_STATE_TRACKER = DejaVuOCRTracker
    REQUIRED_EMULATOR = DejaVuEmulator

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def override_emulator_kwargs(emulator_kwargs: dict) -> dict:
        required_tracker = DejaVuOCRTracker
        Environment.override_state_tracker_class(emulator_kwargs, required_tracker)
        return emulator_kwargs


class DejaVuTestEnvironment(TestEnvironmentMixin, DejaVuOCREnvironment):
    """
    A test environment for Deja Vu that integrates testing utilities with OCR capabilities.
    """
    pass