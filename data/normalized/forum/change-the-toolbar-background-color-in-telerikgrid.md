# Change the toolbar background color in telerikgrid

## Question

**Jef** asked on 05 May 2021

Hi there, I'm trying to change the background of toolbar in telerik grid, I know the key is to override the default css, but I couldn't make it. Would you please help me? The font color works well but the background-color doesn't work, even thought I use Bootstrap in the toolbar it still doesn't work. I remove some unnecessary code to make it clean. I also realized it's impossible to do CSS isolation in other components, so I put the css in the global stylesheet. <TelerikGrid Data="GridDataViewModel" Class="addBtn"> <GridColumns> <GridColumn Field="@nameof(ViewModel.Editor)" Editable="false"> </GridColumn> <GridColumn Field="@nameof(ViewModel.EditTime)" Editable="false"> </GridColumn> <GridCommandColumn Width="190px"> <GridCommandButton Command="Save" Icon="save" ShowInEdit="true"> Update </GridCommandButton> </GridCommandColumn> </GridColumns> <GridToolBar> <GridCommandButton Command="Add" Icon="add" Class="addBtn"> Add Branch </GridCommandButton> </GridToolBar> </TelerikGrid> div.k-toolbar button.k-button-icontext { background-color: #4CAF50; color: forestgreen
}.addBtn { background-color: #4CAF50;
}

## Answer

**Marin Bratanov** answered on 05 May 2021

Hello Jeff, Some elements have a background image set to a linear gradient so you need to remove that if you want to change the background. Also, the CSS rule I see attempts to target a button and not the entire grid toolbar. Here is a sample I made for you that shows two basic rules to target the toolbar background color, and the background of buttons in the toolbar. You can tweak them further and cascade through more complex selectors as necessary. <style> /*backbround for the toolbar*/.k-grid.k-toolbar { background-color: red;
} /*background for the buttons in the toolbar*/.k-grid.k-toolbar.k-button { background-color: yellow; background-image: none;
}
</style>

<TelerikGrid Data=@MyData Pageable="true" PageSize="15">
<GridToolBar>
<GridCommandButton Command="Add" Icon="add" Class="addBtn">Add Branch</GridCommandButton>
</GridToolBar>
<GridColumns>
<GridColumn Field=@nameof(SampleData.Name) Title="Employee Name" />
<GridColumn Field=@nameof(SampleData.HireDate) Title="Hire Date" />
</GridColumns>
</TelerikGrid>

@code {
// in a real case, keep the models in dedicated locations, this is just an easy to copy and see example public class SampleData {
public int ID { get; set; } public string Name { get; set; } public DateTime HireDate { get; set; }
} public IEnumerable <SampleData> MyData=Enumerable.Range (1, 50).Select ( x=> new SampleData {
ID=x,
Name="name " + x,
HireDate=DateTime.Now.AddDays(-x)
});
} Regards, Marin Bratanov Progress Telerik

### Response

**Jeff** commented on 06 May 2021

It works well! Thank you Bratanov, I noticed the background-image did something but didn't realize I needed to set it to none. I'm curious is that possible to add new feature about styling the buttons inside grid? Grid header, columns and cells have implemented the feature already.

### Response

**Marin Bratanov** commented on 06 May 2021

Using CSS in a manner similar to what I outlined is the way to add such custom styling. Most elements in the grid have unique classes so you can easily build selectors for them, and the rows have dedicated events so formatting can be conditional based on the data. The toolbar, however, is not tied to the data so conditional logic for it is entirely up to the app and if you want to change things based on runtime conditions, you can cascade through the Class parameter of the entire grid and change that as needed.

### Response

**Jeff** commented on 06 May 2021

I see, toolbar is not related to data, change the style by chaining toolbar to Class property is enough, thanks for explanation!
