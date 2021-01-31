def matrix_fill(list_1d):
    row, column = int(list_1d[0]), int(list_1d[1])
    matrix = [[0.0 for x in range(column)] for y in range(row)]
    counter = 2
    for row_counter in range(row):
        for column_counter in range(column):
            matrix[row_counter][column_counter] = list_1d[counter]
            counter += 1
    return matrix



def computeDelta():
    for t in range(T):
        for i in range(Nstates):
            if t==0:
                delta[t][i]= emissions_matrix[i][obs_sequence[t+1]]*pi[i+2]
            else:
                index, max_val = -1, -1
                for j in range(Nstates):
                    product = state_trans_matrix[j][i]* delta[t-1][j] * emissions_matrix[i][obs_sequence[t+1]]
                    if product > max_val:
                        index, max_val = j, product
                delta[t][i]= max_val
                deltaIdx[t][i]= index




inp = input().strip().split(" ")
state_list = list(map(float, inp))
state_trans_matrix = matrix_fill(state_list)
Nstates= len(state_trans_matrix)
inp = input().strip().split(" ")
emissions_list = list(map(float, inp))
emissions_matrix = matrix_fill(emissions_list)
inp = input().strip().split(" ")
pi = list(map(float, inp))
inp = input().strip().split(" ")
obs_sequence = list(map(int, inp))
T = obs_sequence[0]
delta = [[0.0 for j in range(Nstates)] for i in range(T)]
deltaIdx = [[0 for a in range(Nstates)] for b in range(T)]
final_state_seq = [0 for x in range(obs_sequence[0])]
computeDelta()
max_idx, delta_max = -1, -1
for j in range(Nstates):
    delta_temp = delta[T - 1][j]
    if delta_temp > delta_max:
        delta_max = delta_temp
        max_idx = j
final_state_seq[-1]= max_idx
idx = max_idx
for jdx in range(2,T+1):
    final_state_seq[-jdx] = deltaIdx[-jdx+1][idx]
    idx = final_state_seq[-jdx]

print(' '.join(map(str, final_state_seq)))


