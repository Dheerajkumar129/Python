def count_words(filename):
    hackword = 0
    with open(filename, 'r') as file:
        for line in file:
            print(line)
            words = line.lower().split()
            for word in words:
                if word == "hack":
                    hackword += 1
        print(hackword)

filename = "automated_file.txt"
count_words(filename)



#automated_file.txt
This project is a data science hack that leverages CSV files to analyze movie ratings, demographics, and genres. The hack begins by importing the datasets into a Jupyter notebook, then hacking together some univariate visualizations for attributes like rating, age, and occupation. A clever hack allows us to visualize how genre popularity has shifted over the years.
Next, the hack tackles the challenge of listing the top 25 movies by average rating, using a hack to filter only those movies with at least 100 ratings. Finally, a comparison hack helps us verify certain hypotheses about movie preferences, such as men hacking their way through more drama and romance than women, while the sci-fi hack shows different results.
This series of hacks gives a clear picture of movie trends and preferences over time.
