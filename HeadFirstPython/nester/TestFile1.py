movies=["a","b","c"]
print(movies)
print(len(movies))
movies.append("d")
print(movies)
movies.pop()
print(movies)
movies.extend(["e","f"])
print(movies)
movies.remove("b")
print(movies)
movies.insert(2,"l")
print(movies)


for i in movies:
    print(i)