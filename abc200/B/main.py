#!/usr/bin/env python3
import sys


def solve(N: int, K: int):
    for i in range(K):
        if N % 200 == 0:
            N = int(N / 200)
        else:
            N = int(str(N) + "200")
    print(N)
    return


# Generated by 2.2.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)


if __name__ == '__main__':
    main()
