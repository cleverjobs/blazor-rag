# Chart Background Color

## Question

**Cha** asked on 10 Aug 2020

I'm working on porting a UWP app to .Net core, and I can't find how to set the chart area color: In the UWP, I have the graph sitting in a grid, and my code is var tempBrush=new SolidColorBrush(GetBackgroundColor(_theData[0].ModuleType)); theGrid.Background=tempBrush; dataGraph.Background=tempBrush; I'd assume the Graph has the ability to set a style, but nope. The samples don't seem to show how to set a lot of things like MajorStep, MinorStep, label rotation etc for a TimeAxis - and I can't find a good reference for what is available. (The API docs have almost no examples.)

## Answer

**Marin Bratanov** answered on 10 Aug 2020

Hello Charles, There are two open feature requests for background settings on the chart that you can Follow (I've added your Vote to each to raise their priority): background on the chart itself background of the plot area element As for other settings - they are far too numerous to provide examples for each and we have added general tips on exploring them, like in the Customize Chart Elements - Nested Tags Settings section or the series-specific articles. We also made the following KBs to offer some examples: Style the Series Labels Prevent crowded grid lines Fix Overlapping Labels How to make transparent markers There's also a pretty large chart with a lot of settings in the Stocks sample app - here is its component file from its repo. For a time axis - the Date Axis article provides examples and explanations on the features specific to time axes. I hope this helps you get started and explore the component. Regards, Marin Bratanov
