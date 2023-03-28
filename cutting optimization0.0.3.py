import random
import itertools

# 0 - 30 ok
# 30 - 80 ne
# 80 < ok
class CuttingOptimization():
    def buy_stock(stock_items,requested_items,size):
        
        print("\n\n\nRemaining stock items:",stock_items)
        print("Remaining requested items:",requested_items)
        print("Standard size of stock:",size)
        print("END")
        all_possible_combinations = []
        for L in range(len(requested_items) + 1):
            for subset in itertools.combinations(requested_items, L):
                if subset == ():
                    pass
                else:
                    all_possible_combinations.append(subset)
        # for i in all_possible_combinations:
        #     if i == ():
        #         all_possible_combinations.remove(i)

        print("All possible combinations: ",all_possible_combinations)

        # return stock_items

    
        
    def best_combination(list1,list2):
        stock_items = list1
        requested_items = list2

        all_possible_combinations = []
        sum_of_all_possible_combinations = []
        all_sum_and_combinations = []
        cutting_coeficient_list = []
        all_items_combinations_coeficient = []
        cutting_coeficient_list = []
        all_items_combinations_coeficient = []
        specific_size = []

        stock_items.sort()
        requested_items.sort()
        
        

        for L in range(len(requested_items) + 1):
            for subset in itertools.combinations(requested_items, L):
                all_possible_combinations.append(subset)

        for i in all_possible_combinations:
            if i == ():
                all_possible_combinations.remove(i)

        for i in range(len(all_possible_combinations)):
            if len(all_possible_combinations[i]) == 1:
                blade_witdh = 0.003
            else:
                blade_witdh = 0.003 * (len(all_possible_combinations[i])-1)
            sum_of_all_possible_combinations.append(round(sum(all_possible_combinations[i])+blade_witdh,5))

        for i,j in zip(sum_of_all_possible_combinations,all_possible_combinations):
            all_sum_and_combinations.append((i,j))

        for i in stock_items:
            for j,z in all_sum_and_combinations:
                if i >= j:
                    cutting_coeficient_list.append(i-j)
                    all_items_combinations_coeficient.append((i-j,z,i,j))
                    pass
                else:
                    break
        all_items_combinations_coeficient_sorted = sorted(all_items_combinations_coeficient, key=lambda x: x[0])
        
        for i in all_items_combinations_coeficient:
            if i[0] < 0.3 or i[0] > 0.8:
                specific_size.append(i)
        # print("All possible combinations: ",specific_size)
        
        all_items_combinations_coeficient_sorted = sorted(specific_size, key=lambda x: x[0])
            

        try:
            best_result = all_items_combinations_coeficient_sorted[0]
            # print("possible combinations: ",len(all_items_combinations_coeficient_sorted))
            stock = best_result[2]
            request = best_result[1]
            boolen = True
            for i in stock_items:
                if i == stock:
                    stock_items.remove(i)
                    break
                else:
                    pass
            for i in requested_items:
                for j in request:
                    if i == j:
                        requested_items.remove(i)
                        break
                    else:
                        pass
            if len(requested_items) == 0:
                perfect_result = True
            else:
                perfect_result = False
            return stock_items,requested_items,best_result,boolen,perfect_result
        except IndexError:
            # print("Buy more stock")
            best_result = "Buy more stock"
            boolen = False
            perfect_result = False
            return stock_items,requested_items,best_result,boolen,perfect_result
                # pass

    
    def minimal_waste(stock_items,requested_items,size):
        while True: 
            result = CuttingOptimization.best_combination(stock_items,requested_items)
            
            if result[3] == True and result[4] != True:
                print(result)
                
                continue
            elif result[4] == True:
                print("No need to buy stock")
                print(result)
                # print("Perfect result")
                break
            elif result[4] == False and result[3] == False and ((result[2] == "No solution") or (result[2] == "Buy more stock")):
                # print(all_items_combinations_coeficient_sorted)
                z = CuttingOptimization.buy_stock(result[0],result[1],size)
                break
            else:
                break


stock_items = []
for i in range(10):
    stock_items.append(round((random.uniform(1,4)-0.2),2))

requested_items = []
for i in range(10):
    requested_items.append(round(random.uniform(1,4),2))

print(stock_items)
print(requested_items)
print("=" * 30)
result = CuttingOptimization.minimal_waste(stock_items,requested_items,6)
