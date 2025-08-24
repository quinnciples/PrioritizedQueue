# PrioritizedQueue

## Overview

**PrioritizedQueue** is a Python project that provides a simple way to manage and process items in a queue where each item can have dependencies (requirements) on other items. The core of the project is the `QueueManager` class, which ensures that items are only processed when all their requirements have been processed first.

## Features

- **Add Items with Requirements:** Add items to the queue, specifying dependencies on other items.
- **Dependency Validation:** Prevents adding items with requirements that are not already present in the queue.
- **Batch Processing:** Determines which items are ready to be processed based on their dependencies.
- **Processing Tracking:** Marks items as processed and keeps track of processed items.
- **Summary Printing:** Prints a summary of all items and their requirements.

## Usage

1. **Create a QueueManager Instance:**
    ```python
    queue = QueueManager()
    ```

2. **Add Items:**
    ```python
    queue.addItem('A', None)         # No requirements
    queue.addItem('B', ['A'])        # Requires 'A' to be processed first
    ```

3. **Process Items:**
    ```python
    next_batch = queue.nextBatch()
    queue.processItem(next_batch)
    ```

4. **Print Summary:**
    ```python
    queue.printSummary()
    ```

## Example

```python
queue = QueueManager()
queue.addItem('A', None)
queue.addItem('B', ['A'])
queue.addItem('C', ['A', 'B'])

while True:
    batch = queue.nextBatch()
    if not batch:
        break
    queue.processItem(batch)
```

## Exception Handling

If you try to add an item with requirements that are not present in the queue, a `RequirementsNotInQueue` exception will be raised.

## License

This project is provided for educational purposes and does not include a specific license.

## Author