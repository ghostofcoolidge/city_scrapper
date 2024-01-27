import requests

# pulls the data from the website
r = requests.get("https://www.city-data.com/city/South-Carolina.html")

# removes the body of text that does not contain the list of cities and population
r_test = r.text.split("<tbody>")[-1].split("</tbody>")[0]

# writes the header for the text file
with open("test.txt", "w+", encoding="utf-8") as f:
    f.write("city, state and population\n\n")

# appends each city and state to the text file
with open("test.txt", "a+", encoding="utf-8") as f:

    # loops through line of text parse the city name, state, and population
    for item in r_test.split("</tr>"):
            parsed_data = ""
            if "href='" in item:

                # checks if the string has javascript in it and parses accordingly
                if "href='j" in item:
                    parsed_name = item.split("href='javascript:l(\"")[1].split(");'>")[1].split("</a>")[0]
                    parsed_population = item.split("<td>")[-1].split("</td>")[0]
                    parsed_data = parsed_name + " " + parsed_population + "\n"
                
                # if javascript not in string, parses accordingly
                else:
                    parsed_name = item.split("html'>")[1].split("</a>")[0]
                    parsed_population = item.split("<td>")[-1].split("</td>")[0]
                    parsed_data = parsed_name + " " + parsed_population + "\n"

                # writes city data to text file
                f.write(parsed_data)


print('done!')