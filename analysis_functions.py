def Cohen_d(group1, group2):

    # Compute Cohen's d.

    # group1: Series or NumPy array
    # group2: Series or NumPy array

    # returns a floating point number 

    diff = np.mean(group1) - np.mean(group2)

    n1, n2 = len(group1), len(group2)
    var1 = np.var(group1)
    var2 = np.var(group2)

    # Calculate the pooled threshold as shown earlier
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    
    # Calculate Cohen's d statistic
    d = diff / np.sqrt(pooled_var)
    
    return d
    
    
 def create_metro_dataset(series):
    metro_dataset = clean_data.loc[clean_data['CSI'] == '1'][series]
   
    return metro_datase
    
def create_non_metro_dataset(series):
    non_metro_dataset = clean_data.loc[clean_data['CSI'] != '1'][series]
    return non_metro_dataset
    
def plot_distribution(data1, label1, data2,label2):
    sns.distplot(data1, label=str(label1))
    sns.distplot(data2 , label=str(label2))
    plt.legend()
    
def get_sample_means(data,sample_size):
    means = []
    for i in range(0,100000):
        a_mean = np.mean(np.random.choice(data, size=sample_size))
        means.append(a_mean)
    return means
    
    