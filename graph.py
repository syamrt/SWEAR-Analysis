
import matplotlib.pyplot as plt
def plotg(aca,ver,quan): 
    left=[1,2,3] 
    height = [aca,ver,quan] 
    tick_label = ['Academic', 'Verbal', 'Quantitative'] 
    plt.bar(left, height, tick_label = tick_label, 
            width = 0.2, color = ['red', 'green']) 
    plt.xlabel('Field') 
    plt.ylabel('Percentage(%)') 
    plt.title('Analysis') 
    plt.show()
    
    


