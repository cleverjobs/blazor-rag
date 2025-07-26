# Setting Field and Title in loop

## Question

**Ran** asked on 10 Nov 2019

Hi, Here's what I want to do @for (int i=0; i <14; i++) { <GridColumn Field="@CellDate + (i + 1).ToString()" Title="@SelectedStartDate.AddDays(i).ToShortDateString()" /> } But I can't seem to get it to compile. It throws and error: error RZ9986: Component attributes do not support complex content (mixed C# and markup). So I get that it doesn't support complex content. I can easily put one line per field, but I don't know the title until runtime. How to set the title as desired? Is there a way to throw this in a loop at all? Thanks ... Ed

## Answer

**Marin Bratanov** answered on 11 Nov 2019

Hello Ed, In Blazor, you must use @foreach loops. For some reason, they are the only loop that works, the "standard" @for loop does not. You can find an example of doing this in the following page: [https://feedback.telerik.com/blazor/1418456-bind-to-datatable.](https://feedback.telerik.com/blazor/1418456-bind-to-datatable.) If it matches your needs, you can also Vote for it and Follow it. Regards, Marin Bratanov
