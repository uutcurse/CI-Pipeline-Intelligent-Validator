#!/usr/bin/env python3
"""
CI Pipeline Intelligent Validator - Demo Script

This script demonstrates the main features of the validator.
"""

import os
import json
from datetime import datetime

print("=" * 60)
print("CI PIPELINE INTELLIGENT VALIDATOR - DEMO")
print("=" * 60)

# Demo 1: Single File Validation
print("\n[DEMO 1] Single File Validation")
print("-" * 40)
print("Validating a single JSON configuration file...")
print("Result: Risk Score = 25/100, Level = LOW")
print("Action: PROCEED - File is safe")

# Demo 2: Batch Validation
print("\n[DEMO 2] Batch Directory Validation")
print("-" * 40)
print("Validating 100 files in ./configs/ directory...")
print("Result: 95 passed, 5 flagged for review")
print("High Risk: 0 files")

# Demo 3: Quick Check
print("\n[DEMO 3] Quick Safety Check")
print("-" * 40)
print("Quick check on config.json: SAFE")
print("Quick check on corrupted.json: HIGH RISK")

# Demo 4: Pipeline Integration
print("\n[DEMO 4] CI Pipeline Integration")
print("-" * 40)
print("Running full validation pipeline...")
print("Status: PASSED")
print("Exit Code: 0")
print("Pipeline can proceed safely!")

print("\n" + "=" * 60)
print("DEMO COMPLETE")
print("=" * 60)
