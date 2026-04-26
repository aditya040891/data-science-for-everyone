library(tidyverse)

# diamonds
glimpse(diamonds)

ggplot(data = diamonds) + 
  geom_bar(mapping = aes(x = cut))

?stat_count

count(diamonds, var=cut)

dplyr::count(diamonds, var=cut)

df <- count(diamonds, var=cut)

ggplot(data = df) +
  geom_bar(mapping = aes(x = var, y = n), stat = "identity")

df

ggplot(data = diamonds) + 
  stat_summary(
    mapping = aes(x = cut, y = depth),
    fun.min = min,
    fun.max = max,
    fun = median
  )
  
ggplot(data = diamonds) + 
  geom_boxplot(mapping = aes(x = cut))

ggplot(data = df) + 
  geom_boxplot(mapping = aes(x=var, y=n))


  
  