# Auto fit grid column resize also fixed ones: how to avoid?

## Question

**Cla** asked on 29 Feb 2024

Hi, i use Grid.AutoFitAllColumnsAsync() to resize column width based on column content. Now, this method resize also non resizable columns ( Resizable="false" ) I would like to apply autofit only on resizable columns, how to solve? I would use AutoFitColumnsAsync() method but i need a generic way to apply it excluding non resizable columns. There is a way to read from code the Resizable property of columns?

## Answer

**Claudio** answered on 01 Mar 2024

I solved the issue with a workaround. I have done an extension method who auto fit all resizable columns. To determine if a column is resizable i used reflection to access the internal property Column of GridColumnState object. Can be an acceptable solution? It would be glad to update telerik library exposing the Column property as public, so all other column properties would be accessible. public static async Task AutoFitResizableColumnsAsync <T>( this Telerik.Blazor.Components.TelerikGrid<T> grid ) { var gridState=grid.GetState(); var columns=new List<string>(); var columnProperty=typeof (Telerik.Blazor.Components.Common.Grid.State.GridColumnStateBase).GetProperty( "Column", BindingFlags.Instance | BindingFlags.NonPublic); foreach ( var colState in gridState.ColumnStates)
{ var column=(Telerik.Blazor.Common.Columns.IColumn)columnProperty.GetValue(colState); if (column.Resizable)
columns.Add(colState.Id);
} if (columns.Count> 0 ) await grid.AutoFitColumnsAsync(columns);
}

### Response

**Dimo** commented on 05 Mar 2024

Hi Claudio, The demonstrated approach may work, but I am not sure it follows best practices in Blazor. Normally, Blazor uses declarative component configuration and the app always knows what the component configuration is. From this point of view, there should be no need for the application to extract component information with reflection. For example, you can create a Dictionary that holds information about the resizability of all columns. Use this Dictionary to set the Resizable parameter for all columns, and also, define which columns should be auto fitted. For things that are controlled by the user and can change at runtime, we provide the Grid state: Grid State documentation Grid column state KB Column resizability cannot be changed by the user, so it's not part of the Grid state.
