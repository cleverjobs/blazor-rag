# Separate ColumnChooser button

## Question

**Joe** asked on 05 Nov 2020

Hello, I was wondering if it is possible to add a column chooser button to the GridToolbar. Now it's only possible to have a column chooser in the ColumnMenu and then it's in every column. Example here: [https://ibb.co/F3TndK2](https://ibb.co/F3TndK2)

## Answer

**Svetoslav Dimitrov** answered on 10 Nov 2020

Hello Joeri, Currently, we expose the column chooser only as part of the ColumnMenu. To create a custom column chooser you could: Setup a custom Telerik Button in the Grid Toolbar Setup the Visible parameter for the columns of your Grid On click of that button open a TelerikWindow or an animation container Use the Telerik Checkbox to toggle their visibility Below, you could see a short code snippet with a sample implementation of a custom column chooser: <TelerikGrid Data="@MyData" Pageable="true" PageSize="10">
<GridToolBar>
<TelerikButton OnClick="@( _=> isModalVisible=true )">Column Chooser</TelerikButton>
</GridToolBar>
<GridColumns>
@foreach ( var col in Columns)
{
<GridColumn Field="@col.Key" Width="120px" Visible="@col.Value" />
}
</GridColumns>
</TelerikGrid>

<TelerikWindow Modal="true" @bind-Visible="@isModalVisible">
<WindowTitle>
<strong>Column Chooser</strong>
</WindowTitle>
<WindowContent>
@foreach ( var col in Columns)
{ var id=$" {col.Key} Column";
<TelerikCheckBox Value="@col.Value" ValueChanged="@((bool value)=> ValueChanged(col.Key, value))" Id="@id"></TelerikCheckBox>
<label for="@id">@col.Key Column</label>
}
</WindowContent>
<WindowActions>
<WindowAction Name="Minimize" />
<WindowAction Name="Maximize" />
<WindowAction Name="Close" />
</WindowActions>
</TelerikWindow>

@code { public bool isModalVisible { get; set; } public Dictionary<string, bool> Columns { get; set; }=new Dictionary<string, bool>
{
{ nameof (SampleData.Id), true },
{ nameof (SampleData.Name), true },
{ nameof (SampleData.Team), true },
{ nameof (SampleData.HireDate), true }
}; private void ValueChanged ( string key, bool value ) {
Columns[key]=value;
} public class SampleData { public int Id { get; set; } public string Name { get; set; } public string Team { get; set; } public DateTime HireDate { get; set; }
} public IEnumerable<SampleData> MyData=Enumerable.Range( 1, 30 ).Select(x=> new SampleData
{
Id=x,
Name="name " + x,
Team="team " + x % 5,
HireDate=DateTime.Now.AddDays(-x).Date
});
} Regards, Svetoslav Dimitrov

### Response

**Michal** commented on 28 Mar 2022

Hello Svetoslav, this apporach is close, but i am missing one point: HOW to iterate grid columns which are created in RAZOR layout. <TelerikGrid @ref="GHL"...> <GridColumns> <GridColumn Field="@(nameof(TIMVykVykaz.CC))" DisplayFormat="{0:n2}" Title=@(Localize( " Total Price "))/>....
</<GridColumns> @code{
foreach(var col in GHL.GridColumns){
col.Title...
... will not work, because "GridColumns" is RenderFragment.
} 1) - Any idea how to iterate DECLARED columns in grid? (GridState is not enought, there is missing "Title" for end user) 2)- Any alternative how to show colum chooser by code(or somehow)? (Imagine scenario when NO columns are initialy visible in grid to the end user) Thank you

### Response

**Marin Bratanov** commented on 28 Mar 2022

In Blazor, the typical approach is to define the data in the view-model, and build the component based on that. So, some descriptor class for the columns can be your data source and a foreach loop over it can create your columns, while filtering it can let you loop over them. You can find a basic example at the bottom of this thread: [https://feedback.telerik.com/blazor/1450105-column-chooser](https://feedback.telerik.com/blazor/1450105-column-chooser)

### Response

**Michal** commented on 18 Jun 2023

View-model has its place, but is there an option how to iterate declared <GridColumns> from code? If you spent time with declaring it, why not to access it? Its overkill to duplicate it to the backing class(model) again, especially in classic sql query->frontend. Its another "dummy/disconnected object" to maintain and synchronize with grid. Any "special trick" will by useful also, like iterating "renderfragments"(but i dunno how), its not performance critical. End users chooses the columns, re-arrange, changes the widths and save it as own layout/view not too frequently. Its just for let user pick columns with "friendly" (title) names=end user defined view from existing pre-definition(GridColumns). This should also elegantly cover the scenario, when you building grid dynamically(foreach in gridcolumns etc.) with Visible property. And here we have nice centralized place where all definitions are - effective proven concept :) Any tips are welcomed, thanks.

### Response

**Yanislav** commented on 21 Jun 2023

Hello Michal, In general, the <GridColumns> are part of the component definition and since they are declared by the developer it is expected that he can access them. Regarding your question about a trick that allows you to iterate a RenderFragment, I'm not aware of any such existing method or approach. Technically there is an alternative, although it is not recommended. It involves accessing the internal Grid property called ColumnsCollection using Reflection. It's important to note that working with internal properties is not recommended. Note that such implementations can be unreliable and can lead to issues. That being said, the approach suggested by my colleague Marin seems to be the most effective solution. If you have any further questions or need further assistance, please feel free to let me know.

### Response

**Michal** commented on 21 Jun 2023

Hi Yanislav, thanks for the tip, helped a lot. Combining grid.GetState() and reflected column list gives together all "user friendly" info. :) Example how to get list of colum definitions: var _GridColumns=(gGirdReferenceVariabla.GetType().GetProperty(" ColumnsCollection ", BindingFlags.Instance | BindingFlags.NonPublic).GetValue(gGirdReferenceVariabla) as List<IColumn>); var FirstColumnTitle=_GridColumns .Where(x=>x is BoundColumnBase).First(). Title; As You said, its only for reading values, no-one should modify values this way. From the perspective of "grid column picker", its only for retrieving the Titles of all available columns. Other values are already present at gird.GetState().

### Response

**Yanislav** commented on 26 Jun 2023

Hello Michal, I'm glad to hear that my tip was helpful to you! It's great that you were able to retrieve all the information you needed. Regarding the example you provided, I want to caution you about accessing private properties directly. While it may work for now, it's generally not recommended to rely on private properties because they can be changed in future updates. Currently, there are no plans to change them, but it's important to be aware of this possibility. Instead, I suggest considering alternative approaches like the one suggested by my colleague.
