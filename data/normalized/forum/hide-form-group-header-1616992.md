# Hide form group header

## Question

**Sar** asked on 20 Jul 2023

I have a form which has 2 columns in one of the columns in one row I need to have two nested columns, but need to hide the header line since there is no header text. how can I hide the header line?

## Answer

**Georgi** answered on 24 Jul 2023

Hi, Sarah Based on the provided information, I suspect that you would like to hide the header line that appears under the LabelText, is that correct? If yes, this can be accomplished by using CSS. I have prepared a REPL example where you can see it in action. A class can be added to the form group via the Class parameter: <FormGroup Columns="2" ColumnSpacing="15px" Class="no-headers-form"> And, use a class selector to hide the line: <style>.no-headers-form.k-form-legend { display: none;
}
</style> Let me know if additional questions arise. Kind Regards, Georgi Progress Telerik
