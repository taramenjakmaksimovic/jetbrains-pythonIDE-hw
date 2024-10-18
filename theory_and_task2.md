# Theory 📖

If you are here, you have sucessfully completed the first step! 🎉 <br>

## Making a simple plot using seaborn 📊
Please look at the range of plots [here](https://seaborn.pydata.org/examples/index.html). Clicking on the image you will see the name of the plot. <br>

A simple way to create a plot using seaborn is by using `sb.name_of_the_plot()`, where sb is the seaborn alias. Typically, axis labels for the plot should not be left blank, and you can set them like this: `sb.name_of_the_plot(x='name1', y='name2')`.

The data parameter indicates where seaborn should look for the variables that you are plotting. To add data to your plot, use `sb.name_of_the_plot(data='your_data')`.

The order parameter refers to the arrangement of categorical variables on the axes of a plot. To specify the order in your plot, use `sb.name_of_the_plot(order='custom_order')`.

The hue parameter allows you to add a third dimension to your plot by differentiating data within the same category using color. To add hue to your plot, use `sb.name_of_the_plot(hue='column_name')`, which specifies the column in your data used to group the data by different colors. You can also specify the hue order with`sb.name_of_the_plot(hue_order='custom_hue_order')`.
 
# Task 🤓
Create a simple bar plot that shows the number of games per 4 specific gaming platforms (PS4, XOne, PC and WiiU) by game genre. <br>
Use the code from the previous step. X label should be named 'platform', y label should be named 'count'. The order of the platforms should be: PS4, XOne, PC an WiiU. The order of the genres should be: Action, Adventure, Fighting, Misc, Platform, Puzzle, Racing, Role-Playing, Shooter, Simulation, Sports, Strategy. <br>

> **Note**
> If you don't include `plt.show()` you won't see your plot. Plt is a matplotlib alias.
>