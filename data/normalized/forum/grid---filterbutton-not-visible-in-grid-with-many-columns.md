# Grid - Filterbutton not visible in grid with many columns

## Question

**Ger** asked on 14 May 2019

Dear Telerik, the Gridfilter is working fine. Just one small problem. When there are many columns (in my case 12), the filter input textfield is too big for the column (see screenshot). The filterbutton is not visible. You have to scroll to see it. Is it possible to adjust the length of the input-field and fontsize of the different griditems ? What do you recommend to solve this ? Regards, Gert

## Answer

**Marin Bratanov** answered on 15 May 2019

Hello Gert, There are different ways this could be done and one would be to have the filter inputs have percentage width. Something like the date time filter or the number filter that you can see in our demos: [https://demos.telerik.com/blazor-ui/grid/filtering.](https://demos.telerik.com/blazor-ui/grid/filtering.) At the moment it is the string filter that is different only (and, obviously the bool filter which is a checkbox, so this isn't really applicable). There may also be a max-width on the inputs so they never stretch to the full cell width if the cell is very wide. I believe that we both agree that the filter and clear filter buttons should always be visible, however. If you think this is a good solution (please take it for a spin, with your columns, with fewer columns, resize the screen and so on), let me know and I will put it up in the

### Response

**Henri** answered on 15 May 2019

Hello Marin, in your demo example, the filter button of the number and date column stay visible when the screen is resized. I think the String-column should behave the same. Suggestions : - make the String-Input-field smaller (less characters) (most of the time people search only with a few characters) - the filter button must be visible all the time (like decimal/date filter) - create the possibility to decrease font-size generally for the Grid (or all Telerik components at once). (I personally think the font-size is default a bit too large) Regards, Gert

### Response

**Marin Bratanov** answered on 15 May 2019

Hello Gert, Here is the enhancement request page I made for the filter appearance: [https://feedback.telerik.com/blazor/1409173-ensure-filter-buttons-are-always-visible-and-the-inputs-are-responsive.](https://feedback.telerik.com/blazor/1409173-ensure-filter-buttons-are-always-visible-and-the-inputs-are-responsive.) If you have anything to add, feel free to drop a comment. On the font-size - you can add some CSS of your own to change the font size, something like the following snippet (result attached at the end of the post): <style> div. smallerFont, div.smallerFont.k-filtercell * { font-size: 10px; } </style> @using Telerik.Blazor.Components.Grid <TelerikGrid Data="@MyData" Class="smallerFont" Pageable="true" Filterable="true" Sortable="true" Height="200"> <TelerikGridColumns> <TelerikGridColumn Field="@(nameof(SampleData.ID))"> </TelerikGridColumn> <TelerikGridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name"> </TelerikGridColumn> <TelerikGridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date"> </TelerikGridColumn> </TelerikGridColumns> </TelerikGrid> original: <TelerikGrid Data="@MyData" Pageable="true" Filterable="true" Sortable="true" Height="200"> <TelerikGridColumns> <TelerikGridColumn Field="@(nameof(SampleData.ID))"> </TelerikGridColumn> <TelerikGridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name"> </TelerikGridColumn> <TelerikGridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date"> </TelerikGridColumn> </TelerikGridColumns> </TelerikGrid> @functions { //in a real case, keep the models in dedicated locations, this is just an easy to copy and see example public class SampleData { public int ID { get; set; } public string Name { get; set; } public DateTime HireDate { get; set; } } public IEnumerable<SampleData> MyData=Enumerable.Range(1, 50).Select(x=> new SampleData { ID=x, Name="name " + x, HireDate=DateTime.Now.AddDays(-x) }); } Regards, Marin Bratanov
