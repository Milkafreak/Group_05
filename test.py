import numpy as np
import pandas as pd 

def fun1(a: float = 1.0) -> np.ndarray:
    """
    """
    return np.zeros(10) + a

def fun2(a: float = 1.0) -> pd.DataFrame:
    """
    """
    # initialize list of lists
    data = [['tom', 10], ['nick', 15], ['juli', 14]]
 
    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns = ['Name', 'Age'])
    
    df['age_m'] = df['Age'] * a
    
    return df
    


fun1(2)

fun2(2)