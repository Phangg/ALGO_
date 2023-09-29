def solution(today, terms, privacies):
    answer = []
    
    today = list(map(int, today.split(".")))
    
    # terms -> term_dict
    term_dict = {}
    for t in terms:
        tmp_arr = t.split(" ")
        term_dict[tmp_arr[0]] = int(tmp_arr[1])
    
   # privacies split
    for (index, privacy) in enumerate(privacies):
        tmp_arr = privacy.split(" ")
        contract_date = list(map(int, tmp_arr[0].split(".")))
        terms_type = tmp_arr[1]
        
        print("b:   ", today, contract_date, terms_type)
        
        # check possible date
        contract_date[1] += term_dict[terms_type]
        if contract_date[1] > 12:
            q, r = divmod(contract_date[1], 12)
            if r == 0:
                contract_date[1] = 12
                contract_date[0] += (q - 1)
            else:
                contract_date[1] = r
                contract_date[0] += q
        
        contract_date[2] -= 1
        if contract_date[2] == 0:
            contract_date[2] = 28
            contract_date[1] -= 1
            if contract_date[1] == 0:
                contract_date[1] = 12
                contract_date[0] -= 1
        
        # check answer
        if today[0] > contract_date[0]:
            answer.append(index + 1)
        elif today[0] == contract_date[0] and today[1] > contract_date[1]:
            answer.append(index + 1)
        elif today[0] == contract_date[0] and today[1] == contract_date[1] and today[2] > contract_date[2]:
            answer.append(index + 1)
    
        print("a:   ", today, contract_date, terms_type)
    return answer