# Component to use to simulate WinForms GroupBox

## Question

**NiV** asked on 09 Jul 2023

Which component can I use to simulate WinForms GroupBox, to group some fields in a square with a small title on the upper left? (See example in image1 from WinForms). The nearest thing I've found is FormGroup, but doesn't visually group fields in a square, shows only upper line with title (see example on image2, groups "Personal information" and "Employee information"). This way, if after the group I have other fields not in a group (so no title needed for them) the user doesn't know when the group finishes. Thank you.

## Answer

**Dimo** answered on 12 Jul 2023

Hi Fabio, You have two options: Override the CSS styles of our Blazor components and achieve the desired look. Use a FormItemsTemplates and create custom UI with the desired look. Here is an example for the first option. <TelerikForm Model="@person" Columns="2" ColumnSpacing="25px" Class="group-borders"> <FormValidation> <DataAnnotationsValidator> </DataAnnotationsValidator> </FormValidation> <FormItems> <FormGroup LabelText="Personal Information" Columns="2" ColumnSpacing="15px"> <FormItem LabelText="First Name" Field="@nameof(Person.FirstName)"> </FormItem> <FormItem LabelText="Last Name" Field="@nameof(Person.LastName)"> </FormItem> <FormItem LabelText="Age" Field="@nameof(Person.Age)" ColSpan="2"> </FormItem> <FormItem LabelText="Email" Field="@nameof(Person.Email)" ColSpan="2"> </FormItem> <FormItem LabelText="Company Name" Field="@nameof(Person.CompanyName)"> </FormItem> <FormItem LabelText="Position" Field="@nameof(Person.Position)"> </FormItem> </FormGroup> </FormItems> </TelerikForm> <style>.group-borders.k-form.k-form-fieldset { border: 1px solid red;
}.group-borders.k-form.k-form-legend { width: auto; border-width: 0; padding: 0. 3em;
} </style> @code {
public Person person { get; set; }=new Person();

public class Person {
public string FirstName { get; set; }

public string LastName { get; set; }

public int Age { get; set; }

public string Email { get; set; }

public string CompanyName { get; set; }

public string Position { get; set; }
}
} Regards, Dimo
