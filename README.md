# Loop Testing with Prefixes
## The Problem
The problem that I chose to look at was the difference in speed when looking at different solutions to the same problem with code. Specifically three different variations of code that searched through a list to match a given prefix. What inspired me to choose this as my problem was my original solution to my CS151 midterm which was horribly slow. It probably cost me a ton of time on my midterm while testing different words. When working with small datasets these inefficiencies often go unnoticed it was until I got late into the problem that I noticed the flaw in my code. This was also a fun way for me to experiment with timing functions and seeing how the simplest solutions are often the fastest when it comes to computers.
### 1. My Original Loop (Slow)
```python
def valid_prefix(prefix):
    for i in range(len(prefix)):
        for word in SIXES:
            print(word[:i+1])
            if word[:i+1] == prefix:
                return True
            else:
                pass
    return False
```
>This is almost the exact code that I'm testing with a few things switched for variables to make testing easier. This uses a nested loop checking each prefix length against all words, redundantly comparing many times because nested loops grow over time making the inner loop sometimes execute literally thousands of times. Not only is it slow but just looking at it, it's very cluttered.
### 2. My Improved Loop (Medium)
```python
def valid_prefix_med(prefix, word_list):
    for word in word_list:
        if prefix == word[:len(prefix)]:
            return True
    return False
```
>I realized I could remove the inner loop by slicing each word once and directly comparing it to the prefix. This change speeds up the code by eliminating a lot redundant iterations.
### 3. Optimized Solution (Fast)
```python
def valid_prefix_fast(prefix, word_list):
	return any(word.startswith(prefix) for word in word_list)
```
>This version uses Python's built-in `startswith()` method along with the `any()` method. It's somehow the shortest among the three and also the fastest who would've thought. It's the fastest because it uses Python's built in methods which are optimized to be ran in python.
## Benchmarking
In order to save time when running the code I decided to split up the code into two separate parts the benchmark and the graph creation. Otherwise every time you'd trying and change something little about the graph you'd have to wait about a minute for every iteration of the benchmark to complete. This improves reusability and in my opinion readability allowing you to see the different parts that each code does.  
#### Data Collection
The code is run 10,00 times for each prefix in the given list `prefixes = ['c', 'ca', 'car', 'care', 'cares']`. The code checks whether a given prefix matches the start of any word from the word list, `SIXES`. It comes from a python file that contains every English word, `SIXES` referring to all the English words with 6 characters. The times were recorded, saved to a csv, and then plotted using pandas and `matplotlib` to work some magic. 
- **Timing** is done by recording the current time before and after running the function then subtracting to get the total time. Specifically I use the `time.time()` function from the `time` library. Because of the variability of computers running the test many times helps to alleviate some of the randomness. 
- The **data structure** consists of the results being collected in a list and then added to a `numpy` array which is then put inside of a `pandas` DataFrame and exported as a csv in order to be used inside of a different file. 
- By testing a **variety of prefixes** the code covers different cases for how long the prefix is. This matters because checking a shorter prefix would generally be faster than checking a long one so ensuring that we check both allows us to ensure that their is different in the outputs of the different algorithms.
#### Extra
- Using the `pandas` DataFrame was extremely helpful because it gave me easy access to powerful tools that allowed me transform the data how I wanted that being create a new column which displayed the difference from the fast and slow columns, export the data into a csv to be used later, and even transform the data into a markdown so it could be easily displayed.
- One thing I had to come back and do is add code that ensures that the whole file isn't run when importing code elsewhere because I wanted the code to be a tad bit more modular by making prefixes a variable that way you can change it in benchmark and then go over and graph it without having to change other code.
## Results & Analysis
### Table Analysis

| Prefix|    Slow |  Medium |    Fast | Time Diff|
| :---- | ------: | ------: | ------: | -------: |
| c     | 3.37406 | 3.29766 |  2.8319 | 0.542168 |
| ca    | 7.32399 | 4.22505 | 2.85994 |  4.46405 |
| car   | 11.5709 | 4.26772 | 2.86555 |  8.70532 |
| care  | 15.2111 | 4.20548 | 2.81983 |  12.3913 |
| cares | 19.0985 |  4.2281 | 2.86689 |  16.2316 |

Above is that markdown extracted from python using the built in `.to_csv()` function that `pandas` has. The data has columns for the times recorded by each method slow, medium, and fast indexed by the tested prefix strings. The results clear show a massive difference in performance based on the algorithm when looking at larger strings.
- The time difference shown in the fourth column was calculated using vector subtraction to to calculate the time difference across columns. I originally wanted to use it in the graphic somehow but couldn't figure out a nice way to integrate it in without it just appearing to be a parallel line to the slow line.

The largest takeaway from this project is how dramatically algorithm choice impact performance even for something as simple as prefix checking. The slow version will run through multiple layers of loops which adds extra nonsense at every loop iteration. The fast solution uses the built in functions which means it barely has to do any heavy lifting. Choosing a slow algorithm could mean the difference between an instant response and noticeable lag in any program.
### Visual Analysis
![Prefix Benchmark Comparison Over 10,000 Runs](https://github.com/Vespitalian/prefix-benchmark-cc/blob/main/prefix_benchmark.png)

This chart is a comparison of how long different versions of a loop take to run with different prefixes. It shows which algorithm runs best at different prefix lengths.
- The slow approach line gets increasingly sharper as the prefixes get longer. 
- The medium solution grows a bit in the beginning while coasting at ~4.2 from then on. 
- The fast solution remains the quickest and the most consistent solution staying at ~2.8 seconds throughout each variation in prefix. 
#### Creation Process
Creating the graphic was easy mostly because I didn't have to use any special graphs that we didn't go over. I did end up searching a lot of the different options available in the `matplotlib` library.
##### Visualization Choices
- **Line Plot**: Plotting these as lines instead of a pie char may have been obvious but why not bars or points? Time moves and is constant not a fixed integer value so it makes most sense to represent that change in time over a line which is also a constant not showing any gaps between data points.
- **Line coloring**: In this case the coloring is used to signify the quality of the algorithm. Red being poor, yellow being okay, andd green being good. Without the legend you wouldn't inherently know which algorithm is which just by looking at them (unless you're a computer scientist of course). The legend is something that is often overlooked but it is a very essential part of a graph because it helps you differentiate what is going on.
	-  I wanted the legend to be in reverse order because that's how it made sense in my brain and luckily that wasn't very hard to find since the documentation on `matplotlib` is so extensive. It was as simple as adding `reverse=True` when adding the legend function.
- **Basics**: To understand what the graph is showing it's essential to include labels on both the x and y axes to tell the reader what these numbers mean. The title sums up the whole graphic in a simple phrase so you know what you're looking at right away.
- **Grid**: A nice final touch to the graph can be a grid like the one included here so you can tell relatively where each data value is on each prefix. An alternative would be to add points that tell you exactly where the data point is but in my opinion it often takes away from the graph. 
##### Why a graph?
Making a plot like this turns boring numbers like those shown in the chart into a picture that the human eye can quickly understand. It's faster to compare different performances by looking at the different lines rather than reading through tables or raw numbers especially when you're working with more data. This kinda of data is especially hip when presenting results to young people these days as research shows that they can only learn when looking at things. The idea is that you can quickly look at this picture and are able to pickup that the optimized loop is the fastest by a considerable amount showing that the improvements to the code truly do matter.
## Ending Notes
#### Improvements
- **Expanding data**: The most obvious would be comparing this data with more prefixes, more lengths of prefixes, different word lengths, or the full English dictionary. More data is always better right?
- **Changing metrics**: Measuring more than just the total time a more accurate system would be to calculate the time after a set amount of runs and then calculating the standard deviation with that data or just including other data like median times.
- **The benchmarking method**: Right now the code uses time differences with `time.time()`. I found a separate function called `timeit` that might be able to perform timing more efficiently reducing "garbage" in the data collection process.
- **Ease of use**: Adding command-line arguments to control the number of runs or prefixes without having to manually go in and edit the code which would make the easier to use.

#### Real-World Applications
The difference between the nested loop and a built-in function seemed only minor when looking at just one prefix character but once the query got larger the time just keeps increasing exponentially. In this example the slowest algorithm took about 19 seconds for the longest prefix. If we changed to a larger dictionary that lag could quickly sky rockets to minutes or even hours. 

Benchmarking algorithms and optimizing code performance are applicable to every single job field in computer science. One similar example to what this test was accomplishing is autocomplete. Autocomplete is many different systems of technology, our browsers, our phones, and many other places. When a user types a few letters, the backend needs to quickly search through a large dictionary/database to suggest possible completions to the user based on the language the user uses, frequently used words, etc. 

Using inefficient or slow matching algorithms like the original code I came up with would directly negatively impact the user experience by creating latency or lag in how long it took for the recommended word to pop up, and in the slowest example almost 20 seconds (it was actually much less but it can still add up). With 20 seconds of delay any user will have already typed their word long ago. The simple difference between a nested loop and a built-in method in this example can be the difference between a snappy program and one that is noticeably laggy.

Performance benchmarking like the method I used (although I'm sure more sophisticated), that being running functions repeatedly, recording the time an event took, storing, graphing, and comparing results are all widely used for any software development where performance optimization is important such as in gaming. You **never** want to allow the user to blame their skill issues on your poor game design. Although some lag issues aren't necessarily a game developers problem and result from poor internet connection to the servers which then leads to the question of whose fault that is. The game developer for not having their server closer to the end-user or the end-user for having cheap wifi. 
