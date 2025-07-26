# Telerik Blazor Grid ForEach

## Question

**Ric** asked on 25 Oct 2021

I have the following grid. I the student has many different schools. How do I list the different schools in one column. <TelerikGrid Data="@openTipGridData" ...> <GridToolBar> </GridToolBar> <GridSettings> <GridPagerSettings InputType="PagerInputType.Input" PageSizes="@gobalPageSizesOptions" ButtonCount="5" /> </GridSettings> <GridColumns> <GridColumn Field="Student.FirstName" Title="First Name"></GridColumn> <GridColumn Field="Student.LastName" Title="Last Name"></GridColumn> <GridColumn Title="Schools"> <Template Context="Schools"> @foreach (DataColumn col in openTipGridData.Student.Schools) { } </Template> </GridColumn> <GridColumn Field="Encounter.AddDate" DisplayFormat="{0:dd MMM yy}" Title="Assigned To"></GridColumn> </GridColumns> </TelerikGrid>

### Response

**Marin Bratanov** commented on 26 Oct 2021

This pseudocode looks right, then you should choose how you want to render them in the cell and put the desired markup/component(s) in the foreach body. The only issue I see is that you must use the context variable, so something like <Template Context=" Schools "> @foreach (var item in Schools.TheSchoolsCollection) { } </Template>
