library(tidyverse)
library(r2d3)

library(openxlsx)

# read csv
diary <- read.xlsx("diary.xlsx",1)

# split year, month, day
diary$month <- paste(substring(diary$date, 1, 2), substring(diary$date, 7, 10), sep = "/")
#diary$day <- diary$date
diary$year <- substring(diary$date, 7, 10)


# convert "Date" into Date form
diary$Date <- as.Date(diary$date, "%m/%d/%Y")

# group by "date" and sum
diary_group <- diary %>%
  group_by(Date) %>%
  summarise(sum = n())


# r2d3 canlendar plot
r2d3plot <- r2d3(data = diary_group, d3_version = 5, container = "div", options = list(start = 2022, end = 2024), script = "d3-template.js")

# save as html
save_d3_html(r2d3plot, file = "index.html", 
             selfcontained = TRUE, libdir = NULL,
             background = "white",
             knitrOptions = list())

