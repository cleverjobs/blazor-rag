# Change grid column index in OnStateInit not working

## Question

**Cla** asked on 13 Dec 2024

Hi, my code use OnStateInit to change the column order, settings the GridColumnState.Index property. Now i found it not work anymore (i can't found the cause). This is a simplified version who reply the issue: grid is created with Col1 and Col2, in OnStateInit i revert the index of the columns so i assume who grid will render with Col2 and Col1 (inverted order) but seem not working. [https://blazorrepl.telerik.com/QeFwbnFd19xPAId547](https://blazorrepl.telerik.com/QeFwbnFd19xPAId547) What's wrong? Thanks

## Answer

**Dimo** answered on 13 Dec 2024

Hi Claudio, The OnStateInit handler should also take into account the checkbox column: private void OnGridStateInit ( GridStateEventArgs<GridData> args ) {
args.GridState.ColumnStates=new List<GridColumnState>
{ new GridColumnState() { Index=0 }, new GridColumnState() { Index=2 }, new GridColumnState() { Index=1 }
};
} Regards, Dimo Progress Telerik
