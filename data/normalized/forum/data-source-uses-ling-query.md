# Data source uses ling query

## Question

**ianian** asked on 21 Oct 2019

Hi Can anyone help with this please? The following HTML produces a satisfactory result in that all columns are populated: if (purchaseOrders==null) { <p><em>Loading...</em></p> } else { <table class="table"> <thead> <tr> <th>PO No.</th> <th>PO Date</th> </tr> </thead> <tbody> @foreach (var purchaseOrder in purchaseOrders) { <tr> <td>@purchaseOrder.PurchaseOrderId</td> <td>@purchaseOrder.PurchaseOrderDate.ToShortDateString()</td> <td>@purchaseOrder.Supplier.SupplierName</td> </tr> } </tbody> </table> } There is a linq query in a service file which retrieves data across the FK between "Purchase Order" and "Supplier". However the SupplierName column remains blank in the Telerik grid with the following code: <TelerikGrid Data="purchaseOrders" Height="800px" Pageable="true" PageSize=@PageSize Sortable="true" Groupable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow"> <GridColumns> <GridColumn Field="@(nameof(PurchaseOrder.PurchaseOrderId))" Title="PO No." Groupable="false" /> <GridColumn Field="@(nameof(PurchaseOrder.PurchaseOrderDate))" Title="PO Date" /> <GridColumn Field="@(nameof(PurchaseOrder.Supplier.SupplierName))" Title="Supplier" /> </GridColumns> </TelerikGrid> The HTML and Telerik grids use the same data source and models. Many thanks The

## Answer

**Marin Bratanov** answered on 22 Oct 2019

Hi Ian, At the moment, the grid does not support nested models, and you can Follow the implementation of such functionality in this page: [https://feedback.telerik.com/blazor/1432615-support-for-nested-complex-models.](https://feedback.telerik.com/blazor/1432615-support-for-nested-complex-models.) I've added your Vote for you, and you can find linked from it solutions (like using a template or implementing a flattened view-model). Regards, Marin Bratanov
