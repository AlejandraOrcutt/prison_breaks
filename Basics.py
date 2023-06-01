#!/usr/bin/env python
# coding: utf-8

# # Analyzing Data

# ## Prison Helicopter Escapes 

# ### The questions to be answered are:
#     1)In which year did the most helicopter prison break attempts occur?
#     2)In which countries do the most attempted helicopter prison breaks occur?

# We begin by importing some helper functions.

# In[1]:


from helper import *


# ## Getting the Data

# We are getting the data from the [List of helicopter prison escapes](https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article.

# In[ ]:


url = "https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes"
data = data_from_url(url)


# Let's print the first three rows

# In[3]:


for row in data[:3]:
    print(row)


# We removed the last column which has details and occupies to much space

# In[4]:


index = 0
for row in data:
    data[index] = row[:-1]
    index += 1


# In[5]:


print(data[:3])


# We are going to replace the first row with just the year using the fetch-year() function

# In[6]:


for row in data:
    year = fetch_year(row[0])
    row[0] = year


# In[7]:


print(data[:3])


# ## Attempts per Year I

# We are using the lambda function to find min and max year 

# In[8]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]


# In[9]:


print(min_year)
print(max_year)


# Now we'll create a list of all the years ranging from min_year to max_year. Our goal is to then determine how many prison break attempts there were for each year. Since years in which there weren't any prison breaks aren't present in the dataset, this will make sure we capture them.

# In[10]:


years = []
for year in range(min_year, max_year + 1):
    years.append(year)


# In[11]:


print(years)


# Next, we have to find out how many attempts were done per year

# We will write a loop to iterate over a list of years. For each year, a new list is created with two elements: the year itself and the initial value of 0. This new list is then appended to the attempts_per_year list.

# In[12]:


attempts_per_year = []
for year in years:
    attempts_per_year.append([year, 0])


# In the next block of code, the outer loop for row in data: iterates over each element row in the data list containing a list of records.
# 
# The inner loop for year_attempt in attempts_per_year: iterates over each element year_attempt in the attempts_per_year list. attempts_per_year is a list of lists, where each inner list represents a year and its corresponding attempt count.
# 
# The line year = year_attempt[0] assigns the first element of the year_attempt list (which represents a year) to the variable year.
# 
# The if statement if row[0] == year: checks if the first element of the current row matches the year. This is done to find the corresponding year in the attempts_per_year list.
# 
# If the condition is True, meaning the year of the row matches the current year_attempt, the code block inside the if statement is executed.
# 
# In the line year_attempt[1] += 1, it increments the second element of the year_attempt list (which represents the attempt count) by 1. This increases the attempt count for the corresponding year.
# 
# After the loops complete, the line print(attempts_per_year) is used to display the updated attempts_per_year list, showing the year and its updated attempt count.
# 
# In summary, this loop iterates over each row in the data list, matches the year with the corresponding element in the attempts_per_year list, and increments the attempt count for that year. Finally, it prints the updated attempts_per_year list.

# In[13]:


for row in data:
    for year_attempt in attempts_per_year:
        year = year_attempt[0]
        if row[0] == year:
            year_attempt[1] += 1            


# In[14]:


print(attempts_per_year)


# ## Attempts per Year II

# In[15]:


for row in data:
    for year_attempt in attempts_per_year:
        # assign the year value in year_attempt to year
        if row[0] == year:
            year_attempt[1] += 1


# In[16]:


print(attempts_per_year)


# ## Attempts per Year III
# 

# In[17]:


### In which year did the most attempts at breaking out of prison with a helicopter occur?


# In[18]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# ## Attempts by Country

# ### In which countries do the most attempted helicopter prison escapes occur?

# In[19]:


countries_frequency = df["Country"].value_counts()


# In[20]:


print_pretty_table(countries_frequency)


# ## Conclusion
# 1)  In which year did the most helicopter prison break attempts occur? 1986, 2001, 2007 and 2009
# 

# 2)  In which countries do the most attempted helicopter prison breaks occur? 
# France
