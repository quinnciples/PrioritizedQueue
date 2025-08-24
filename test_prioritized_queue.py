import unittest
from PrioritizedQueue import QueueManager, RequirementsNotInQueue

class TestQueueManager(unittest.TestCase):
    def setUp(self):
        self.qm = QueueManager()

    def test_add_item_no_requirements(self):
        self.qm.addItem('A', None)
        self.assertIn('A', self.qm.items)
        self.assertIsNone(self.qm.getRequirements('A'))

    def test_add_item_with_requirements(self):
        self.qm.addItem('A', None)
        self.qm.addItem('B', ['A'])
        self.assertIn('B', self.qm.items)
        self.assertEqual(self.qm.getRequirements('B'), ['A'])

    def test_add_item_with_missing_requirement_raises(self):
        with self.assertRaises(RequirementsNotInQueue):
            self.qm.addItem('B', ['A'])

    def test_next_batch_no_requirements(self):
        self.qm.addItem('A', None)
        self.qm.addItem('B', None)
        batch = self.qm.nextBatch()
        self.assertIn('A', batch)
        self.assertIn('B', batch)

    def test_next_batch_with_requirements(self):
        self.qm.addItem('A', None)
        self.qm.addItem('B', ['A'])
        self.qm.processItem('A')
        batch = self.qm.nextBatch()
        self.assertIn('B', batch)
        self.assertNotIn('A', batch)

    def test_process_item_str(self):
        self.qm.addItem('A', None)
        self.qm.processItem('A')
        self.assertIn('A', self.qm.processed)

    def test_process_item_list(self):
        self.qm.addItem('A', None)
        self.qm.addItem('B', None)
        self.qm.processItem(['A', 'B'])
        self.assertIn('A', self.qm.processed)
        self.assertIn('B', self.qm.processed)

    def test_print_summary(self):
        self.qm.addItem('A', None)
        self.qm.addItem('B', ['A'])
        # Just ensure it runs without error
        self.qm.printSummary()

if __name__ == '__main__':
    unittest.main()