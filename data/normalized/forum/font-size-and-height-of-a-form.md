# Font size and height of a Form

## Question

**Ali** asked on 19 May 2021

Hi, How can set the height of a Form and How can set font size of text in form items?

## Answer

**Svetoslav Dimitrov** answered on 21 May 2021

Hello Alireza, The TelerikForm is designed to accommodate the form fields that are part of it. Its height is a calculated value of multiple factors: The line-height (the height of the lines that separate the editors) and the height of the editors themselves. Below, I have added an example of how to decrease the font-size for the editors, limit the height of the line and reduce the size of the labels: <style>.custom-form-height.k-form,.k-form-inline { line-height: 1;
}.custom-form-height.k-form input { font-size: 8px;
}.custom-form-height.k-form label { font-size: 8px } </style> @using System.ComponentModel.DataAnnotations <TelerikForm Model="@person" Class="custom-form-height"> <FormValidation> <DataAnnotationsValidator /> </FormValidation> </TelerikForm> @code {
public Person person=new Person();

public class Person
{
[Editable(false)]
public int Id { get; set; }

[Required]
[MaxLength(20, ErrorMessage="The first name should be maximum 20 characters long")]
[Display(Name="First Name")]
public string FirstName { get; set; }

[Required]
[MaxLength(25, ErrorMessage="The last name should be maximum 25 characters long")]
[Display(Name="Last Name")]
public string LastName { get; set; }

[Required]
[Display(Name="Date of Birth")]
public DateTime? DOB { get; set; }
}
} Regards, Svetoslav Dimitrov
