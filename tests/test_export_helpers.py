"""Extract a pure helper without importing the effectful training export."""
import ast
import contextlib
import io
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1] / 'crypto_market_prediction_project-DB_DL_combined/갈대 AI/갈대_AI_LSTM_최적화.py'


class ExportHelperTests(unittest.TestCase):
    def setUp(self):
        tree = ast.parse(PATH.read_text(encoding='utf-8'))
        node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'below_threshold_len')
        namespace = {}
        exec(compile(ast.Module([node], type_ignores=[]), str(PATH), 'exec'), namespace)
        self.helper = namespace['below_threshold_len']

    def test_report_counts_sequences_at_or_below_threshold(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.helper(2, [[1], [1, 2], [1, 2, 3]])
        self.assertAlmostEqual(float(output.getvalue().rsplit(':', 1)[1]), 200/3)

    def test_zero_threshold_counts_empty_sequence(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.helper(0, [[], [1]])
        self.assertEqual(float(output.getvalue().rsplit(':', 1)[1]), 50)


if __name__ == '__main__':
    unittest.main()
