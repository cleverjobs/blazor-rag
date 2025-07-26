# Format when Null

## Question

**TimTim** asked on 22 Feb 2021

There are a few issues with the "Format" parameter. Are we missing something? Example: <TelerikDateTimePicker Format="f" @bind-Value="@CurrentDate" Id="f-standard"></TelerikDateTimePicker> Using the above code, when the date and time is null it shows "f" in the text input. Why? Shouldn't it at least show the proper format. If we write the format using the .NET format instead of shorthand it shows fine but we prefer that when the field is null it shows nothing (empty). Can this be done? Why didn't you wire up (support) the "placeholder" attribute of the input and allow us to set our own placeholder which could take place of the value in "Format"? Also, if we set Format="", it will keep the field empty like we desire but then when a date is selected it's in a format that we don't expect or want. Why don't you create controls that follow the html standard? If you are attaching a date and time picker to an input, why don't you support all html specification attributes of the input? Showing the date format in the input is ugly and not desirable. See the attached images.

## Answer

**Tim** answered on 22 Feb 2021

I've since evaluatedthe date and time picker from other providers and the placholder is supported. Syncfusion: <SfDateTimePicker TValue="DateTime?" Placeholder="Select a date and time"></SfDateTimePicker> DevExpress: <DxDateEdit @bind-Date="@DateTimeValue"ClearButtonDisplayMode="DataEditorClearButtonDisplayMode.Auto"NullText="Select a date..."></DxDateEdit>

### Response

**Marin Bratanov** answered on 23 Feb 2021

Hi Tim, You can Follow the implementation of this feature here: [https://feedback.telerik.com/blazor/1452940-placeholder-for-datepicker-and-the-other-date-inputs.](https://feedback.telerik.com/blazor/1452940-placeholder-for-datepicker-and-the-other-date-inputs.) I've added your Vote on your behalf so that it raises its priority. Clicking the Follow button will send you emails when it gets updated so you can upgrade to the corresponding version that will contain the feature. The thread also contains a couple of ideas that can serve as workarounds. Regards, Marin Bratanov

### Response

**Tim** answered on 23 Feb 2021

Marin, based on your link, this doesn't look like it will be fixed anytime soon. Sorry for being harsh, but please tell me in what scenario a user would like to see a "f" or "d" in the date field? Why would you have ever designed a control like that in the first place? W\e are moving over to Syncfusion. A simple thing like this costs you $$$ in licenses and renewals.

### Response

**Marin Bratanov** answered on 23 Feb 2021

Hello Tim, You don't have to use a shorthand format string like "f" or "d" that makes no sense to the user, you can use something that does - such as "HH:mm:ss", for example. As for why a feature is not available yet - it is simply because we have to prioritize - it is not possible to create native components from the ground up and, in less than two years, have them have the same feature sets as component suites that have been on the market for a decade or more. We listen very actively to the feedback from our community and we've changed our roadmap many times to reflect the demand we see for certain features. So far, this has not been one of them, and while I agree it would be a great addition, there are a couple of easy workarounds that you can employ without significant effort. Regards, Marin Bratanov

### Response

**Tim** answered on 23 Feb 2021

"HH:mm:ss" doesn't make any sense to the user either. These are users, not developers. A typical user wants to see a blank field or if a default is needed a real date. Not some .NET format string. Yikes. This is a simple fix for you, it doesn't impede your roadmap or development cycle. Please. Start making HTML controls, not these nightmare, abstracted away controls. placeholder="". HTML STANDARDS!!!!!! Please spend a minute going throughout the internet, visit any legitimate, popular website (Apple, Google, Airbnb, etc) and find a date/time field. Show me one that has this "HH:mm:ss" gibberish in the field. Your product managers are failing you and costing you thousands in licenses. Trust me.

### Response

**Marin Bratanov** answered on 23 Feb 2021

We keep adding a ton of features to our component suite, and there is much more compared to 4 months ago when your trial ended (and there will be a massive update on the InCell editing of the grid by the end of this week) and I'd encourage you to give them a try, even if this particular feature is not among them. If you are not willing to, I'll be truly sorry to see you go again, Tim. Regards, Marin Bratanov
