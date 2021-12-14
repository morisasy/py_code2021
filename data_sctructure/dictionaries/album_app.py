form album import Beatles_Discography

def most_prolific(discs):
#We will store a dictionary of years
#and number of albums per year
    years = {}
    maxyears = []
    maxnumber = 0
    for disc in discs:
        year = discs[disc]
        if year in years:
            years[year] += 1
        else:
            years[year] = 1

#find the year in which the maximum
#number of albums was published
#there are more elegant ways of accomplishing this,
#but the code below works
    for year in years:
        if years[year] > maxnumber:
            maxyears=[]
            maxyears.append(year)
            maxnumber = years[year]
        elif years[year] == maxnumber and not (year in maxyears):
            maxyears.append(year)
    if (len(maxyears) == 1):
        return maxyears[0]
    else:
        return maxyears
