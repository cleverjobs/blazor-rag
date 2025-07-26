# Problem with telerik component

## Question

**Dan** asked on 23 Aug 2020

Here is a copy of the component that i built for my form this is the component named "DataTextField" @inherits EagleCS.ComponentClasses.DataInputTextBase<string> <div class="form-group"> <label class="h6">@(TextLabel): </label> <TelerikTextBox @bind-Value="@Value"></TelerikTextBox> <ValidationMessage For="@ValueExpression"></ValidationMessage> </div> Here it is inside an EditForm <DataAnnotationsValidator /> <DataTextField TextLabel="Name" @bind-Value="screenModel.Name" /> When I click submit for the form even with a value inside it blanks out the text field and then set the field to be empty.

## Answer

**Marin Bratanov** answered on 24 Aug 2020

Hi Daniel, The DataTextField component must expose and raise a ValueChanged event when the field value actually changes, and that usually happens on an input event - like ValueChanged or OnChange, and I see neither in this code. This ValueChanged event allows the @bind-Value syntax and the framework relies on it being raised with the correct new data in order to update the parent view-model. Regards, Marin Bratanov
