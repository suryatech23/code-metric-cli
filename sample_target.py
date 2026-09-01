# A sample script used to test code metrics and AST parsing
class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_items(self):
        results = []
        for item in self.data:
            if item > 10:
                if item % 2 == 0:
                    results.append(item * 2)
                else:
                    results.append(item)
            else:
                results.append(0)
        return results

    def clear(self):
        self.data.clear()
