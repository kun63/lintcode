class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        import collections
        course_dict = collections.defaultdict(set)
        indegree = collections.defaultdict(int)
        start_course = set([x for x in range(numCourses)])
        for t,u in prerequisites:
            if t not in course_dict[u]:
                indegree[t] += 1
            course_dict[u].add(t)
            if t in start_course:
                start_course.remove(t)
        # import collections
        q = collections.deque(list(start_course))
        if not q:
            return []
        path = []
        visited = set()
        # print(course_dict[0])
        while q:
            # print(q)
            c = q.pop()
            path.append(c)
            for t in course_dict[c]:
                indegree[t] -= 1
                if indegree[t] == 0:
                    q.append(t)
                    # visited.add(t)
            # if c in course_dict:
            #     for t in course_dict[c]:
            #         if t not in visited:
            #             q.append(t)
                        # visited.add(t)
        if len(path) != numCourses:
            return []
        return path

if __name__ == "__main__":
    # print(Solution().findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))
    print(Solution().findOrder(10,[[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]))
        