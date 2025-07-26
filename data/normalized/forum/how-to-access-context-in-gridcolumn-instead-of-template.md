# How to access context in GridColumn instead of Template?

## Question

**Ste** asked on 25 Nov 2021

Hi, Usually you can easily get the context by doing the following: <GridColumn Field="PostalCode">
<Template>
@{ var item=context as Hostel; //stuff happens }
</Template>
</GridColumn> I have overridden the Telerik GridColumn with my own GridColumn, and I want to be able to pass the context as a parameter to my own GridColumn, like this: <GridColumn Item="@context" Field="PostalCode"></GridColumn> Is this possible?

### Response

**Dimo** commented on 25 Nov 2021

The second syntax means that context should come from <GridColumns> or from the <Grid>. Neither of them expose it, however. What are you trying to accomplish?

### Response

**Stefan** commented on 25 Nov 2021

I feel like my English is too limited to give a proper explanation, but basically I want to be able to pass the value in the column (for example the PostalCode like above) to the GridColumn class I made, which inherits from the Telerik GridColumn, so I can do something with the value based on business logic.

### Response

**Dimo** commented on 26 Nov 2021

There can be multiple rows (PostalCode values) and only one PostalCode column. So it is unclear to me which context (data item) should be used by the column. In case you want to customize each table cell from the column, based on the PostalCode value, you can use the OnCellRender event for this.
