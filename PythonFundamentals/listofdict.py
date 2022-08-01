results = [
    {"district":"tvm","win": 98, "A+": 45000},
    {"district":"ktm","win": 95, "A+": 44000},
    {"district":"apy","win": 97, "A+": 47000},
    {"district":"idk","win": 90 ,"A+": 38000},
    {"district":"ekm","win": 99, "A+": 56000},
    {"district":"pta","win": 99, "A+": 58000},
    {"district":"tsr","win": 98, "A+": 57000},
    {"district":"kzd","win": 99, "A+": 58000},
    {"district":"pkd","win": 95, "A+": 50000},
    {"district":"mpm","win": 90, "A+": 4500},

]

#win % of tvm

# for result in results:
#     if result["district"]=="tvm":
#         print(result["win"])

# using list comprehension

# tvm_win=[result["win"]for result in results if result["district"]=="tvm"]
# print(tvm_win)


print([res["win"]for res in results if res["district"]=="tvm"])

#district with highest win %

print(max(results,key=lambda res:res['win']))

#district with lowest win %

print(min(results,key=lambda res:res['win']))

#district with highest A+

print(max(results ,key=lambda res:res ["A+"]))

#district with lowest A+

print(min(results ,key=lambda res:res ["A+"]))


# total no of win %

win_tot=sum([result["win"]for result in results])
print(win_tot)


#total no of A+

aplus=sum([result["A+"]for result in results])
print(aplus)


# sort the dic wid win % order by ascending order

# def get_win(res):
#     return res["win"]
# results.sort(key=get_win,reverse=True)
# print(results)

results.sort(key=lambda res:res["win"],reverse=True)
print(results)
