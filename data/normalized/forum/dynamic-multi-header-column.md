# Dynamic Multi Header Column

## Question

**Moz** asked on 19 Sep 2023

Hello, I want to create a grid like this with Telerik Blazor Grid: Is it possible to do this using Multi Column Header function ? here's my code : @{
strMonth=string.Empty;
iWeek=0;
<GridColumn Field="@dtGrid.Columns[0].ColumnName" FieldType="@dtGrid.Columns[0].DefaultValue.GetType()" Width="150px"></GridColumn> //Member <GridColumn Field="@dtGrid.Columns[1].ColumnName" FieldType="@dtGrid.Columns[1].DefaultValue.GetType()" Width="150px"></GridColumn> //Project for ( int colMonth=2; colMonth <=dtGrid.Columns.Count - 1; colMonth++)
{ if (DateTime.TryParse(dtGrid.Columns[colMonth].ColumnName, out dt))
{ if (strMonth !=dt.ToString( "MMMM" ))
{
strMonth=dt.ToString( "MMMM" );

<GridColumn Title="@strMonth" FieldType="@dtGrid.Columns[0].DefaultValue.GetType()">
<Columns>
@{
iWeek=Helper.Common.GetWeekOfYear(dt); for ( int colWeek=colMonth; colWeek <=dtGrid.Columns.Count - 1; colWeek++)
{ if (DateTime.TryParse(dtGrid.Columns[colWeek].ColumnName, out dt))
{ if (strMonth !=dt.ToString( "MMMM" ))
{
colMonth=colWeek; break;
} if (iWeek !=Helper.Common.GetWeekOfYear(dt))
{
colMonth=colWeek; break;
}
<GridColumn Title="@string.Format(" Week { 0 } ", iWeek)" FieldType="@dtGrid.Columns[0].DefaultValue.GetType()">
<Columns>
@for ( int iDay=colWeek; iDay <=dtGrid.Columns.Count - 1; iDay++)
{ if (DateTime.TryParse(dtGrid.Columns[iDay].ColumnName, out dt))
{ if (iWeek !=RR.BusinessLogicLayer.Helper.Common.GetWeekOfYear(dt))
{
colWeek=iDay; break;
}
<GridColumn Field="@dt.Day.ToString()" FieldType="@dtGrid.Columns[colWeek].DefaultValue.GetType()" Width="150px"></GridColumn>
}
}
</Columns>
</GridColumn>
}
}
}
</Columns>
</GridColumn>
}
}
}
} Above code only can get me until Month Column, when i debug it iWeek only fires after all column rendered ? so , it can't create the Child Column of Months Column. How can i fix it so it can show Multi Header of Months, Week and Day
