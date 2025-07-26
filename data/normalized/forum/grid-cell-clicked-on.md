# Grid cell clicked on?

## Question

**Dea** asked on 24 Feb 2023

I have a need to be able to click on a cell and then capture the value in that cell in codebehind. How can I do that? I tried to play around with Column Template but I am getting no where. :( Need a GridCell_OnClick event so I can grab the cell value the Row tis on and the Column tis in. Thanks Deasun.

### Response

**Deasun** commented on 24 Feb 2023

Partly working! :( <GridColumn Field="@nameof(gdMappedUnMappedCostsOVHDR.M2_Amt)" Title="@M2_Title"> <Template> @{ var item=context as gdMappedUnMappedCostsOVHDR; var decValueIS=item.M2_Amt; <div @oncontextmenu:preventDefault="true" @oncontextmenu:stopPropagation="true" @oncontextmenu="@( (MouseEventArgs e)=> ShowSpecialContextMenu(e, item.SourceOfCost, @M2_Title) )"> @decValueIS </div> } </Template> </GridColumn> <GridColumn Field="@nameof(gdMappedUnMappedCostsOVHDR.M3_Amt)" Title="@M3_Title"> <Template> @{ var item=context as gdMappedUnMappedCostsOVHDR; var decValueIS=item.M3_Amt; <div @oncontextmenu:preventDefault="true" @oncontextmenu:stopPropagation="true" @oncontextmenu="@( (MouseEventArgs e)=> ShowSpecialContextMenu(e, item.SourceOfCost, @M3_Title) )"> @decValueIS </div> } </Template> </GridColumn> public void ShowSpecialContextMenu(MouseEventArgs args,string strSourceOfCost, string strColWas) { try { // thru this way the user can Right-click on a cell and I can capture the Cells column name and the Rows other cell value. // then I can go do the Business Logic I would need to. // It would be much better from the users point of view if I could do this by just left-clicking on the cell they want more info on. } catch (Exception ex) { }; }

## Answer

**Svetoslav Dimitrov** answered on 01 Mar 2023

Hello Deasun, You can use the Template and the @onclick event on the wrapping <div>. I have added an example where you can easily reuse the same template across different columns: @using System.Reflection;

<TelerikGrid Data="@forecasts" Height="550px" Pageable="true">
<GridColumns>
<GridColumn Template="@(GetColumnTemplate(" Id "))" Field="Id" Title="Id" Width="100px" Editable="false" Groupable="false">
</GridColumn>
<GridColumn Template="@(GetColumnTemplate(" Date "))" Field="Date" Width="220px">
</GridColumn>
<GridColumn Field="Summary">
</GridColumn>
</GridColumns>
</TelerikGrid>

@code { private void OnClickHandler ( string field, object context, object value ) { var fieldName=field; var item=context as WeatherForecast; var cellValue=value;
}

List<WeatherForecast> forecasts { get; set; } protected override void OnInitialized ( ) {
GetForecasts();
} void GetForecasts ( ) {
forecasts=Enumerable.Range( 1, 20 ).Select(x=> new WeatherForecast()
{
Id=x,
Date=DateTime.Now.AddDays(x),
Summary="Summary" + x
}).ToList();
} public class WeatherForecast { public int Id { get; set; } public DateTime Date { get; set; } public string Summary { get; set; }
} public RenderFragment<object> GetColumnTemplate ( string propName ) { // Define the RenderFragment in your code // Its type matches the type of the Grid context - an object // The same as if you were defining it in the markup // The syntax for writing a RenderFragment is rather specific, note the lambda expressions RenderFragment<object> ColumnTemplate=context=> __builder=>
{ // in this example we pass the property name from the grid declaration // and we use reflection to extract the needed data. You don't have to // If you know the field or the type, you can cast and simplify this code as needed PropertyInfo propertyInfo=context.GetType().GetProperty(propName); var propType=propertyInfo.PropertyType; var propValue=propertyInfo.GetValue(context);

<div @onclick="@(()=> OnClickHandler(propName, context, propValue))">@propValue</div>
}; return ColumnTemplate;
}
} Regards, Svetoslav Dimitrov
