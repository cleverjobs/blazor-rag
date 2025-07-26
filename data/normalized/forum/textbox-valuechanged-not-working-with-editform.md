# TextBox ValueChanged not working with EditForm

## Question

**Mic** asked on 29 Mar 2020

I've tried getting this to work a number of ways, but it appears that using the 'ValueChanged' event with the Telerik TextBox is incompatible with <EditForm>. The attached code generates an error using the <EditForm> tag. Works fine if its commented out. The TextBox works fine with EditForm but without ValueChanged defined. Any ideas? @page "/testpage" <EditForm Model="contactName" OnValidSubmit="OnValidSubmit"> <DataAnnotationsValidator /> from the handler: @result <br /> from model: @contactName.LastName <br /> <TelerikTextBox ValueChanged="@( (string s)=> MyValueChangeHandler(s) )" Value="@contactName.LastName"> </TelerikTextBox> @*<TelerikTextBox @bind-Value="@contactName.LastName" />*@<ValidationMessage For="@(()=> contactName.LastName)" /> <div> <button class="btn btn-primary" type="submit">OK</button> </div> </EditForm> @code { string result; public Contact contactName { get; set; }=new Contact(); private void MyValueChangeHandler(string theUserInput) { result=string.Format("The user entered: {0}", theUserInput); //you have to update the model manually because handling the ValueChanged event does not let you use @bind-Value contactName.LastName=theUserInput; } private void OnValidSubmit() { result="Form Submitted"; } public class Contact { public int NameId { get; set; } public string FirstName { get; set; } [System.ComponentModel.DataAnnotations.Required(ErrorMessage="You must enter a Last Name.")] public string LastName { get; set; } } }

## Answer

**Marin Bratanov** answered on 30 Mar 2020

Hi Michael, You can read more about this error and how to solve it in this article: [https://docs.telerik.com/blazor-ui/knowledge-base/requires-valueexpression](https://docs.telerik.com/blazor-ui/knowledge-base/requires-valueexpression) Here's the simplest change: <TelerikTextBox ValueChanged="@( (string s)=> MyValueChangeHandler(s) )" Value="@contactName.LastName" ValueExpression="@( ()=> contactName.LastName )"> </TelerikTextBox> And you may also find this article interesting: [https://docs.telerik.com/blazor-ui/knowledge-base/textbox-validate-on-change](https://docs.telerik.com/blazor-ui/knowledge-base/textbox-validate-on-change) Regards, Marin Bratanov

### Response

**Michael** answered on 30 Mar 2020

Thanks! And thanks for all of the quick replies.
