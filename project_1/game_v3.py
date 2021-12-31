import numpy as np

def game_core_v3(number: int=1) -> int:
    """Find guessed number and return number of attempts. Used method is dichotomy (division of search range by two) 

    Args:
        number (int, optional): guessed number. Defaults to 1.

    Returns:
        int: number of attempts
    """
    
    count = 0
    limit_a = 1
    limit_b = 101
    predict_number = np.random.randint(1, 101)
    
    while number != predict_number:  
        count += 1
        predict_number = (limit_a + limit_b) // 2    # division of search range by two
        if number > predict_number:
            limit_a = predict_number
                       
        elif number < predict_number:
            limit_b = predict_number
    
    return count


def score_game(game_core_v3) -> int:
    """What number of attemts do your algorithm guess on average for 1000 approaches 

    Args:
        game_core_v3
     ([type]): guess function

    Returns:
        int: average number of attempts 
    """
    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core_v3
    (number))
        
    score = int(np.mean(count_ls))
    
    print(f'Your algorothm guess number on average for: {score} attempts')
    return(score)


if __name__ == '__main__':  
    score_game(game_core_v3)
