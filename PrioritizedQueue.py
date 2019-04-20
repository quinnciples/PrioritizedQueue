class RequirementsNotInQueue(Exception):
    """Raised when requirements of an item added to the queue
    are not present in the queue.
    This prevents orphan requirements that are not connected
    to tasks in the queue"""
    pass


class QueueManager:

    items = []
    requirements = {}
    processed = []

    def addItem(self, item, requirements):
        if item not in self.items:
            # check that requirements also exist as items in the queue
            if isinstance(requirements, str):
                if requirements not in self.items and requirements is not None:
                    raise Exception(
                        'Attempted to add item where not all requirements are already in the queue.')
            elif isinstance(requirements, list):
                for requires in requirements:
                    if requires not in self.items and requires is not None:
                        raise Exception(
                            'Attempted to add item where not all requirements are already in the queue.')

            self.items.append(item)
            self.requirements[item] = requirements

    def getRequirements(self, item):
        if item in self.items:
            return self.requirements[item]
        else:
            return None

    def printSummary(self):
        for item in self.items:
            print('Item: ' + item)
            print('Requires')
            if self.requirements[item] == None:
                print('No Requirements')
            else:
                for requires in self.requirements[item]:
                    print(requires)
            print('--------------')

    def nextBatch(self):
        batch = []
        for item in self.items:
            #ready = True
            if self.requirements[item] == None:
                ready = True
            else:
                ready = True
                changed = False
                for requires in self.requirements[item]:
                    if requires not in self.processed and changed == False:
                        ready = False
                        changed = True
            if ready == True:
                if item not in self.processed:
                    batch.append(item)
        return batch

    def processItem(self, item):
        if isinstance(item, str):
            self.processed.append(item)
            print('Processing: ' + item)
        elif isinstance(item, list):
            for newitem in item:
                self.processed.append(newitem)
                print('Processing: ' + newitem + ' ', end="\n")
        print(end="\n")



try:
    queue = QueueManager()
    import string
    import random
    charset = string.ascii_uppercase + string.ascii_lowercase

    for i in list(charset):
        task_name = i
        if random.random() < 0.05 or i == list(charset)[0]:
            requirements = None
        else:
            requirements = [r for r in charset if r < i and random.random() <= 0.2]

        queue.addItem(i, requirements)

    nextBatch = queue.nextBatch()
    #queue.printSummary()
    while len(nextBatch) > 0:
        print('Next Batch ' + str(nextBatch))
        queue.processItem(nextBatch)
        nextBatch = queue.nextBatch()

except Exception as e:
    print(e)

finally:
    print('Done.')
