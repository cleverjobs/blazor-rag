# Pie Chart white background.

## Question

**n/an/a** asked on 09 Feb 2022

1. I am creating a pie chart and the element the chart is nested in has a white background I cant seem to change please help. 2. I am using custom styling and have left out a component I would like to add a single component. I have however changed some of the default telerik styling in the file is there a way I can get the exclusive css for a single component without needing a whole new file? thanks

## Answer

**Marin Bratanov** answered on 10 Feb 2022

Hello, The chart background should be available as a setting as of 2.30: [https://feedback.telerik.com/blazor/1464002-expose-a-parameter-that-changes-the-background-color-of-the-plot-area](https://feedback.telerik.com/blazor/1464002-expose-a-parameter-that-changes-the-background-color-of-the-plot-area) As for component-specific CSS - I am afraid this is not possible. To target a specific component instance with your own CSS overrides, you should use its Class and cascade the customizations through it. Otherwise, more generic rules will target all instances and maybe even parts of other components you did not intend. Regards, Marin Bratanov
