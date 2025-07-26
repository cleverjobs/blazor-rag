# Donut chart and gap/spacing between items

## Question

**Mau** asked on 10 May 2024

I have a donut with 2 ChartSeries. For the inner circle I have tried to separate the different data items with a empty space. But I have no idea how it works. Could somebody help? <ChartSeries Type=" ChartSeriesType. Donut " Data=" @GridDataDonutProjectName " Field=" @nameof ( ProjectOverviewVm. Hours ) " CategoryField=" @nameof ( ProjectOverviewVm. ProjectName ) " Gap="0.8" Spacing="0.8" Margin="5"> Because of the Margin there is some space between the 2 donuts series But how can I add some empty space at the arrows in this picture. I have tried something with spacing and gap but I'm doing something wrong

## Answer

**Tsvetomir** answered on 15 May 2024

Hello Maurice, Thank you for the provided screenshot and for explaining so clearly the result you are looking for. To customize the space between the different segments in a Donut Chart, use the ChartSeriesBorder tag. This is a new feature of our Chart components that is available in our latest version ( 6.0.0 ), which was released today ( 15th of March ). To achieve white space between the segments, set the following parameters of the ChartSeriesBorder tag: The Color parameter to " white " The Width parameter to the desired width space (e.g. " 10 ") To assist you further, I prepared for you a REPL example that demonstrates the desired outcome. As a side note, the Gap and Spacing parameters of the ChartSeries tag are mostly used for other Chart types. I hope the provided information serves you well in continuing with your project. Regards, Tsvetomir Progress Telerik
