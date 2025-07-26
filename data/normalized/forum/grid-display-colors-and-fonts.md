# Grid Display colors and fonts?

## Question

**Dea** asked on 09 Sep 2022

I would like in C# code behind, to set the Header background color and Font Color & Bold it. How can I do that? Something like: Grid.Columns.Header.BAckground=NAvy Grid.Columns.Header.font.color=White Grid.Columns.Header.font.bold=true Also want to do a alternate row coloring setup. How'd I do that? Is there a render event I can use? Thanks Deasun

## Answer

**Dimo** answered on 13 Sep 2022

Hi Deasun, To style the Grid header cells, set custom CSS classes via the HeaderCell parameter of the GridColumn. We don't support inline styles at this point. The Grid applies alternate row backgrounds by default. If you want to further customize the looks of rows and cells, use the OnRowRender and OnCellRender events. They allow you to set custom row and cell CSS classes. To apply random custom styles, including font changes, check this KB article about reducing the Grid font size with custom CSS. Regards, Dimo
