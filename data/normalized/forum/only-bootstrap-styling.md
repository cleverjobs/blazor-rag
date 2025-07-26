# Only Bootstrap Styling

## Question

**PHPH** asked on 30 Jul 2019

Is is possible to dump the kendo .css libraries and style components like buttons purely with Bootstrap?

## Answer

**Marin Bratanov** answered on 31 Jul 2019

Hi, I'm afraid that's not possible. We have a lot of elements and classes that require specific styling and that cannot be done with just bootstrap. We have, however, a theme based on Bootstrap that you can use: [https://docs.telerik.com/blazor-ui/themes.](https://docs.telerik.com/blazor-ui/themes.) You can see it in action in our demos through the theme chooser at the top right hand corner (see the screenshot below). You may also find interesting this sample app where bootstrap and variables are used with compiled SASS to affect the Bootstrap theme and the site stylesheet as well: [https://github.com/telerik/blazor-dashboard.](https://github.com/telerik/blazor-dashboard.) Regards, Marin Bratanov

### Response

**PH** answered on 31 Jul 2019

Ok Marin - understood - thank you for the suggestion for the Bootstrap theme - I'll certainly give that a try. Best regards, Peter
