# Automated Code Review & Metric CLI Tool

A lightweight developer utility written in Python that utilizes Abstract Syntax Trees (`ast`) to perform static code analysis, track structural complexity, and evaluate maintainability metrics.

## Features
- **Static AST Parsing**: Inspects Python source code without execution to identify classes, functions, and control flow branches.
- **Complexity Tracking**: Calculates cyclomatic complexity scores to flag high-risk maintainability bottlenecks.
- **CLI Interface**: Designed for quick integration into local development workflows and automated scripts.

## Usage
Run the analyzer on any target Python script:
```bash
python analyzer.py sample_target.py
