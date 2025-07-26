# Using Telerik charts for box and whisker plot visualization

## Question

**Iva** asked on 07 Nov 2022

Hello to all! I want to share with you my experience of using Telerik charts to build a box and whisker chart. This chart is extremely useful in statistical data processing to identify outliers in a data set. [https://en.wikipedia.org/wiki/Box_plot](https://en.wikipedia.org/wiki/Box_plot) Telerik doesn't have a special box and whisker chart component, but it's pretty easy to make one yourself. To do this, we need a candlestick chart to visualize the range of data and a line chart to visualize outliers. The open-source library MathNet.Numerics is used to calculate the summary statistics of five numbers. [https://numerics.mathdotnet.com](https://numerics.mathdotnet.com) Attached is a sample code, enjoy!
