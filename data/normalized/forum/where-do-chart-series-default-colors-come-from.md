# Where do Chart series default colors come from?

## Question

**Han** asked on 24 Mar 2023

I want my end users to be able to select a "series palette" for the telerik charts I created. Though I can easily create a handler that assigns colors to series when I create them, I was wondering where the default colors come from when no color was assigned to the series, and if I can "override" this somehow for a specific chart. I have Examined the source code somewhat, but up to now to no avail. 1) Is it possible to set the "default colors palette" on <TelerikChart> or <ChartSeriesItems> level, but without setting a specific color on <ChartSeries> level? 2) Is there another way (eg CSS) to define the series color palette for a chart series that would not change the palette for other charts on the same page? 3) How could I address the (default color) palette if I wanted to assign eg each column in a column chart with a color from the default palette? TIA - Hans

## Answer

**Ivan** answered on 27 Mar 2023

Hi! They taken from built-in themes and can be overriden with ThemeBuilder [https://themebuilderapp.telerik.com/](https://themebuilderapp.telerik.com/)

### Response

**Werdna** commented on 16 Aug 2023

Ivan, I am fine using this color palette, but if I have more than 6 series, these colors just repeat. How can I add many more colors than just the default 6?

### Response

**Yanislav** commented on 21 Aug 2023

Hello Andrew, To have full control over the color of the series, you can specify a ColorField. <ChartSeries Type="ChartSeriesType.Pie" ColorField="@nameof(ModelData.Color)" Thus, you can define your own colors for the series by including a field in the model whose value is a valid CSS color. The colors will be applied to the respective series. You can specify the color explicitly or execute a custom logic to generate random colors like in the following example: [https://blazorrepl.telerik.com/wHaPmxvx35X8Zw1v52](https://blazorrepl.telerik.com/wHaPmxvx35X8Zw1v52) I hope this helps. In case you have any other questions, please do not hesitate to contact us.

### Response

**Christian** commented on 16 Jul 2024

In blazor the charts are ignoring my theme builder. In MVC I could add Theme="Sass" but that doesn't seem to be an option in Blazor. How do I get the charts to use the theme builder colors?

### Response

**Christian** commented on 16 Jul 2024

Theme builder doesn't work for blazor charts

### Response

**Dimo** commented on 17 Jul 2024

@Christian I am copy-pasting my ticket reply here for everyone's reference: The Chart series colors depend on the $series-... variables in the ThemeBuilder. The Chart may not use the expected colors due to the following reasons: The series variables are not customized in the ThemeBuilder. The custom CSS theme is outdated and you need to recreate it to be compatible with the Telerik UI for Blazor version. The custom CSS theme is not registered correctly. There are two Telerik CSS themes on the page and the second one overrides the first one. The Chart series have their Color or ColorField parameters set. I am sending you a few attachments: A sample custom theme with 4 custom series colors ( series-a, series-b, series-c, and series-d ). A screenshot of the series variables in the ThemeBuilder. How the below Chart example looks like when the app is using the attached custom theme.
