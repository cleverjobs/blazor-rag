# GridSearchBox with templated field

## Question

**Ger** asked on 28 Jan 2021

I have a template for one of my columns that is bound to a bool property of the context object. class Model { public string Name { get; set; } public string Guid { get; set; } public bool IsSelected { get; set; } } And grid columns defined like so: <GridColumns> <GridColumn Field="@(nameof(Model.IsSelected))" Width="220px" Title="Name" Resizable="false"> <Template Context="context"> @{ if (context is Model model) { <TelerikCheckBox Id="cbIsSelected" @bind-Value="@model.IsSelected" /> <label for="cbIsSelected" class="ml-2">@model.Name</label> } } </Template> </GridColumn> <GridColumn Field="@(nameof(Model.Guid))" Width="330px" /> </GridColumns> The GridSearchBox works beautifully on the Guid field, but not on the Name field. I'd like to be able to search on both. I'd appreciate guidance on how to do this.

## Answer

**Marin Bratanov** answered on 29 Jan 2021

Hello Gerhard, The searchbox feature works with string fields, so it should work with the Name field. Judging by the title of this thread, I suspect you need it to work with the IsSelected field - since it is bool and not a string, it cannot work. You can Follow this feature request for additional types support in the searchbox: [https://feedback.telerik.com/blazor/1485012-allow-searchbox-to-work-with-other-data-types.](https://feedback.telerik.com/blazor/1485012-allow-searchbox-to-work-with-other-data-types.) Here is a small test sample that shows this working as expected for the Name field once a column for it is added, and how booleans cannot yet be filtered. The key thing is that for the grid searchbox to use a certain field, there must be a column using it. I am attaching a short video with the expected behavior to the end of this post as a reference too. <TelerikGrid Data="@Data" Pageable="true"> <GridToolBar> <GridSearchBox> </GridSearchBox> </GridToolBar> <GridColumns> <GridColumn Field="@(nameof(Model.IsSelected))" Width="220px" Title="Name" Resizable="false"> <Template Context="context"> @{
if (context is Model model)
{ <TelerikCheckBox Id="cbIsSelected" @bind-Value="@model.IsSelected" /> <label for="cbIsSelected" class="ml-2"> @model.Name </label> }
} </Template> </GridColumn> <GridColumn Field="@(nameof(Model.Guid))" Width="330px" /> <GridColumn Field="@(nameof(Model.Name))" Width="330px" /> </GridColumns> </TelerikGrid> @code{
List <Model> Data { get; set; }=Enumerable.Range(1, 100).Select(x=> new Model { IsSelected=x % 3==0, Name=$"Name {x}", Guid=Guid.NewGuid().ToString() }).ToList();
public class Model
{
public string Name { get; set; }
public string Guid { get; set; }
public bool IsSelected { get; set; }
}

} Regards, Marin Bratanov

### Response

**Gerhard** answered on 29 Jan 2021

Thank you for the detailed response Marin. It turns out that I could just as well bind to the Name field instead of the IsSelected field. No other changes are necessary and the previous (desired) behavior is retained, plus, searching now works on the Name field too obviously. I would be good to support other datatype in the search box though.

### Response

**Marin Bratanov** answered on 29 Jan 2021

You're welcome, Gerhard. Indeed, using the Name column only could be a solution for you as long as you either don't want to edit the IsSelected field, or you would make an editor to edit both fields in that column. On another note - the grid has built-in selection that does not require a field in your own model: [https://docs.telerik.com/blazor-ui/components/grid/selection/overview](https://docs.telerik.com/blazor-ui/components/grid/selection/overview) Regards, Marin Bratanov

### Response

**Gerhard** answered on 01 Feb 2021

Hi Marin, Thanks for the heads-up on the built-in selection support. I am still getting familiar with the components so I didn't know about this. It looks like it'll serve my purposes so I shall update my implementation accordingly!

### Response

**Marin Bratanov** answered on 01 Feb 2021

I'm happy to see the grid make things easier for you, Gerhard :) Regards, Marin Bratanov
