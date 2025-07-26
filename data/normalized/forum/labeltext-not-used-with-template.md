# LabelText not used with template

## Question

**Mau** asked on 23 Mar 2021

Hi, I have a form with the same type of error if I use a TelerikSwitch or a TelerikDropDownList in the Template <FormItem Field="Bill" LabelText="Billable"> <Template> <TelerikSwitch @bind-Value="@Project.Billable" OffLabel="No" OnLabel="Yes"></TelerikSwitch> </Template> </FormItem> The text in LabelText isn't visible. and the Form layout is "broken". Without LabelText the name of the Field isn't whown either

## Answer

**Svetoslav Dimitrov** answered on 23 Mar 2021

Hello Maurice, The Template lets you control the rendering of the FormItem, thus the LabelText is not present. In order to provide a label that is styled like the default one from the TelerikForm, you can apply some CSS classes to the standard HTML <label> element. Below, I have created an example that might serve you as a base: @using System.ComponentModel.DataAnnotations <TelerikForm Model="@person"> <FormValidation> <DataAnnotationsValidator /> </FormValidation> <FormItems> <FormItem> <Template> <label for="numeric-id" class="k-label k-form-label"> Id </label> <TelerikNumericTextBox @bind-Value="@person.Id" Id="numeric-id"> </TelerikNumericTextBox> </Template> </FormItem> <FormItem> <Template> <label for="first-name" class="k-label k-form-label"> First Name </label> <TelerikTextBox @bind-Value="@person.FirstName" Id="first-name"> </TelerikTextBox> </Template> </FormItem> <FormItem> <Template> <label for="last-name" class="k-label k-form-label"> Last Name </label> <TelerikTextBox @bind-Value="@person.LastName" Id="last-name"> </TelerikTextBox> </Template> </FormItem> </FormItems> </TelerikForm> @code {
public Person person=new Person();

public class Person
{
[Range(100, 1000, ErrorMessage="The Id must be between 100 and 1000")]
public int Id { get; set; }
[Required]
[MaxLength(20, ErrorMessage="The first name should be maximum 20 characters long")]
public string FirstName { get; set; }
[Required]
[MaxLength(25, ErrorMessage="The last name should be maximum 25 characters long")]
public string LastName { get; set; }
}
} Let me know if you have any further questions. Regards, Svetoslav Dimitrov Progress Telerik
