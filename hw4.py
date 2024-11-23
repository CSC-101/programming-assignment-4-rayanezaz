import sys
import build_data

fullData = build_data.get_data()

def percent(line, less):
    perc = 0
    program = line[1].split(".")
    if program[0] == "Education":
        if len(less) == 0:
            for county in fullData:
                try:
                    perc += county.education[program[1]]
                except KeyError:
                    print("Invalid Key")
                    return
        else:
            for county in less:
                try:
                    perc += county.education[program[1]]
                except KeyError:
                    print("Invalid Key")
                    return
    elif program[0] == "Ethnicities":
        if len(less) == 0:
            for county in fullData:
                try:
                    perc += county.ethnicities[program[1]]
                except KeyError:
                    print("Invalid Key")
                    return
        else:
            for county in less:
                try:
                    perc += county.ethnicities[program[1]]
                except KeyError:
                    print("Invalid Key")
                    return
    elif program[0] == "Income":
        if len(less) == 0:
            for county in fullData:
                try:
                    perc += county.income[program[1]]
                except KeyError:
                    print("Invalid Key")
                    return
        else:
            for county in less:
                try:
                    perc += county.income[program[1]]
                except KeyError:
                    print("Invalid Key")
                    return
    print(round(perc/len(fullData),2))

def totalPopulation(less):
    pop = 0
    if len(less) == 0:
        for county in fullData:
            pop += county.population["2014 Population"]
    else:
        for county in less:
            pop += county.population["2014 Population"]
    print(pop)

def filterST(less):
    filterCounties = []
    for county in fullData:
        if county.state == less[1]:
            filterCounties.append(county)
    print(len(filterCounties))
    return filterCounties

def filterGT(line, less):
    filterCounties = []
    program = line[1].split(".")
    if program[0] == "Education":
        if len(less) == 0:
            for county in fullData:
                try:
                    if county.education[program[1]] > float(line[2]):
                        filterCounties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key")
                    return
        else:
            for county in less:
                try:
                    if county.education[program[1]] > float(line[2]):
                        filterCounties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key")
                    return
    elif program[0] == "Income":
        if len(less) == 0:
            for county in fullData:
                try:
                    if county.income[program[1]] > float(line[2]):
                        filterCounties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key")
                    return
        else:
            for county in less:
                try:
                    if county.income[program[1]] > float(line[2]):
                        filterCounties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key")
                    return
    elif program[1] == "Ethnicities":
        if len(less) == 0:
            for county in fullData:
                try:
                    if county.ethnicities[program[1]] > float(line[2]):
                        filterCounties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key")
                    return
        else:
            for county in less:
                try:
                    if county.ethnicities[program[1]] > float(line[2]):
                        filterCounties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key")
                    return
    print("Filter: {} Greater than {}: {}".format(program[0], line[2], len(filterCounties)))
    return filterCounties

def filterLT(line, less):
    filterCounties = []
    program = line[1].split(".")
    if program[0] == "Education":
        if len(less) == 0:
            for county in fullData:
                try:
                    if county.education[program[1]] < float(line[2]):
                        filterCounties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key")
                    return
        else:
            for county in less:
                try:
                    if county.education[program[1]] < float(line[2]):
                        filterCounties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key")
                    return
    elif program[0] == "Income":
        if len(less) == 0:
            for county in fullData:
                try:
                    if county.income[program[1]] < float(line[2]):
                        filterCounties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key")
                    return
        else:
            for county in less:
                try:
                    if county.income[program[1]] < float(line[2]):
                        filterCounties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key")
                    return
    elif program[0] == "Ethnicities":
        if len(less) == 0:
            for county in fullData:
                try:
                    if county.ethnicities[program[1]] < float(line[2]):
                        filterCounties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key")
                    return
        else:
            for county in less:
                try:
                    if county.ethnicities[program[1]] < float(line[2]):
                        filterCounties.append(county)
                except ValueError:
                    print("Value {} can't be converted to a number".format(line[2]))
                    return
                except KeyError:
                    print("Invalid Key")
                    return
    print("Filter: {} Less than {}: {}".format(program[0],line[2],len(filterCounties)))
    return filterCounties

def display(less):
    if len(less) == 0:
        for county in fullData:
            print("County: {}\nState: {}\nPopulation: {}\n".format(county.county, county.state, county.population["2014 Population"]))
    else:
        for county in less:
            print("County: {}\nState: {}\nPopulation: {}\n".format(county.county, county.state, county.population["2014 Population"]))

def population(line, less):
    pop = 0
    program = line[1].split(".")
    if program[0] == "Ethnicities":
        if len(less) == 0:
            for county in fullData:
                pop += round(county.ethnicities[program[1]] * county.population["2014 Population"])
        else:
            for county in less:
                pop += round(county.ethnicities[program[1]] * county.population["2014 Population"])
    elif program[0] == "Education":
        if len(less) == 0:
            for county in fullData:
                pop += round(county.education[program[1]] * county.population["2014 Population"])
        else:
            for county in less:
                pop += round(county.education[program[1]] * county.population["2014 Population"])
    elif program[0] == "Income":
        if len(less) == 0:
            for county in fullData:
                pop += round(county.income[program[1]] * county.population["2014 Population"])
        else:
            for county in less:
                pop += round(county.income[program[1]] * county.population["2014 Population"])
    print("Population of {}: {}".format(program[1],population))

file = open(sys.argv[1])
lessCounties = []
for line in file:
    line = line.split(":")
    for x in range(len(line)):
        if "\n" in line[x]:
            line[x] = "".join(line[x][y] for y in range(len(line[x])-1))
    if line[0] == "display":
        display(lessCounties)
    elif line[0] == "filterST":
        lessCounties = filterST(line)
    elif line[0] == "filterGT":
        lessCounties = filterGT(line,lessCounties)
    elif line[0] == "filterLT":
        lessCounties = filterLT(line,lessCounties)
    elif line[0] == "totalPopulation":
        totalPopulation(line)
    elif line[0] == "population":
        population(lessCounties)
    elif line[0] == "percent":
        percent(line,lessCounties)
    elif line[0] == "reset":
        lessCounties = []
    else:
        print("Not a Command")