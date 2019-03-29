# This is an implementation of coin change problem using
# bottom up dynamic programming.
# Problem statement: given a set of coins of different values
# and an amount to make up, find number of different ways to
# make up the amount using given set of unlimited supply of 
# coins from the given set.

def coin_change(amount, coins):
    # if amount is less than 0, return 0.
    if amount < 0:
        return 0

    # construct the results list to store lower valued results 
    ways = [0 for i in range(0, amount + 1)]
    # there is one way to make amount 0
    ways[0] = 1
    # start filling the table from 1 to amount
    for i in range(1, amount + 1):
        # for each coin if the amount is greater than
        # coin's value, compute ways[i] from lower terms
        for c in coins:
            if i >= c:
                ways[i] += ways[i-c]
    #return final value
    return ways[amount]

def main():
    coins = [1, 2, 5]
    amount = 4
    print("different ways to make ",
        amount, " is ", coin_change(amount, coins))

if __name__ == "__main__":
    main()