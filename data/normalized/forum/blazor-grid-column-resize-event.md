# Blazor Grid Column Resize Event

## Question

**Joh** asked on 18 Aug 2021

Hi, My PM is wanting us to capture the column resize event and save this so when a user comes back to a certain page the column widths are set to the previous widths they set. Is there a way to capture the a column resize width and the widths of the columns? Thanks

## Answer

**Matthias** answered on 19 Aug 2021

Hi John, there are several ways to do this. The simplest way is GridState: documentation and an example Alternatively, you can use the OnStateChanged event and save the column width: State event for example: OnStateChanged="@((GridStateEventArgs <dtoObj> args)=> OnStateChangedHandler(args))" void OnStateChangedHandler ( GridStateEventArgs<dtoObj> args ) { foreach ( var item in args.GridState.ColumnStates)
{ // Width }
}
