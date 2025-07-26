# Is there any way to disable the entire form?

## Question

**Dav** asked on 29 Mar 2024

I am using a form component as a read only display of my model. I am using auto generated fields and don't want to define my form items manually if I don't have to. Is there an easy way to disable the entire form?

## Answer

**Hristian Stefanov** answered on 01 Apr 2024

Hi David, The easiest way to disable the Form is to set the Editable data annotation attribute on the model properties to false. Here is an example I have prepared for you: @using System.ComponentModel.DataAnnotations <TelerikForm Model="@PersonModel" Width="300px"> <FormValidation> <DataAnnotationsValidator /> </FormValidation> <FormButtons> </FormButtons> </TelerikForm> @code {
private Person PersonModel { get; set; }=new Person() { FirstName="ReadOnly First Name", LastName="ReadOnly Last Name" };

public class Person
{ [Editable(false)] public int Id { get; set; } [Editable(false)] [Display(Name="First Name")]
public string FirstName { get; set; } [Editable(false)] [Display(Name="Last Name")]
public string LastName { get; set; }
}
} Let me know if the result covers your needs. Regards, Hristian Stefanov Progress Telerik
