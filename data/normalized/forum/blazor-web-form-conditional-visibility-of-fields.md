# Blazor Web Form Conditional Visibility of Fields

## Question

**Dav** asked on 12 Jun 2022

With a Blazor razor page, is there any way of having a FormItem Field conditionally visible in a TelerikForm dependant upon another field? Use case is where details about person are filled in by the person in question OR a second person. The second person details are only required if the submiiter isn't the person in question. The only ways I can think of doing this thus far are: Have two versions of the page, with a third directing page Have two versions of the form with only one visible depending upon the state of the condition. Both are not scalable if in the model there are several conditional fields. :(

## Answer

**Benjamin** answered on 16 Jun 2022

Yes, you can use a simple if-statement for that, as the ChildFragment of <TelerikForm> can contain razor code. Example: <TelerikForm Model="@MyModelObject"> <FormField Field="@nameof(MyModelClass.Person)"> <Template>...do stuff...</Template> </FormField> @if(string.IsNullOrEmpty(MyModelObject.Person)) { <FormField Field="@nameof(MyModelClass.SecondPerson)"> <Template>...do stuff...</Template> </FormField> } </TelerikForm> @code { private MyModelClass MyModelObject {get;set;} }

### Response

**David** commented on 21 Jun 2022

I did try something liek that. Mustn't have correctly bracketed the FormField.

### Response

**David** commented on 21 Jun 2022

Next question. How do conditionals on the context in a Grid? I'll post that.

### Response

**Hristian Stefanov** answered on 23 Jun 2022

Hi David, I'm glad to see that upgrading to the last version solved the case. Here is the public post about the last question for visibility: How to conditionally display grid cell data based upon the row context?. I'm marking the case as closed. Regards, Hristian Stefanov Progress Telerik
