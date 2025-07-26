# Dynamically setting PageSize based on Grid Height

## Question

**Mic** asked on 16 Apr 2020

Marin: I'm able to size the grid based on the Viewport height, but having done that I want to set the Grid PageSize property so that the number of rows per page roughly consumes the available vertical space-- in other words I'm trying to avoid the vertical scroll bars appearing on the grid because it's displaying more rows than will fit in visible grid height. Presumably something like GridHeight / GridRowHeight would equal the optimal PageSize, but my experiments trying to get the RowHeight didn't work. Can you provide an example of how to do it? BONUS Question: How can I embed line returns in a string that will be displayed as a line break in the grid? ('\n' doesn't work for me) <div style="margin: 0;padding: 0;border-width: 0; height: 95vh;"> <TelerikGrid Data="@MyData" Height="100%" Pageable="true" Resizable="true"> <GridColumns> <GridColumn Field="@(nameof(SampleData.Id))" Width="120px" /> <GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" Groupable="false" /> <GridColumn Field="@(nameof(SampleData.Team))" Title="Team" /> <GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date" /> </GridColumns> </TelerikGrid> </div> @code { public IEnumerable<SampleData> MyData=Enumerable.Range(1, 200).Select(x=> new SampleData { Id=x, Name="Name " + x + "\nNext Line", Team="team " + x % 5, HireDate=DateTime.Now.AddDays(-x).Date }); public class SampleData { public int Id { get; set; } public string Name { get; set; } public string Team { get; set; } public DateTime HireDate { get; set; } } }

## Answer

**Marin Bratanov** answered on 16 Apr 2020

Hello Michael, You will need JS Interop to hook to the window.resize event and consume that handler in the component where the grid is declared. There are libraries that can help you with that (like this one ). Then, when you have the actual size of the viewport, and the actual size of the grid, you can perform the desired calculation in the event handler, and set the PageSize parameter of the grid (you will, of course, have to use a field in the view-model for that). If you create such a sample, I'd encourage you to open a pull request in this repo and post it, we award such contributions with Telerik points: [https://github.com/telerik/blazor-ui](https://github.com/telerik/blazor-ui) On line breaks - you need to initialize a MarkupString and include and HTML tag that can produce the desired result (such as a <br /> tag). The \n symbol applies to C#, but the browser renders HTML. Regards, Marin Bratanov

### Response

**Michael** answered on 16 Apr 2020

Let me rephrase my question... is there a way to determine the current Row Height of the grid? I get that you can supply a RowHeight and it will use that value, but if I'm not defining RowHeight how can I find out what it is?

### Response

**Marin Bratanov** answered on 17 Apr 2020

Hi Michael, You need JS Interop for that too. The grid is an HTML <table> and so the browsers determine a lot in its rendering - for example, when you set the RowHeight parameter, we set it as an inline style attribute to the row, but if the contents of a certain cell (say, long text, or a large image) are taller than that, the browser will ignore the explicit height we set and make the row taller. If you define a RowHeight that can accommodate all your content without stretching the rows, you can rely on using that in your calculations. Otherwise, you will need to use JS Interop to get the actual rendered height of the HTML elements. Regards, Marin Bratanov

### Response

**Michael** answered on 17 Apr 2020

Thanks-- I was hoping the grid might expose an easier way to get it (maybe a future feature?). From looking at the javascript examples it looks like more trouble than it's worth. I am using Ed's BlazorSize package by the way. When I have a chance I'll try to put together an example of all the tips and tricks I've learned-- mostly thanks to you-- in case it can help others getting started with the grid.

### Response

**Marin Bratanov** answered on 17 Apr 2020

Hello Michael, I do not expect the grid to expose such a feature. It provides a lot of settings so you can customize its behavior, and it expects that the developer sets them according to the application logic. Using JS Interop to get the DOM elements size will be the way until Microsoft provide a built-in way to do that in Blazor (If that happens). JS Interop is a valid thing in Blazor, even if the framework aims at enabling a lot of C# for many tasks that required JS. On examples of what you did and learned, feel free to post them. Maybe some of them would be interesting scenarios that can go into this repo (for example, if you implement the page size change with the viewport change approach). Regards, Marin Bratanov

### Response

**Michael** answered on 26 Apr 2020

Marin: I have created a sample project to demonstrate a number of things I have learned about in working with the Telerik Blazor Grid including how to dynamically set the grid height, responsively add or subtract columns based on media breakpoints, selecting a page and row and how to handle some formatting issues. Telerik Blazor Grid Demo None of this is rocket science, but it might be useful for others getting started. I know you suggested adding it to the existing telerik/blazor-ui repository, and I would if I knew how, but I'm afraid that doing pull requests is not in my toolkit. You are welcome to add it to the Telerik Blazor repository if you think it's worthy. Thanks for your continued help.

### Response

**Twain** commented on 04 Jan 2023

Thanks Michael. What you are sharing is very helpful. I will use it as a guide for my own implementation. Twain.

### Response

**Marin Bratanov** answered on 27 Apr 2020

Hello Michael, I added the project to the following URL: [https://github.com/telerik/blazor-ui/tree/master/grid/adjust-height-with-browser.](https://github.com/telerik/blazor-ui/tree/master/grid/adjust-height-with-browser.) You will find your Telerik points updated. Regards, Marin Bratanov
