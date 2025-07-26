# Always show selected rows - Filter as Or Selected

## Question

**JonJon** asked on 02 Aug 2021

Users would like any row selected not be filtered out of display. new FilterDescriptor ( nameof ( Selected ), FilterOperator. IsEqual, true )?

## Answer

**Marin Bratanov** answered on 03 Aug 2021

Hello Jon, You can use the OnRead event of the grid to provide the current page of data to it with your own code (see more here ). This means that you can take into account the selected items it currently has and implement the desired logic to put them where you want them to be. The Data can be filtered, sorted, paged without any regard to selected items, this is an important separation between these features and the grid cannot, out-of-the-box, change that behavior, the data cannot be coupled with row selection, or cell selection or other such UI gimmicks. Regards, Marin Bratanov
