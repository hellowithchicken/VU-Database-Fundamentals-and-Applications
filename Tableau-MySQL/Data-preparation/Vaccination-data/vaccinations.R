library(tidyverse)
library(readr)
library(lubridate)

setwd("~/OneDrive - UvA/VU work/Example SQL databases/CoronaImpact/Vaccination data")

data <- read_csv("data.csv") %>% filter(ReportingCountry != "LI")

vaccineNames <- as.data.frame(unique(data$Vaccine))

# vaccines table

vaccineNames <- vaccineNames %>% 
  rename(vaccine = `unique(data$Vaccine)`) %>% 
  arrange(vaccine) %>% 
  mutate(id = row_number()) %>% 
  select(id, vaccine) %>% 
  write_csv("vaccines.csv")

# add vaccine target population to countries table

geos <- read_csv("~/OneDrive - UvA/VU work/Example SQL databases/CoronaImpact/CountryTable/geos.csv")
target_populations <- data %>% 
  filter(ReportingCountry == Region,
         TargetGroup == "ALL") %>%
  select(ReportingCountry, Denominator) %>% 
  distinct_all()

geos <- geos %>% 
  select(-X1) %>%
  full_join(target_populations, by = c("Code" = "ReportingCountry")) %>% 
  rename(vaccine_population = Denominator) %>% 
  write_csv("~/OneDrive - UvA/VU work/Example SQL databases/CoronaImpact/CountryTable/geos_withpop.csv", na = "NULL")
  

# prepare the main vaccination table

dataFordb <- data %>% 
  filter(TargetGroup == "ALL") %>% 
  left_join(vaccineNames, by = c("Vaccine" = "vaccine")) %>% 
  rename(vaccine_id = id) %>% 
  filter(ReportingCountry == Region) %>% 
  left_join(geos, by = c("ReportingCountry" = "abbrv")) %>% 
  select(geo_id, vaccine_id, FirstDose, SecondDose, NumberDosesReceived, YearWeekISO) %>% 
  mutate(Year = substr(YearWeekISO, 1, 4),
         Week = substr(YearWeekISO, 7,8),
         date = as.Date(paste(Year, Week, 1, sep="-"), "%Y-%U-%u")) %>% 
  mutate(date = date - 3) %>% 
  mutate(date = case_when(
    Week == 52 ~ as.Date("2020-12-18"),
    Week == 53 ~ as.Date("2020-12-25"),
    TRUE ~ date
  )) %>% 
  select(geo_id, vaccine_id, FirstDose, SecondDose, NumberDosesReceived, week_start = date) %>% 
  arrange(week_start, geo_id, vaccine_id) %>% 
  mutate(id = row_number()) %>% 
  select(id, geo_id, vaccine_id, FirstDose, SecondDose, NumberDosesReceived, week_start) %>% 
  write_csv("vaccinationRollOut.csv", na = "NULL")

