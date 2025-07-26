# Incell Editing Font Size

## Question

**Ste** asked on 07 Nov 2020

I've used the Elastic Design example to change the font size of the grid, however, font size for Incell Editing appears to revert to standard size. I'm assuming there are some further style settings that can be set to get Incell Editing to match the Grid Font size?

## Answer

**Marin Bratanov** answered on 11 Nov 2020

Hi Steve, You can add cascades that also target inputs in the CSS, for example, here's the addition to the example from the docs: The grid offers elastic design capabilities <style> div.smallerFont, div.smallerFont.k-filtercell * { font-size: 10px;
} div.smallerFont.k-dropdown.k-header.k-dropdown-operator { width: calc ( 8px + 2em )!important;
} /* One example for altering content inside the cells - the inputs in InCell editing mode here
You can create similar rules as needed by inspecting the rendered HTML. This blog can help you do that
[https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools](https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools)
*/ div.smallerFont.k-grid-edit-cell input { font-size: 10px;
} </style> <TelerikGrid Data="@MyData" Class="smallerFont" Pageable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Sortable="true" Height="200px"> <GridColumns> <GridColumn Field="@(nameof(SampleData.ID))"> </GridColumn> <GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name"> </GridColumn> <GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date"> </GridColumn> </GridColumns> </TelerikGrid> original: <TelerikGrid Data="@MyData" Pageable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Sortable="true" Height="200px"> <GridColumns> <GridColumn Field="@(nameof(SampleData.ID))"> </GridColumn> <GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name"> </GridColumn> <GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date"> </GridColumn> </GridColumns> </TelerikGrid> @code {
//in a real case, keep the models in dedicated locations, this is just an easy to copy and see example
public class SampleData
{
public int ID { get; set; }
public string Name { get; set; }
public DateTime HireDate { get; set; }
}

public IEnumerable <SampleData> MyData=Enumerable.Range(1, 50).Select(x=> new SampleData
{
ID=x,
Name="name " + x,
HireDate=DateTime.Now.AddDays(-x)
});
} Regards, Marin Bratanov

### Response

**Fairoz** answered on 13 Apr 2021

Hi Marin, I have been trying to change the font size of the entire grid but had not been able to do so. I have tried the above elastic codes and the font size for the filter cell does change but not the cells from the rows. I have only one read only column. Am I missing anything?

### Response

**Steve** answered on 13 Apr 2021

Fairoz, Have you updated to the latest version of Telerik Blazor? I believe I was seeing the same thing as you, and then without altering my code I updated Telrik Blazor and it started working for all of the Grid.

### Response

**Marin Bratanov** answered on 13 Apr 2021

Hi all, Changing the font size can require a few CSS rules (see example in the Elastic Design section of the docs ) and it is important to keep in mind that when you upgrade you must update the assets and themes if you are not using them through our static assets. Regards, Marin Bratanov

### Response

**Fairoz** answered on 13 Apr 2021

I had just updated to 2.22.0 and its still the same. The CSS rules does not change the Font Size of the Grid. <TelerikGrid Class="smallerFont" Data="@traveller.P_RunInfos" Height="600px" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" EditMode="@GridEditMode.Incell" Resizable="true" SelectionMode="@GridSelectionMode.Multiple" @bind-SelectedItems="traveller.P_SelectedRunInfos"> @*<TelerikGrid Data="@traveller.P_RunInfos" Height="600px" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" EditMode="@GridEditMode.Incell" Width="1500px" Resizable="true" SelectionMode="@GridSelectionMode.Multiple" SelectedItemsChanged="@((IEnumerable<RunInfo> employeeList)=> OnSelect(employeeList))" @bind-SelectedItems="traveller.P_SelectedRunInfos">*@<GridColumns> <GridCheckboxColumn /> <GridColumn Field="P_RunID" Title="RunID" Groupable="false" Filterable="true" Editable="false" /> </GridColumns> </TelerikGrid> div.smallerFont, div.smallerFont .k-filtercell * { font-size: 10px; } div.smallerFont .k-dropdown.k-header.k-dropdown-operator { width: calc(8px + 2em) !important; } /* One example for altering content inside the cells - the inputs in InCell editing mode here You can create similar rules as needed by inspecting the rendered HTML. This blog can help you do that [https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools](https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools) */ div.smallerFont .k-grid-edit-cell input { font-size: 10px; } div.smallerFont .k-grid-container { font-size: 10px; }

### Response

**Marin Bratanov** answered on 13 Apr 2021

Hi, I made a sample for you with the current latest (2.23.0) that shows how this works as expected. I am attaching it at the end of this post together with a short video that demonstrates the expected results. I hope comparing against it will help you move forward. You may also find useful this blog post on inspecting the rendering of the elements on the page, the CSS rules that apply to them, and to change those rules: [https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools.](https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools.) Even when there are components for most things, in the web you'd need to handle the HTML tags and their styling with CSS, this is the fundamental thing about a web app and using components cannot completely abstract that away. Regards, Marin Bratanov

### Response

**Fairoz** answered on 14 Apr 2021

Hi Marin, I did import your code to our sample project and observed something. The div.smallerFont had changed the filtercell, the footer region and the in-cell editing fonts but not the default row. Perhaps I need to target the row font specifically? Also, I had no issues with changing the blazor TreeView fonts. The issue seems to be with the Grid only. I can attach the sample project if you require. Let me know how. Thanks.

### Response

**Marin Bratanov** answered on 14 Apr 2021

Hello Fairoz, Perhaps you need a heavier selector. Perhaps there is some other CSS in the project that's interfering. Since there is a set of selectors that works fine for my project, my best advice is to compare against them, inspect the rendering to see what rules are applied and tweak the rules so you get the desired behavior. Regards, Marin Bratanov

### Response

**Fairoz** answered on 15 Apr 2021

This is for those who might hit the same problem. The below needs to be added and it works. div.smallerFont .k-grid-table { font-size: 12px; }
