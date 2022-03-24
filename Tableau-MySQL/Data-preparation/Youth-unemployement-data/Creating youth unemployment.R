library(tidyverse)
library(readr)
library(tidyr)
library(stringr)

setwd("~/OneDrive - UvA/VU work/Example SQL databases/CoronaImpact/Yuth unemployement")

youth_unemployment <- read_tsv("estat_ei_lmhr_m.tsv", na = ":") %>% rename(name = `freq,unit,s_adj,indic,geo\\TIME_PERIOD`)
geos <- read_csv("~/OneDrive - UvA/VU work/Example SQL databases/CoronaImpact/CountryTable/geos.csv")

youth_unemployment <- youth_unemployment %>% 
                    mutate(`2021-01` = parse_number(`2021-01`),
                           `2020-12` = parse_number(`2020-12`)) %>% 
  gather("period", "unemployment_rate", -name) %>% 
  mutate(code = substr(name, 26, length(name))) %>% 
  left_join(geos, by = c("code" = "Code")) %>% 
  mutate(id = row_number()) %>% 
  select(id, geo_id, period, unemployment_rate) %>% 
  filter(!is.na(unemployment_rate))

write_csv(youth_unemployment, "YouthUnemployment.csv")

