library(ggplot2) # importing the library
library(pillar)

?ggplot2 # Documentation

# Do cars with big engines use more fuel than cars with small engines?
mpg
unique(mpg$manufacturer) # unique values of manufacturer column

ggplot2::mpg

# mpg: displ, car's engine size, litres
# mpg: hwy, fuel efficiency on the highway (miles per gallon or mpg)

# Creating ggplot

ggplot(data = mpg) + geom_point(mapping=aes(x=displ, y=hwy))

# ggplot(data = DATASET) + GEOM_FUNCTION(mappings=aes(MAPPINGS))

glimpse(mpg)

# displ, hwy, class
# aesthetic: visual property; Ex. size , color, shape

ggplot(data=mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy, color = class))

ggplot(data=mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy, color = class))

ggplot(data=mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy), color="blue")






