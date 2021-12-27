import numpy as np

def random_predict(number: int=1) -> int:
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # estimated number
    
        if number == predict_number:
            break # exit if number is guessed
    return count


def score_game(random_predict) -> int:
    """What number of attemts do your algorithm guess on average for 1000 approaches 

    Args:
        random_predict ([type]): guess function

    Returns:
        int: average number of attempts 
    """
    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f'Your algorothm guess number on average for: {score} attempts')
    return(score)

if __name__ == '__main__':  
    # RUN
    score_game(random_predict)

# print(f"Count of attemts: {random_predict()}")