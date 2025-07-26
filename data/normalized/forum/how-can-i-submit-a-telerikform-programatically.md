# How can I submit a TelerikForm programatically?

## Question

**Joh** asked on 02 Apr 2025

I have a form that has a single editable field. When that field has a value put into it there is a method that validates the value and fills in the rest of the fields based on the value. That method then should also trigger a submit. I do not want the UI portion of the form to change or respond with a confirmation. I do need the record Id that is created when the form is submitted. So basically Put a value into a field. Fill out the rest of the form automatically based on the above value & submit the form data to my DB and return a record Id. That retrieved Id is then fed to another component that resides in a window control on the original form component. Ideally there would be way to use a form ref to submit the form... i.e. myFormRef.Submit()

## Answer

**Dimo** answered on 03 Apr 2025

Hello John, The Telerik Blazor Form doesn't perform HTTP POST requests, so there is no need to submit it programmatically. If the Form values are already validated (which you can do programmatically if needed), then you can simply obtain the values from the Form Model object and save them to the database. Regards, Dimo

### Response

**Anislav** answered on 05 Apr 2025

John, I’ve prepared an example at: [https://blazorrepl.telerik.com/wpYSYzbG19GCJZZl57](https://blazorrepl.telerik.com/wpYSYzbG19GCJZZl57) that demonstrates a form where the name is the only field to be populated. When this field is filled out, it automatically updates the first and last names. Finally, the OnValidSubmit event of the TelerikForm is handled to generate an ID for the model. Regards, Anislav Atanasov
