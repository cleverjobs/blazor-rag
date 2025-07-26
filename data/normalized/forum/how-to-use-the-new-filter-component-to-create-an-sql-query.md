# How to use the new Filter component to create an SQL query

## Question

**Fab** asked on 03 Mar 2022

Good morning all, I'm taking a look to the new Filter component, recently added to Telerik UI for Blazor. I'm using it to build conditions to send to a custom SQL Query generator which will build the where clauses mapping from the export of the filter component. At the moment I'm simply serializing the CompositeFilterDescriptor to JSON obtaining something like this: { "FilterDescriptors": [{ "Operator": 4, "Member": "Quantity", "Value": 25 }, { "Operator": 1, "Member": "Quantity", "Value": 40 }, { "Operator": 2, "Member": "OrderShipCountry", "Value": "France" }, { "FilterDescriptors": [{ "Operator": 17, "Member": "OrderShipName", "Value": "La maison d\u0027Asie" }, { "Operator": 18, "Member": "OrderShipName", "Value": "Victuailles en stock" }
], "LogicalOperator": 1 }
], "LogicalOperator": 0 } and I will have the Query Generator parse it, but if there are better strategies, please let me know. Thanks, have a nice day. PS: I tagged this question as General Discussion as it seems like a "Filter" tag is not available yet.

### Response

**Lane** commented on 05 May 2022

Did you get this working? Would you be willing to share the details of the Query Generator? Thanks.

## Answer

**Marin Bratanov** answered on 06 Mar 2022

Hi Fabrizio, That's a valid approach. Regards, Marin Bratanov
