from sklearn.model_selection import train_test_split

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x, y = train_test_split(list, test_size=2, shuffle=False)

print(y)