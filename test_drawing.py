import unittest
from drawing_app import search_dwg, validate_dwg, load_drawings
from drawing_app import validate_revision
from drawing_app import validate_status

class TestValidateDwg(unittest.TestCase):
#validate_dwg
    def test_valid_drawing_number(self):
        result = validate_dwg("DWG-001")
        self.assertTrue(result)

    def test_invalid_drawing_number_short(self):
        result = validate_dwg("ABC-00")
        self.assertFalse(result)

    def test_invalid_drawing_number_format(self):
        result = validate_dwg("NUM-123")
        self.assertFalse(result)

    def test_invalid_drawing_number_long(self):
        result = validate_dwg("DWGDWGg")
        self.assertFalse(result)

    def test_invalid_drawing_number_special_chars(self):
        result = validate_dwg("DWG-DWG")
        self.assertFalse(result)

#search_dwg
    def test_valid_drawing(self):
        drawing = load_drawings()
        result = search_dwg(drawing, "DWG-001")
        self.assertTrue(result)

    def test_invalid_drawing(self):
        drawing = load_drawings()
        result = search_dwg(drawing, "DWG-008")
        self.assertFalse(result)

    def test_empty_drawing(self):
        drawing = load_drawings()
        result = search_dwg([], "DWG-001")
        self.assertFalse(result)

    def test_expected_drawing(self): 
        drawing = load_drawings()
        expected_value = "DWG-001"
        result = search_dwg(drawing, "DWG-001")
        self.assertEqual(expected_value, result["drawing_number"])

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




    