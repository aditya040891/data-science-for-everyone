# Importing standard plotting library
library(ggplot2)
# basic plot 1
ggplot(mpg, aes(x=displ, y=hwy)) + geom_point() + facet_wrap(~class)

# basic plot 2
ggplot(mpg, aes(x=displ, y=hwy)) + geom_point() + facet_grid(year~cyl)

# basic plot 3
ggplot(mpg, aes(x=displ, y=hwy, color=class)) + 
  geom_point() + 
  labs(title="Fuel Efficiency by Engine Power", 
       subtitle="Fuel Economy data from 1999 and 2008 for 38 popular car models",
       x = "Engine Power (litres displacement)",
       y = "Fuel Efficiency (miles per gallon)",
       color="Car Type")    

# basic plot 4
library(dplyr)

best_in_class <- mpg %>% group_by(class) %>% filter(row_number(desc(hwy))==1)

ggplot(mpg, aes(displ, hwy)) + 
  geom_point(aes(color=class)) +
  geom_label(data = best_in_class, aes(label=model), alpha=0.5)

# basic plot 4a
library(ggrepel)

ggplot(mpg, aes(displ, hwy)) + 
  geom_point(aes(color=class)) + 
  geom_text_repel(data=best_in_class, aes(label=model))

