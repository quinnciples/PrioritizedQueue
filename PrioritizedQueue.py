class RequirementsNotInQueue(Exception):
    """Raised when requirements of an item added to the queue
    are not present in the queue."""
    pass

class QueueManager:
    def __init__(self):
        """
        Initializes a new QueueManager instance.

        Attributes:
            items (list): List of items in the queue.
            requirements (dict): Mapping of item to its requirements.
            processed (list): List of processed items.
        """
        self.items = []
        self.requirements = {}
        self.processed = []

    def addItem(self, item, requirements):
        """
        Adds an item to the queue with its requirements.

        Args:
            item (str): The item to add.
            requirements (list, str, or None): Requirements for the item.
                Can be None, a string, or a list of strings.

        Raises:
            RequirementsNotInQueue: If any requirement is not already in the queue.
        """
        if item in self.items:
            return
        # Normalize requirements to list or None
        if requirements is None:
            reqs = []
        elif isinstance(requirements, str):
            reqs = [requirements]
        else:
            reqs = list(requirements)
        # Check requirements exist
        for req in reqs:
            if req not in self.items and req is not None:
                raise RequirementsNotInQueue(
                    f"Requirement '{req}' for item '{item}' not in queue."
                )
        self.items.append(item)
        self.requirements[item] = reqs if reqs else None

    def getRequirements(self, item):
        """
        Retrieves the requirements for a given item.

        Args:
            item (str): The item to query.

        Returns:
            list or None: The requirements for the item, or None if none exist.
        """
        return self.requirements.get(item, None)

    def printSummary(self):
        """
        Prints a summary of all items in the queue and their requirements.
        """
        for item in self.items:
            print(f'Item: {item}')
            print('Requires:')
            reqs = self.requirements[item]
            if not reqs:
                print('No Requirements')
            else:
                #for req in reqs:
                    #print(req)
                print(', '.join(reqs))
            print('--------------')

    def nextBatch(self):
        """
        Determines the next batch of items that are ready to be processed.

        Returns:
            list: Items whose requirements have all been processed and are not yet processed.
        """
        batch = []
        for item in self.items:
            # reqs = self.requirements[item]
            
            # ready = True
            # if reqs:
            #     for req in reqs:
            #         if req not in self.processed:
            #             ready = False
            #             break

            ready = all(req in self.processed for req in self.requirements[item]) if self.requirements[item] else True

            if ready and item not in self.processed:
                batch.append(item)
        return batch

    def processItem(self, item):
        """
        Marks an item or a list of items as processed and prints their names.

        Args:
            item (str or list): The item or list of items to process.
        """
        if isinstance(item, str):
            self.processed.append(item)
            print(f'Processing: {item}')
        elif isinstance(item, list):
            for newitem in item:
                self.processed.append(newitem)
                print(f'Processing: {newitem}')
        print()

if __name__ == "__main__":
    try:
        queue = QueueManager()
        import string
        import random
        charset = string.ascii_uppercase + string.ascii_lowercase

        for i in charset:
            if random.random() < 0.05 or i == charset[0]:
                requirements = None
            else:
                requirements = [r for r in charset if r < i and random.random() <= 0.2]
            queue.addItem(i, requirements)

        nextBatch = queue.nextBatch()
        queue.printSummary()
        while nextBatch:
            print('Next Batch', nextBatch)
            queue.processItem(nextBatch)
            nextBatch = queue.nextBatch()

    except RequirementsNotInQueue as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print('Done.')