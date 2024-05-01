import unittest
from console import HBNBCommand

class TestConsoleCreate(unittest.TestCase):
    def test_missing_class_name(self):
        console = HBNBCommand()
        console.do_create("")
        self.assertEqual(console.stdout.getvalue().strip(), "** class name missing **")

    def test_nonexistent_class_name(self):
        console = HBNBCommand()
        console.do_create("NonExistentClass")
        self.assertEqual(console.stdout.getvalue().strip(), "** class doesn't exist **")

    def test_create_object(self):
        console = HBNBCommand()
        console.do_create("State name=\"California\"")
        output = console.stdout.getvalue().strip()
        self.assertTrue(output.startswith("b") and len(output) == 36)  # Check if ID is printed

    def test_invalid_parameters(self):
        console = HBNBCommand()
        console.do_create("State name=\"California\" invalid_param=123")
        self.assertEqual(console.stdout.getvalue().strip(), "b90e3c27-bd4e-49b1-b82f-70b8f1e3f8a3")


if __name__ == '__main__':
    unittest.main()
