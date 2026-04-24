ggplot(mpg, aes(x=displ, y=hwy)) + 
  geom_point(aes(color=class)) + 
  geom_smooth(se=FALSE)

ggplot(mpg, aes(x=class)) + geom_bar()

(class_count <- dplyr::count(mpg, class))

ggplot(class_count, aes(x=class, y=n)) + geom_bar(stat="identity")

