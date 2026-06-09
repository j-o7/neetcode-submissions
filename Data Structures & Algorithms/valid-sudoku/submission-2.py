class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # horizontals = [[] for _ in range(9)]
        verticals = [[] for _ in range(9)]
        grids = [[] for _ in range(9)]
        # print(horizontals)
        # print(verticals)
        # print(grids)

        hi = 0
        # vi = 0
        # gi = 0
        for i, hor in enumerate(board):
            # horizontals[i] = board[i]

            vi = 0

            for j, vert in enumerate(hor):
                verticals[vi].append(vert)
                grid_row = i // 3
                grid_col = j // 3

                grid_idx = grid_row * 3 + grid_col
                grids[grid_idx].append(vert)

                vi += 1


        # print(grids)
        # print(horizontals)
        # print(verticals)
        
        for i in range(9):
            hor_set = set()
            ver_set = set()
            grid_set = set()

            hor = board[i]
            ver = verticals[i]
            grid = grids[i]

            for j in range(9):
                if hor[j] != '.':
                    if hor[j] in hor_set:
                        return False
                    hor_set.add(hor[j])

                if ver[j] != '.':
                    if ver[j] in ver_set:
                        return False
                    ver_set.add(ver[j])

                if grid[j] != '.':
                    if grid[j] in grid_set:
                        return False
                    grid_set.add(grid[j])

        return True