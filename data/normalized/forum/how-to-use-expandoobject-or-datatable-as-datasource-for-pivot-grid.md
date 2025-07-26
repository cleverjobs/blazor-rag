# How to use expandoObject or datatable as datasource for Pivot Grid?

## Question

**LeoLeo** asked on 03 May 2024

I'm Currently developing dynamic pivot grid for that i need to use expandoObject or datatable as datasource

## Answer

**Hristian Stefanov** answered on 03 May 2024

Hi Leo, I confirm that it is not possible to directly bind the PivotGrid to ExpandoObject or DataTable. What you can do is convert the data source to an appropriate format - the documentation on local data binding can be used as a reference: [https://docs.telerik.com/blazor-ui/components/pivotgrid/data-binding#local.](https://docs.telerik.com/blazor-ui/components/pivotgrid/data-binding#local.) I hope this will help you move forward with the implementation on your end. Regards, Hristian Stefanov Progress Telerik

### Response

**Leo** commented on 03 May 2024

Thanks Hristian, Is there any way to bind data dynamically into pivotgrid without using models if there so it can be very helpful

### Response

**Hristian Stefanov** commented on 07 May 2024

Hi Leo, I confirm that the PivotGrid data binding requires the usage of a model. Kind Regards, Hristian
