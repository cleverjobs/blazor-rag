# DatePicker is not firing OnChange Event

## Question

**con** asked on 17 Jun 2020

Hi, This is my DatePicker: <TelerikDatePicker Min="@Min" Max="@Max" @bind-Value="@thePickerValue" Id="select-date" OnChange="@MyOnChangeHandler"></TelerikDatePicker> @code { public string newAppDat { get; set; } public DateTime Max=DateTime.Now.AddDays(180); public DateTime Min=DateTime.Now.AddDays(-60); private DateTime? thePickerValue { get; set; } private void MyOnChangeHandler(object theUserInput) { newAppDat=(theUserInput as DateTime?).Value.ToString("yyyymmdd"); } } I set a break point inside Handler but execution is not pausing on it when I pick new date in DatePicker. Please advise.

## Answer

**const** answered on 17 Jun 2020

never mind, sorry, I have to hit ENTER to fire one. I thought this fires when I'm picking new date

### Response

**Marin Bratanov** answered on 17 Jun 2020

Indeed, it requires an Enter click or that the input loses focus. It is, effectively, a confirmation event that the user accepts this value. If you want more immediate events, the ValueChanged can be of service, and you only needto populate the model yourself and remove the two-way bindnig. You can read more about both events and see how to use them in the docs: [https://docs.telerik.com/blazor-ui/components/datepicker/events.](https://docs.telerik.com/blazor-ui/components/datepicker/events.) Regards, Marin Bratanov

### Response

**Craig** commented on 19 May 2022

I don't think this is true. If you open the picker, click on a new start and end value the calendar automatically closes (i.e. loses focus) but no OnChange event is fired even though the dates are updated in the component/model. You have to reopen the calendar and press enter to make the event fire (and although there are some, I don't think most users navigate a date range picker through the keyboard). So in effect the user has changed the value of the model but no OnChange event is raised so we can react to it. That can't be the correct or desired behaviour? I know you can use EndValueChanged as a workaround but you have to start checking for nulls/min value to see if the user is actually setting the end date or just starting the process when really you'd expect a components OnChange event to fire when, you know, the values have changed? Could you not implement the workaround internally inside the component to fire the OnChange or use an intermediate value for binding on the component so the component manages the binding process? Either would allow the OnChange to be fired at the right time

### Response

**Marin Bratanov** commented on 22 May 2022

Hi Craig, This thread is originally for the DatePicker and in my tests that works as expected. Your question seems to be about the DateRangePicker and that behaves differently: [https://docs.telerik.com/blazor-ui/components/daterangepicker/events#onchange,](https://docs.telerik.com/blazor-ui/components/daterangepicker/events#onchange,) here is the relevant quote (emphasis mine for this case): The OnChange event represents a user action - confirmation of the current value. It fires when the user presses Enter in the input, or when the input loses focus. The focus will also be lost when the user starts clicking in the calendar popup. While that might not be the most accurate wording (feel free to click the "improve this article" link and suggest a better one if you find this confusing), this component is expected to behave differently than the plain date picker. The problem with this, in the context of the range picker, is that you cannot know the user intent, nor what they will do - it is a heuristic task. They can select the start of the range, but then stop, or they may type instead of use the popup. It is, basically, trying to tie DOM events, to user intent (not action), and to do that with 1 event from 2 inputs. There is simply no way to be 100% certain. They keyword from your question is "expect" - we can't "expect" or "foresee" what will happen. In the most common case, you need to update the view-model based on the user selections, and two-way binding provides that. For more advanced situation, the best I can offer is that the application implements necessary logic around what is available as events at the moment per the documentation. For example, you can add the intermediate field in the view-model, and compare against that to monitor for changes, check what changed (you can even check how long ago), and decide what the application needs to do.

### Response

**Craig** commented on 23 May 2022

Hi Marin, Thanks for the reply. You're correct, this is for the DateRangePicker component rather than the DatePicker. Let me know if you want this discussion in its own area. The advice in the online documentation seems to conflict with the intellisense documentation Specifies the callback that's called when the current value is committed (confirmed) by the user - either through the Enter key, or when the Component loses focus. I would argue the "Component" is the DateRangePicker and not just the input element associated with the component as when the input element loses focus you're still in the DateRangePicker component when using the calendar. It's something minor but could be confusing as the picker component automatically closes when the second date is selected. I think you may have misunderstood in regards to expectations. I'd agree we can't guess what the user is going to do next but the point was once the user has clicked on a first and second date the requirements for firing the OnChange event have been met. Those values have changed and we know the user did it. Whether it's by clicking on the first date with the calendar and then swapping to keyboard entry and pressing enter or by clicking on two entries on the calendar. I'd say it's reasonable to expect the event to fire in both of those circumstances but at the moment it only fires in one. An example would be a simple report page where once the start and end dates have changed the results would refresh. At the moment the only workaround (that I know of at least) is by hooking the EndValueChanged event but this requires extra checks because the event also fires when starting a selection (the end date resets to either null or the min datetime value). So in the EndValueChanged event you need to check whether this is the user changing the end value or the component because the selection has been reset. I believe hooking the EndValueChanged also means you can't use two way binding. Doing a quick google of daterangepickers what I'm suggesting seems to be the norm. Of the checks I did (just scrolling down the results and looking at each implementations demo page) they either implement an Apply/Cancel button so they're using that to fire the events (this also helps with validation/cancellation by the user) or once both dates are set the callback is fired (which is what I'm suggesting) The Apply/Cancel option [https://blazordaterangepicker.azurewebsites.net/](https://blazordaterangepicker.azurewebsites.net/) [https://www.syncfusion.com/blazor-components/blazor-daterangepicker](https://www.syncfusion.com/blazor-components/blazor-daterangepicker) [https://www.daterangepicker.com/#examples](https://www.daterangepicker.com/#examples) The callback fired option [https://demos.devexpress.com/MVCxDataEditorsDemos/Editors/DateRangePicker](https://demos.devexpress.com/MVCxDataEditorsDemos/Editors/DateRangePicker) [https://longbill.github.io/jquery-date-range-picker/](https://longbill.github.io/jquery-date-range-picker/) Telerik's implementation is the only example I can find where you set the data using the most common method (mouse to set both dates) and it doesn't raise a OnChange or callback event to allow us to react to the change without having to implement other checks to make sure this event is actually from the end user.

### Response

**const** answered on 17 Jun 2020

I have a feeling that "event confirmation" you are talking about, is rather a work around the issue/limitation on development site than kind of care of users. Why I need to confirm the choice I just made a millisecond ago? The real name of that Event is "OnFocusLost" I would say. Correct me if I'm wrong.

### Response

**Marin Bratanov** answered on 17 Jun 2020

It also fires when an item is selected from the dropdown. It also fires on Enter key which is commonly used by users to confirm a value (e.g., as they tab through a form). It also fires in a few other cases with other inputs (e.g., multiselect) and this name keeps consistency among all of them. Last but not least, it does not interfere with two-way binding while still providing you with the value. Regards, Marin Bratanov

### Response

**const** answered on 17 Jun 2020

That last thing is actually most valued one. Thank you
