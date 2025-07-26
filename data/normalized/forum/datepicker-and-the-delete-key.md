# DatePicker and the delete key

## Question

**Dea** asked on 22 Jun 2021

I have a DatePicker bound to a non-nullable DateTime property. If the user presses delete on a part of the date, that part is reset, and the error shown is "The date format is not parsable. Please enter valid date" rather than the validation message defined in the validator class. It's then impossible to get rid of this message other than by typing in a valid date. Selecting with the actual picker does not work. I have made a video to demonstrate: [https://youtu.be/twCXE4jTTJs](https://youtu.be/twCXE4jTTJs) <TelerikDatePicker Id="dpStartDate" @bind-Value="CurrentlyEditedItem.StartDate" Width="100%" Format="dd/MM/yyyy"></TelerikDatePicker> public Validator() { RuleFor(x=> x.SiteId).NotEmpty().WithMessage("Please select a site"); RuleFor(x=> x.StartDate).NotEmpty().WithMessage("Please supply a start date"); }

## Answer

**Nadezhda Tacheva** answered on 25 Jun 2021

Hi Dean, The reason behind the behavior you are getting stems from the data type used in this scenario as binding the DatePicker to DateTime and Nullable DateTime can result in different user experience and values that it will output. More details on that you can find in this section of the overview article for DateInput, it is valid for the other date pickers as well. In summary, when using non-nullable DateTime and you delete a segment of the input, the input is not valid until you enter another value for this segment. By that time, since it is actually treated as invalid, it cannot be parsed and the validation error occurs. The solution in this case will be to use nullable DateTime. Thus, when modifying a part of the input, if some parts are not defined(deleted), the value remains null and no validation error will be shown. I hope you will find the above information useful. If any further questions appear, please do not hesitate to contact us. Thank you for choosing Telerik UI for Blazor! Regards, Nadezhda Tacheva
