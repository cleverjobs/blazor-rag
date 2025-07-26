# Very basic questions: Including Telerik CSS files in Blazor project

## Question

**che** asked on 21 May 2021

Hello, a REALLY basic question here, as I don't work on the UI tier very often. I am looking for a little help getting started with Less-Based themes. I'm reading [https://docs.telerik.com/kendo-ui/styles-and-layout/appearance-styling.](https://docs.telerik.com/kendo-ui/styles-and-layout/appearance-styling.) How do I add the CSS files ( kendo.common.css and kendo.[theme].css) to my Visual Studio 2019 project? I.e., where are they installed on my Windows 10 machine so I can reference them? Or, is there a URL to Telerik that I have to configure somewhere in my project? I am also going to throw out this anticipatory question - Do you think I will be able to do things like make Blazor Grid rows shorter in height via using Less-Based (or any)Themes...or do I need to make my own CSS classes to accomplish this? Thanks a lot!

## Answer

**Marin Bratanov** answered on 21 May 2021

Hi, If you will be using the Telerik UI for Blazor components, you must use one of the themes they support: [https://docs.telerik.com/blazor-ui/themes/overview.](https://docs.telerik.com/blazor-ui/themes/overview.) These are the SASS themes that you can also use with Kendo, but you cannot use the LESS themes with the UI for Blazor components, and you must not mix two themes on the same page. Generally, if you want to tweak a particular aspect of a particular component, the way is to inspect the rendered HTML and its applied styles, and to devise CSS rules that override the built-in rules so that you can achieve the desired appearance. You can find one example of reducing sizes and paddings here: [https://docs.telerik.com/blazor-ui/components/grid/overview#elastic-design.](https://docs.telerik.com/blazor-ui/components/grid/overview#elastic-design.) The Themes we have have some general settings and if writing up specific CSS overrides for certain element is not enough for you, the best way to apply widespread modifications is to build a custom theme. The Theme Builder app we provide is good for changing basics like colors, and if you want to dig deeper into paddings, typography and other dimensions, getting the themes source code and modifying it to build your own theme is the way to go. You can read more about both here: [https://docs.telerik.com/blazor-ui/themes/custom-theme.](https://docs.telerik.com/blazor-ui/themes/custom-theme.) Regards, Marin Bratanov

### Response

**chesk345** commented on 21 May 2021

Thank you! I'll go over your answer carefully and try to get up on the learning curve. I'll come back if I have more specific questions.
