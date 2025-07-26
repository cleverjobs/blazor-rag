# Grid inherit/default parameters

## Question

**Mau** asked on 18 Feb 2021

Is it possible to create grid subcomponents which have a number of parameters set ? Simple example (not realistic) would be to have components like <SortableTelerikGrid> which is just the <TelerikGrid Sortable="true"> so instead of having to specify all parameters in each page we can get some default parameters going.

## Answer

**Marin Bratanov** answered on 19 Feb 2021

Hello Maurice, Yes, it is possible. Just create a component in your app, put the Telerik Grid on it and set its parameters as desired. Then, add a few parameters to your own component that expose the settings you want changeable and point the grid parameters to them. It would probably be a generic component that takes the grid Data as a parameter too. Regards, Marin Bratanov

### Response

**Tejinder** commented on 14 Dec 2021

Comment removed.

### Response

**Maurice** answered on 02 Mar 2021

Thanks, I managed to do this using only class as well, and that way I do not need to "proxy" all parameters. My next problem is trying to create new gridcolumn types. <TelerikGrid> <GridColumns> <GridColumnBoolean> Which should have a template to show 'deleted' or 'not deleted' for instance based on the column value. I have tried creating a .razor which contains a GridColumn but could not get it work. Also tried a class inheriting from gridcolumn with an override on the builder tree. What would you suggest would be the way to go ? This is a recurring thing for us. We want to have a certain template for all our boolean columns in all our grids so don't want to specify it everytime. We also would like to minimize code in the .razor file itself.

### Response

**Maurice** answered on 02 Mar 2021

I have managed to get it working. with fixed column name but I will fix that now public class BooleanColumn : Telerik.Blazor.Components.GridColumn { public BooleanColumn() { this.FieldType=typeof(bool); } protected override void OnParametersSet() { base.OnParametersSet(); this.Template=GetColumnTemplate("clt_deleted"); } public RenderFragment<object> GetColumnTemplate(string propName) { RenderFragment<object> ColumnTemplate=context=> __builder=> { Dictionary<string, object> rowdata=(Dictionary<string, object>)context; if ((bool)rowdata[propName]) { __builder.OpenElement(1, "div"); __builder.AddContent(2, "test"); __builder.CloseElement(); } }; return ColumnTemplate; } }

### Response

**Maurice** answered on 02 Mar 2021

simple this.Template=GetColumnTemplate(this.Field);
