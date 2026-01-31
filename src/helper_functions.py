#Function to encode signals
def encode(feature, code):
    '''Function to ensure that signals in features are encoded
    to the specified format
    feature - Name of feature to encode
    code - dictionary of codes to encode signals in the feature
    returns a series'''
    return data[feature].map(code)

#Function to classify scores as pass or fail
def transform_grade(x):
  if x > 9:
    return 1
  else:
    return 0


#Function to Generate Table and Graph for minority and majority class in target
def check_balance(data_series):
  a = data_series.value_counts()
  a.name = 'Figure'
  pec = (a*100 / len(data_series)).round(2)
  pec.name = 'percentage'
  a = pd.concat([a,pec], axis=1)
  display(a)
#function to Creat Graph for Dataseries
def create_bar_graph(data_series):
  sns.catplot(data=data_series.to_frame(), x='final_grade', kind='count')
  plt.title("Distribution of Final Grade in Training Data")
  plt.show()