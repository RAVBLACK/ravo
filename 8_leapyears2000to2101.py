#8)Write a program to display all leap year from 2000 to 2101?
for year in range(2000, 2102):
	if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
		print(year)

#output:
# 2000
# 2004
# 2008
# 2012
# 2016	
# 2020
# 2024
# 2028
# 2032
# 2036
# 2040
# 2044
# 2048
# 2052
# 2056
# 2060
# 2064
# 2068
# 2072
# 2076
# 2080
# 2084
# 2088
# 2092
# 2096
# 2100
# 2101
# 2101 is not a leap year.