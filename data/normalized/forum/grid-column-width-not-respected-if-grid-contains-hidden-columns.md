# Grid column width not respected if grid contains hidden columns

## Question

**Cla** asked on 12 Oct 2021

In the documentation is stated: When only some column widths are set and the cumulative width of columns with set widths is less than the available Grid width, the widths of the columns with a set width are respected and the remaining width is distributed evenly between the other columns. [https://docs.telerik.com/blazor-ui/components/grid/columns/width](https://docs.telerik.com/blazor-ui/components/grid/columns/width) This behaviour work well if the columns in the grid are all visibles. If there are some invisible columns (property Visible="false") the remaining width is NOT distributed between the other columns (columns without Width property). Example1: Col1 Width="10px"

Col2 Width="10px"

Col3 (without width property)

Col4 Width="10px" in this situation Col3 is sized correctly based on the remaing width. Example2: Col1 Width="10px"

Col2 Width="10px" Visible="false"

Col3 (without width property)

Col4 Width="10px" in this situation Col3 is sized based on the remaing width BUT also Col4 width is changed! Any suggestion? Thanks

### Response

**Claudio** commented on 12 Oct 2021

Issue solved, it's my mistacke writing the width attribute. Sorry
