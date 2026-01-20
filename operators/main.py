# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
spain_lang = "Castilian Spanish"
switzerland_lang = "German"
print(spain_lang == switzerland_lang)

spain_religion = "Roman Catholic"
switzerland_religion = "Roman Catholic"
print(spain_religion == switzerland_religion) 

spain_capital = "Madrid"
switzerland_capital = "Bern"
#print(len(spain_capital))
#print(len(switzerland_capital))
print(len(spain_capital) != len(switzerland_capital))

spain_gdp = 2.361 * 10**12  # in US dollars
switzerland_gdp = 741.035 * 10**9  # in US dollars
#print(spain_gdp)
#rint(switzerland_gdp)
print(switzerland_gdp>spain_gdp)

spain_popgrowth = 12/100
switzerland_popgrowth = 72/100
print(spain_popgrowth < 100/100) and (switzerland_popgrowth < 100/100)

ten_million = 10**7
#print(ten_million)
spain_popcount = 47.280 * 10**6
switzerland_popcount = 8.860 * 10**6
print(spain_popcount > ten_million) or (switzerland_popcount > ten_million)
print(spain_popcount > ten_million) and (switzerland_popcount < ten_million)
#print(spain_popcount <= ten_million) and (switzerland_popcount > ten_million)