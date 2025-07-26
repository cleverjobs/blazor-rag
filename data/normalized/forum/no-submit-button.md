# No submit button?

## Question

**Dav** asked on 25 Feb 2021

Hello, I am trying to use the form control as a read only output of my model. How can I set the form to read only and get rid of the submit button?

## Answer

**Marin Bratanov** answered on 25 Feb 2021

Hello David, That sounds like a scenario for something like a PropertyGrid. You should Follow the implementation of such a component here (your Vote is already in). The Form is explicitly an Edit component, it is designed for taking user input and letting the application use it. Nevertheless, our next version will use the [Editable] data annotation attribute, so you could mark your model fields with [Editable(false)] so the editors (input) the Form renders will be disabled, but that is still not what the form is for, and might not even be feasible for your model. Regards, Marin Bratanov

### Response

**Michael** answered on 08 Mar 2021

Add an empty <FormButtons> element to the root for, like so: <TelerikForm> ... Items code ... <FormButtons> @* Intentionally blank: FormButtons - RenderFragment - allows you to add custom buttons to the Form. You can use the FormButtons tag to add a Clear button to the Form. If the FormButtons tag is defined there will be no default buttons in the Form. *@</FormButtons> </TelerikForm>
