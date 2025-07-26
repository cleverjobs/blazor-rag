# Validate DatePicker control without EditForm

## Question

**AmsAms** asked on 22 Nov 2022

Is it possible to validate required DatePicker control without EditForm?

## Answer

**Dimo** answered on 25 Nov 2022

Hello Amit, Yes, it is possible. One option is to use the DatePicker's OnChange or ValueChanged event and validate the value manually with code. Another option is to use an EditContext: Bind the DatePicker to a [Required] property of a model class. Create an EditContext from an instance of the model class. Enable DataAnnotations validation for the EditContext. Validate the EditContext and get the validation messages. Regards, Dimo Progress Telerik
