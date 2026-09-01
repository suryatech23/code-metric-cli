import ast
import sys

class CodeMetricsAnalyzer(ast.NodeVisitor):
    def __init__(self, filepath):
        self.filepath = filepath
        self.function_count = 0
        self.class_count = 0
        self.total_lines = 0
        self.complexity_score = 0

    def analyze(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            self.total_lines = len(content.splitlines())
            tree = ast.parse(content)
            self.visit(tree)

    def visit_FunctionDef(self, node):
        self.function_count += 1
        # Simple cyclomatic complexity estimation based on branching nodes
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
                self.complexity_score += 1
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.class_count += 1
        self.generic_visit(node)

    def report(self):
        print(f"--- Code Metrics Report: {self.filepath} ---")
        print(f"Total Lines of Code: {self.total_lines}")
        print(f"Classes Found: {self.class_count}")
        print(f"Functions Found: {self.function_count}")
        print(f"Estimated Complexity Score: {self.complexity_score}")
        print("-" * 42)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <path_to_python_file>")
        sys.exit(1)
    
    analyzer = CodeMetricsAnalyzer(sys.argv[1])
    analyzer.analyze()
    analyzer.report()
