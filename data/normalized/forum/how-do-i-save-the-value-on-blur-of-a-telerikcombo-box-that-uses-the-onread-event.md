# How do I save the Value on Blur of a TelerikCombo-Box that uses the OnRead-Event?

## Question

**Col** asked on 26 Jan 2024

I have a TelerikComboBox that uses the OnRead-Event inside of an EditForm. Binding the selected Value (an Id of type "long") using bindValue to my model in the Edit form is not the problem. However when the component loses focus the selected value resets and I can't submit the form. I guess this is just the default behavior. Using the ValueChanged-Event I realized that it fires not only on selection but also when the component loses focus, which is only the case when using the OnRead-Event. Is there a way for me to disable the firing of the ValueChanged-Event on Blur? This is my ComboBox: <EditForm Model="model" OnValidSubmit="HandleValidSubmitAsync"> <FluentValidator> </FluentValidator> <p> Selected Value: @model.UserId </p> <p> <label class="required" for="..."> @FieldsLoc["..."] </label> <TelerikComboBox TItem="Model" TValue="long" OnRead="@ReadItems" @bind-Value="model.UserId" ValueField="Id" TextField="DisplayName" Filterable="true" FilterOperator="StringFilterOperator.Contains" Width="100%"> </TelerikComboBox> <ValidationMessage For="@(()=> model.UserId)"> </ValidationMessage> </p> <TelerikButton OnClick=@(args=> createDialogOpen=false)>@AppLoc["Cancel"] </TelerikButton> <TelerikButton ThemeColor="@ThemeConstants.Button.ThemeColor.Primary"> @AppLoc["Save"] </TelerikButton> </EditForm>

### Response

**Colin** commented on 26 Jan 2024

So I solved the Problem that I had but it wasn't due to the ValueChange-Event. The Problem happened because my args.Data wasn't initialized with any sort of List in case the user hasn't input something already, which somehow caused this Problem to happen. Changed: args.Data=new List <ExtranetUserViewModel> (); To: args.Data=users; With users being a List that's already been initialized before.

### Response

**Hristian Stefanov** commented on 29 Jan 2024

Hi Colin, I'm happy to see you quickly resolved the matter on your own. Thank you for sharing it here, publicly, so other developers can benefit from it. Kind Regards, Hristian
