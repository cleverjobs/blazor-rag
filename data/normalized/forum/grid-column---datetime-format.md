# Grid Column - DateTime Format

## Question

**Mic** asked on 06 Aug 2020

Hello community! Is there a way to format the DateTime value of our model without using templates? Thanks in advance for any tip! <GridColumn Field=@nameof(WillyMachine.DateDebut) Title="Debut" Filterable="true" Editable="false" Width="100px" />

### Response

**Mario** commented on 24 May 2022

Hi, you can use: DisplayFormat="{0:dd/MM/yyyy} <GridColumn Field="@nameof(Journalhd.Feccom)" Title="Fecha" DisplayFormat="{0:dd/MM/yyyy}"> Best Regards

## Answer

**Marin Bratanov** answered on 06 Aug 2020

Hi Michael, When this feature gets implemented there will be: [https://feedback.telerik.com/blazor/1451067-add-attribute-format-for-grid-column-to-apply-c-standard-formats.](https://feedback.telerik.com/blazor/1451067-add-attribute-format-for-grid-column-to-apply-c-standard-formats.) I've added your Vote to it to raise its priority, and you can click the Follow button for email notifications. Regards, Marin Bratanov

### Response

**Michael** answered on 06 Aug 2020

You're the best Marin

### Response

**Zoya** answered on 15 Sep 2020

Hi, I have added my Vote also: date formats in the grid would be fine.. I want to try something a little bit different but still using templates. This code works right: <Telerik.Blazor.Components.GridColumn Field="@nameof(Security.ValidFrom)" Width="100px"> <Template> @((context as Security).ValidFrom.ToString("dd.MM.yyyy")) </Template> </Telerik.Blazor.Components.GridColumn> But I want to have "a dynamic grid" with DataTable Source: <GridColumns> @foreach (DataColumn col in DataTable.Columns) { switch (col.DataType.FullName) { case "System.Int32": <GridColumn Field="@col.ToString()" FieldType="@typeof(decimal)" Width="80px" /> break; case "System.DateTime": <GridColumn Field="@col.ToString()" FieldType="@typeof(DateTime)" Width="100px" /> break; case "System.Boolean": <GridColumn Field="@col.ToString()" Width="70px"> <Template> @{ <input type="checkbox" Editable="true"/> } </Template> </GridColumn> break; default: <GridColumn Field="@col.ToString()" FieldType="@typeof(string)" Width="200px" /> break; } } In this case I didn't find any way to set the DateTime Format. Thank you for your time!

### Response

**Marin Bratanov** answered on 15 Sep 2020

Hi Zoya, You can use templates in columns generated in a loop too. The key thing is that you must obtain the necessary value from the row model (in this case it would be a dictionary with the row data extracted from the DataTable as per this demo ). Then you might need to cast it to the appropriate data type before you can use .ToString(format). Regards, Marin Bratanov

### Response

**Zoya** answered on 16 Sep 2020

Hi Marin, thank you very much for your quick response. I just changed it and it works this way: case "System.DateTime": <Telerik.Blazor.Components.GridColumn Field="@col.ToString()" FieldType="@typeof(DateTime)" Width="100px"> <Template> @Convert.ToDateTime((context as Dictionary<string, object>)[col.ColumnName]).ToString("dd.MM.yyyy") </Template> </Telerik.Blazor.Components.GridColumn> break; case "System.Boolean" : <Telerik.Blazor.Components.GridColumn Field="@col.ToString()" FieldType="@typeof(bool)" Width="70px"> <Template> @{ var r=Convert.ToBoolean((context as Dictionary<string, object>)[col.ColumnName]); <input type="checkbox" disabled @bind=r /> } </Template> </Telerik.Blazor.Components.GridColumn> break; Have a nice evening there!
