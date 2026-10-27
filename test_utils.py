import unittest
from src.utils import parse_json_safely, normalize_assessment, detect_emergency_red_flags

class UtilityTests(unittest.TestCase):
    def test_parse_fenced_json(self):
        obj, error = parse_json_safely('```json\n{"summary":"ok","urgency_level":"LOW"}\n```')
        self.assertIsNone(error)
        self.assertEqual(obj["summary"], "ok")

    def test_bad_json_does_not_crash(self):
        obj, error = parse_json_safely("{bad json")
        self.assertIsNone(obj)
        self.assertIsNotNone(error)

    def test_normalize_urgency(self):
        self.assertEqual(normalize_assessment({"urgency_level":"unknown"})["urgency_level"], "MEDIUM")

    def test_red_flag(self):
        found = detect_emergency_red_flags({"symptoms":["Chest pain"],"symptom_notes":"","notes":""})
        self.assertTrue(found)

if __name__ == "__main__":
    unittest.main()
