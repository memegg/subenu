# core/runner.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from controller import Controller


def run_auto_analyzer(target):
    print(f"\n🚀 Starting automated analysis for: {target}\n")

    controller = Controller(target)
    controller.run_all()

    print(f"\n✅ Analysis completed for: {target}\n")
