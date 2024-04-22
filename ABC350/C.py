N = int(input())
inputs = input()
A = [int(i) for i in inputs.split()]
pos = [0 for i in range(N)]

for i in range(N):
  pos[A[i]-1] = i

answers = []

for i in range(N):
  if i != pos[i]:
    index = pos[i]
    A[i], A[index] = A[index], A[i]
    answers.append(str(i + 1) + " " + str(index+1))
    pos[i], pos[A[index]-1] = pos[A[index]-1], pos[i]

K = len(answers)
print(K)

for i in range(K):
  print(answers[i])
