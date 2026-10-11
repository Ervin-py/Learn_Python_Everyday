import unittest
from drawing_app import search_dwg, drawing, validate_dwg
from drawing_app import validate_revision
from drawing_app import validate_status

class TestValidateDwg(unittest.TestCase):
    def test_valid_drawing_number(self):
        result = validate_dwg("DWG-001")
        self.assertTrue(result)

    def test_invalid_drawing_number(self):
        result = validate_dwg("ABC-001")
        self.assertFalse(result)

    def test_valid_revision(self):
        result = validate_revision("A")
        self.assertTrue(result)

    def test_invalid_revision(self):
        result = validate_revision("0")
        self.assertFalse(result)

    def test_valid_status(self):
        result = validate_status("WIP")
        self.assertTrue(result)

    def test_invalid_status(self):
        result = validate_status("kk")
        self.assertFalse(result)

    def test_valid_drawing(self):
        result = search_dwg(drawing, "DWG-001")
        self.assertTrue(result)

    def test_invalid_drawing(self):
        result = search_dwg(drawing, "DWG-008")
        self.assertFalse(result)


    