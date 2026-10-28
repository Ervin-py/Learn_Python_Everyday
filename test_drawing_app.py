import unittest
from drawing_app import search_dwg, validate_dwg
from drawing_app import validate_revision
from drawing_app import validate_status

class TestValidateDwg(unittest.TestCase):

    def setUp(self):
        self.drawing = [
    {
        "drawing_number": "DWG-001",
        "name": "Shaft Assembly",
        "revision": "A",
        "status": "RELEASED"
    },
    {
        "drawing_number": "DWG-002",
        "name": "Gear Assembly",
        "revision": "B",
        "status": "WIP"
    },
    {
        "drawing_number": "DWG-003",
        "name": "Motor Assembly",
        "revision": "C",
        "status": "OBSOLETE"
    },
    {
        "drawing_number": "DWG-004",
        "name": "bracket",
        "revision": "A",
        "status": "WIP"
    }
]

#validate_dwg
    def test_valid_drawing_number(self):
        result = validate_dwg("DWG-001")
        self.assertTrue(result)

    def test_invalid_drawing_number_wrong_prefix(self):
        result = validate_dwg("ABC-001")
        self.assertFalse(result)

    def test_invalid_drawing_number_wrong_separator(self):
        result = validate_dwg("DWG/001")
        self.assertFalse(result)    

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
        result = search_dwg(self.drawing, "DWG-001")
        self.assertTrue(result)

    def test_invalid_drawing(self):
        result = search_dwg(self.drawing, "DWG-008")
        self.assertFalse(result)

    def test_empty_drawing(self):
        result = search_dwg([], "DWG-001")
        self.assertFalse(result)

    def test_expected_drawing(self): 
        expected_value = "DWG-001"
        result = search_dwg(self.drawing, "DWG-001")
        self.assertEqual(expected_value, result["drawing_number"])

#validate_revision 
    def test_valid_revision(self):
        result = validate_revision("A")
        self.assertTrue(result)

    def test_empty_revision(self):
        result = validate_revision("")
        self.assertFalse(result)

    def test_length(self):
        result = validate_revision("AA")
        self.assertFalse(result)

    def test_number(self):
        result = validate_revision("0")
        self.assertFalse(result)

    def test_special_chars_validate_revision(self):
        result = validate_revision("@")
        self.assertFalse(result)
#validate_status
    def test_valid_status_WIP(self):
        result = validate_status("WIP")
        self.assertTrue(result)

    def test_valid_status_RELEASED(self):
        result = validate_status("RELEASED")
        self.assertTrue(result)

    def test_valid_status_OBSOLETE(self):
        result = validate_status("OBSOLETE")
        self.assertTrue(result)

    def test_invalid_status(self):
        result = validate_status("kk")
        self.assertFalse(result)

    def test_special_chars_validate_status(self):
        result = validate_status("@")
        self.assertFalse(result)


    