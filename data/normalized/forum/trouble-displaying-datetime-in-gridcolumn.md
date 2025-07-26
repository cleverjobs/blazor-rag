# Trouble displaying datetime in GridColumn

## Question

**Hen** asked on 25 Apr 2023

Hi, I'm trying to display the local datetime using this code but it just shows up empty. <GridColumn Field="@(nameof(Dto.DateTimeOffset.LocalDateTime))" Title="Date" /> If I remove .LocalDateTime it works but then it shows the incorrect local time.

## Answer

**Justin** answered on 25 Apr 2023

Hi Henrik, Try calling the LocalDateTime method on the Dto.DateTimeOffset field in a Column Template like this: <GridColumn Field="@nameof(Product.Released)" Title="Released"> <Template> @{
var product=context as Product;
var time=product.Released; <span> @time.LocalDateTime.ToString("F") </span> } </Template> </GridColumn> Here is a running example in our REPL. I hope this helps. Regards, Justin Progress Telerik

### Response

**Henrik** commented on 25 Apr 2023

Thanks for the quick reply. Is there anyway to simplify/reuse it because I need todo it in a lot of places with multiple dates per grid? Regards, Henrik

### Response

**Dimo** commented on 28 Apr 2023

@Henrik - there are a couple of options - Add one more property in the Grid model class, which has a custom getter and returns the above expression. Bind the column to that property. In this case you won't need a column template, but all data operations for this column will start working on a string property. Implement reusable Grid column template.
