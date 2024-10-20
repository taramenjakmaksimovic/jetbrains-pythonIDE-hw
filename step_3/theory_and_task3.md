# Theory 📖

You made the bar minimum. No pun intended. 😂

## Customization ✨
What you don't like about the previous barplot? Well, for me it is that it doesn't have a window title, the legend is not next to the barplot and the barplot is too small for that much information. Let's customize it!

Seaborn doesn't have a direct way to set the window title, but it is built on top of matplotlib, so you can set the window title using matplotlib commands. First, let's just make the barplot bigger. You can do that with `fig=plt.figure(figsize=(width, height))`, where fig is a variable name for a figure object. Now you can add the title using `fig.canvas.manager.set_window_title('Title')`.
If you want to change the aesthethics of all the plots created using seaborn, you can use `sb.set_theme()` where sb is a seaborn alias.

Some parameters of `set_theme()`:

Style:
You can choose from several built-in styles:
* "darkgrid" - a dark background with grid lines
* "whitegrid" - a light background with grid lines
* "dark" - a dark background without grid lines
* "white" - a light background without grid lines
* "ticks" - adds ticks to the axes without grid lines

Palette:
You can specify a color palette using names of seaborn palettes (like "deep", "muted", "bright", etc.) or by passing a custom color list.

Context:
You can set the context for your plot using the following options:
* "paper" - for small-scale media like papers
* "notebook" - for interactive environments
* "talk" - for presentations
* "poster" - for large displays

For more information on `set_theme()` please click [here](https://seaborn.pydata.org/generated/seaborn.set_theme.html#seaborn.set_theme).

> **Note**
>
> When you call `sb.set_theme()` without any parameters, it uses the following default values for the parameters style, palette, and context: <br>
> style: "darkgrid" <br>
> palette: "deep" <br>
> context: "notebook"





A simple legend isn't enough, you want to make in more informative and position it as you want. Title parameter is, as it name says, adding the title to your legend. Loc parameter determines the location of the legend on your plot. <br>

Loc values are:
* 'best' (0) - automatically chooses the location with the least overlap with the plot
* 'upper right' (1) - places the legend in the upper-right corner
* 'upper left' (2) - places the legend in the upper-left corner
* 'lower left' (3) - places the legend in the lower-left corner
* 'lower right' (4) - places the legend in the lower-right corner
* 'right' (5) - places the legend on the right side of the plot (not inside)
* 'center left' (6) - places the legend in the middle of the left side
* 'center right' (7) - places the legend in the middle of the right side
* 'lower center' (8) - places the legend at the bottom center of the plot
* 'upper center' (9) - places the legend at the top center of the plot
* 'center' (10) - places the legend in the center of the plot <br>

Each of these can be used either by name or by the corresponding integer.

The loc parameter isn't enough, because you want the legend outside the plot. To make this happen, you use `bbox_to_anchor(x,y)`, where x and y are the coordinates specifying the point to which the legend is anchored. <br>

These values usually range from 0 to 1, where:
* 0 corresponds to the left/bottom of the plot/figure,
* 1 corresponds to the right/top of the plot/figure.
* Values outside the 0-1 range place the legend further outside the plot.

Using these parameters, your code for legend will look like `legend=plt.legend(title='Title', loc= loc_value, bbox_to_anchor=(x, y))`, where the first legend is a variable name. 
The customization of the legend doesn't end there, you can also add changes tho the frame. <br>

To achieve that you can do: <br>
`frame = legend.get_frame()` - method `get.frame()` retrieves the frame (the border) of the legend <br>
`frame.set_facecolor('color')` - this line changes the background color of the legend frame <br>
`frame.set_edgecolor('color')` -this line changes the edge color of the legend frame



# Task 🤓
Using the code from the previous step, customize the barplot:
1. Set the plot window title: title the plot window as 'Game Platform Analysis'.
2. Configure the plot theme: apply the default seaborn theme to the plot.
3. Adjust plot dimensions: set the width of the plot to 14 and the height to 8.
4. Customize the legend:
* add a title to the legend: 'genre'.
* position the legend in the center right of the plot using `loc`.
* use `bbox_to_anchor()` to adjust the legend's position, setting the x coordinate to 1.14 and the y coordinate to 0.5.
5. Modify the legend frame:
change the frame's edge color and face color to white.