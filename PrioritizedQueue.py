class RequirementsNotInQueue(Exception):
    """Raised when requirements of an item added to the queue
    are not present in the queue."""
    pass

class QueueManager:
    def __init__(self):
        self.items = []
        self.requirements = {}
        self.processed = []

    def addItem(self, item, requirements):
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
        return self.requirements.get(item, None)

    def printSummary(self):
        for item in self.items:
            print(f'Item: {item}')
            print('Requires:')
            reqs = self.requirements[item]
            if not reqs:
                print('No Requirements')
            else:
                for req in reqs:
                    print(req)
            print('--------------')

    def nextBatch(self):
        batch = []
        for item in self.items:
            reqs = self.requirements[item]
            ready = True
            if reqs:
                for req in reqs:
                    if req not in self.processed:
                        ready = False
                        break
            if ready and item not in self.processed:
                batch.append(item)
        return batch

    def processItem(self, item):
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
        # queue.printSummary()
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