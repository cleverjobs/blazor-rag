# template context value

## Question

**Dav** asked on 15 Oct 2020

So I want make a component that encapsulates your grid column component and then drive the look from a database table (aka width and type). for numeric columns I want to align right . The problem is that the type of object is not known so i cannot cast it like you have done in your right align template example code. Is there a way to get the reference field value into the template and not just the bound record object (aka context). or of course is there a better way to do this ?? Any help would be appreciated. @switch ((Dashboard.Enums.EColumnType)GridViewColumn.ColumnType) { case Enums.EColumnType.Numeric: <GridColumn Field="@GridViewColumn.FieldName" Title="@GridViewColumn.HeaderText" Width="@GridViewColumn.Width"> <Template> <div style="text-align: right;"> @((context as data).TargetProperty) </div> </Template> </GridColumn> break; case Enums.EColumnType.Currency: break; case Enums.EColumnType.Percentage: break; default: <GridColumn Field="@GridViewColumn.FieldName" Title="@GridViewColumn.HeaderText" Width="@GridViewColumn.Width" /> break; } @code { [Parameter] public GridViewColumn GridViewColumn { get; set; } }

## Answer

**Kristian** answered on 16 Oct 2020

Hi David, If I'm understanding your case correctly, you want to get the property type and property value of the object, but you don't know the object type. At the end of the post, you can find an attachment with sample code which aligns int columns to the right without knowing the type and value of the property which is related to that column. In the example, you will find a solution using GridColumn Template in which you can get the value and type using reflection. This approach is a bit more performance-optimized because won't create too much component instances in the memory which is the one thing that Microsoft point as a good practice. The key point is in the method GetColumnTemplate() where the template is generated. public RenderFragment<object> GetColumnTemplate ( string propName ) {
RenderFragment<object> ColumnTemplate=context=> __builder=>
{
PropertyInfo propertyInfo=context.GetType().GetProperty(propName); var propType=propertyInfo.PropertyType; var propValue=propertyInfo.GetValue(context); if (propType==typeof ( int ))
{
<div style="text-align: right;">
@propValue
</div>
} else {
@propValue
}
}; return ColumnTemplate;
} Here we get the name of the column and using Reflection we get its type and value from the object. Depending on the type of the column we render different HTML (with different alignment) You can see that the object is not cast to any type, so the solution is abstract enough and you can reuse it in multiple grids. On another note - our next release will have a ColumnRender event where you will be able to add classes conditionally so this might make things easier - you could add a CSS rule to align the contents to the right and also the upcoming DisplayFormat parameter can let you avoid the template altogether for formatting numbers and dates. You can preview how this will work here and here. Regards, Kristian

### Response

**David Ocasio** answered on 16 Oct 2020

thankyou kristian your code did indeed send me down the right road. I don't need to probe for the type in my case since that is driven by a specification table. I am a but concerned about using reflection since it can have a performance impact but it does seem to work well enough. i have enclosed the doctored code using your reflection solution for posterity. Yes it does sound like that columnrender event would be usefull to me again thankyou very much for your assitance @using System.Reflection; <GridColumn Field="@GridViewColumn.FieldName" Title="@GridViewColumn.HeaderText" Width="@GridViewColumn.Width" Template="@(GetColumnTemplate())" /> @code { [Parameter] public GridViewColumn GridViewColumn { get; set; } public RenderFragment<object> GetColumnTemplate() { RenderFragment<object> ColumnTemplate=context=> __builder=> { if (GridViewColumn==null) return; PropertyInfo propertyInfo=context.GetType().GetProperty(GridViewColumn.FieldName); if (propertyInfo==null) return; var propType=propertyInfo.PropertyType; var propValue=propertyInfo.GetValue(context); switch ((Dashboard.Enums.EColumnType)GridViewColumn.ColumnType) { case Enums.EColumnType.Numeric: <div style="text-align: right;"> @propValue </div> break; case Enums.EColumnType.Currency: break; case Enums.EColumnType.Percentage: break; default: @propValue break; } }; return ColumnTemplate; } }
