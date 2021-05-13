#!/usr/bin/env python3
import sys


def solve(N: int, S: "List[str]"):
    registerd = set()
    for i in range(len(S)):
        s = S[i]
        if not(s in registerd):
            print(i + 1)
            registerd.add(s)
    return


# Generated by 2.2.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)


if __name__ == '__main__':
    main()
