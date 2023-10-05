#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for i in range(len(dir(hidden_4))):
        if dir(hidden_4)[i][0] == "_":
            continue
        else:
            print(f"{dir(hidden_4)[i]}")
