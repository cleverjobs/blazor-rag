# DateTimePicker shows the placeholder when it is set to empty

## Question

**Twa** asked on 05 Aug 2024

Given the definition of a DateTimePicker component binded with a variable of type DateTime? (pic1.png) <FormItem Field="@nameof(CronTriggerViewModel.EndAt)"> <Template> <label for="endat" class="k-label k-form-label"> @L10n["UI-TRIGGERENDAT"] </label> <div class="k-form-field-wrap"> <TelerikDateTimePicker @bind-Value="@CronTriggerVM.EndAt" Placeholder=" " Id="endat" Format="G" /> </div> </Template> </FormItem> [ Display(ResourceType=typeof(Resources.Scheduler), Name="UI_TRIGGERENDAT" ) ] public DateTime? EndAt { get; set; }=DateTime.Now.AddDays( 1 ); Even though the placeholder is set to be empty, when the value is cleared, the placeholder still appears (pic2.png), and the field is marked as invalid even though no validation is configured (pic3.png). For more details, I have attached an animated gif showing what happens (video.zip). Is there any way to don't show the placeholder and avoid the input to be mark as invalid?

## Answer

**Nansi** answered on 08 Aug 2024

Hi Twain, If I understand correctly you are facing two issues: When does the placeholder appear When is the field marked as invalid Is that correct? Placeholder In the video that you provided the date that you see in the input field is the default value: public DateTime? EndAt { get; set; }=DateTime.Now.AddDays(1); If you remove the default value, the input field displays the Format only when the user focuses on the input field. I have prepared a REPL example to demonstrate this. You can read more about this behavior in the Placeholder parameter description. Red border The red border appears because the component value is not in the correct format and type and cannot be parsed. The form is valid and can be submitted. By design our DateTimePicker and similar components have the following behavior when their value is bound to a nullable DateTime: When the input is partially correct (for example M/d/2024 ) the red border appears. We keep the red border even if the component value is bound to a nullable DateTime because it is more user-friendly. We consider that it is good to indicate to the user that they have started filling in the date, but haven't finished it, even if it is not required to be filled in. When they want to input something in this field we want to indicate when the input is not valid. When the input is fully cleared, the red border shouldn't appear. This is a bug. I created a report on your behalf: [https://feedback.telerik.com/blazor/1660917-datetimepicker-should-not-get-red-border-when-bound-to-nullable-datetime-and-the-input-is-empty](https://feedback.telerik.com/blazor/1660917-datetimepicker-should-not-get-red-border-when-bound-to-nullable-datetime-and-the-input-is-empty) I added your vote there and as a creator, you are automatically subscribed to get status updates. In the meantime, I have also added a workaround in the public post. Last but not least, I'd like to thank you for reporting this behavior! As a small gesture of appreciation, I rewarded your account with some Telerik points. Regards, Nansi

### Response

**Twain** answered on 09 Aug 2024

Thanks Nansi for your response. I'll apply the workaround in the meantime. Regards. Twain.
