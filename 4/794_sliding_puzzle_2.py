class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """

    def minMoveStep(self, init_state, final_state):
        # # write your code here
        import copy
        from collections import deque

        def inreachable(state):
            p = None
            for i in range(3):
                if p != None:
                    break
                for j in range(3):
                    if state[i][j] == 0:
                        p = (i, j)
                        break
            i_0, j_0 = p
            outcome = set()
            p_i = {0, 1, 2}
            p_j = {0, 1, 2}
            p_i.remove(i_0)
            p_j.remove(j_0)
            a, b = p_i
            temp = copy.deepcopy(state)
            v = temp[a][j]
            temp[a][j] = temp[b][j]
            temp[b][b] = v
            outcome.add(str(temp))
            a, b = p_j
            temp = copy.deepcopy(state)
            v = temp[i][a]
            temp[i][a] = temp[i][b]
            temp[i][b] = v
            outcome.add(str(temp))

            return outcome

        def transf_state(state):
            p = state.index('0')
            # for i in range(3):
            #     if p != None:
            #         break
            #     for j in range(3):
            #         if state[i][j] == 0:
            #             p = (i, j)
            #             break
            i, j = p//3, p%3
            temp_ps = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            next_ps = []
            outcome = []
            for t in temp_ps:
                a, b = t
                if a >= 0 and b >= 0 and a <= 2 and b <= 2:
                    next_ps.append((a, b))
            for a, b in next_ps:
                temp = list(state)
                new_p = 3*a+b
                v = temp[new_p]
                temp[new_p] = temp[p]
                temp[p] = v
                # temp[3*i+j], temp[p] = temp[p], temp[3*i+j]
                # a_0, b_0 = p
                # temp = copy.deepcopy(state)
                # temp[a_0][b_0] = temp[a][b]
                # temp[a][b] = 0
                temp = ''.join(temp)
                if temp not in visited:
                    outcome.append(temp)
            return outcome

        visited = set()
        # visited_in = set()
        temp_ = ''
        for e in init_state:
            temp = ''.join([str(x) for x in e])
            temp_ += temp
        init_state = temp_
        temp_ = ''
        for e in final_state:
            temp = ''.join([str(x) for x in e])
            temp_ += temp
        final_state = temp_
        q = deque([init_state])
        step = -1
        while q:
            step += 1
            for _ in range(len(q)):
                temp_state = q.popleft()
                visited.add(temp_state)
                if temp_state == final_state:
                    return step
                # next_inreach = inreachable(temp_state)
                # if str(final_state) in next_inreach:
                #     return -1
                next_states = transf_state(temp_state)
                # for ns in next_states:
                #     visited.add(ns)
                visited.update(next_states)
                q.extend(next_states)
        print(len(visited))
        return -1

    def _minMoveStep(self, init_state, final_state):
        st, ed = "", ""
        S, q = set(), []
        fx = [0, 0, 1, -1]
        fy = [1, -1, 0, 0]
        for i in range(3):
            for j in range(3):
                st += str(init_state[i][j])
                ed += str(final_state[i][j])
        q.append(st)
        S.add(st)
        dep = 0
        while len(q) > 0:
            siz = len(q)
            for i in range(siz):
                now = q[i]
                if(now == ed):
                    return dep
                pos = now.find('0')
                x, y = pos // 3, pos % 3
                for j in range(4):
                    nx, ny = x + fx[j], y + fy[j]
                    if(nx < 0 or nx >= 3 or ny < 0 or ny >= 3):
                        continue
                    tpos = 3 * nx + ny
                    a, b = max(tpos, pos), min(tpos, pos)
                    now = now[0:b] + now[a] + \
                        now[b + 1:a] + now[b] + now[a + 1:]
                    if(not now in S):
                        q.append(now)
                        S.add(now)
                    now = now[0:b] + now[a] + \
                        now[b + 1:a] + now[b] + now[a + 1:]
            for i in range(siz):
                q.pop(0)
            dep += 1
        print(len(S))
        return -1


if __name__ == "__main__":
    # a = [[2,8,3],[1,0,4],[7,6,5]]
    # b = [[1,2,3],[8,0,4],[7,6,5]]
    a = [[5, 7, 3], [8, 4, 6], [2, 1, 0]]
    b = [[5, 7, 3], [8, 4, 6], [1, 2, 0]]
    # b = [[1,8,3],[6,5,4],[7,2,0]]
    print(Solution().minMoveStep(a, b))
