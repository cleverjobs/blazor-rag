# TelerikGrid with DetailTemplate has wrong colspan

## Question

**Hol** asked on 08 Nov 2022

Hello, Update: Solved it with css. I have a TelerikGrid like: <TelerikGrid Data="@MainViewModels">
<DetailTemplate> var details=context as DetailViewModel;

<TelerikGrid Data="details.Details">
<GridColumns>
<Grid Column Field="Title" />
</GridColumns>
</TelerikGrid>
</DetailTemplate>

<GridColumns>
<GridColumn Field="Field1" />
<GridColumn Field="Field2" />
<GridColumn Field="Field3" />
</GridColumns>
</TelerikGrid> 4 columns are generated: one <td class="k-hieracrchy-cell" role="gridcell"> and three <td class=" " role="gridcell"> columns. But in <tr class="k-detail-row"> -> <td class="k-detail-cell"> there is colspan="3" instead of 4. So the details do not have the full width of the table. How do I set the colspan to 4 or expand the detail table to the full width of the parent table? Thanks

## Answer

**Nadezhda Tacheva** answered on 10 Nov 2022

Hi Holger, The described behavior is expected by design. The <tr class="k-detail-row"> contains two cells: <td class="k-hierarchy-cell"> - it is aligned with the hierarchy cell of the parent Grid. <td class="k-detail-cell"> - it is aligned with the actual data columns of the parent Grid. The colspan of this cell will match the number of declared columns the parent Grid has in order to keep that alignment. In your scenario, the parent Grid has three columns, so the colspan of the detail cell is 3. You are correct that this can be altered with some CSS to achieve the desired result. I am glad that you now have a working solution on your end. Please let us know if any other questions are raised. Regards, Nadezhda Tacheva
