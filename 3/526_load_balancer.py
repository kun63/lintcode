class LoadBalancer:

    cluster = set()
    def __init__(self):
        # do intialization if necessary
        pass

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        self.cluster.add(server_id)

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        self.cluster.remove(server_id)

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        outcome = self.cluster.pop()
        self.cluster.add(outcome)
        return outcome
if __name__ == "__main__":
    l = LoadBalancer()
    l.add(1)
    l.add(2)
    l.add(3)
    l.pick()
    l.pick()
    l.pick()
    l.pick()
    l.remove(1)
    l.pick()
    l.pick()
    l.pick()