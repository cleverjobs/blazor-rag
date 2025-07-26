# Ignore forward slash, allow various formats when using date input

## Question

**EliEli** asked on 24 May 2021

I have a common scenario that my users complain about and find annoying. 1) I have a DatePicker with format of M/d/yyyy 2)They click in and (for example) quickly type 2/20/2021 expecting that to be the date, instead as soon as they hit the forward slash it jumps to the year and leaves them with 2/d/0020 3) In an attempt to fix it the user will press backspace to delete a character but that clears it all and leaves the yyyy highlighted, forcing them to stop their workflow and click back to the start and be careful not to mess anything up This is not very user friendly. Reproducible here: Blazor DatePicker Demos - Overview | Telerik UI for Blazor I and our users much prefer what they are used to in your Telerik Ajax tools that pops open the calendar when focusing on the box and will allow for free flow typing of a date, allowing a variety of formats on the fly and verify on leaving the field. [https://demos.telerik.com/aspnet-ajax/datepicker/overview/defaultcs.aspx](https://demos.telerik.com/aspnet-ajax/datepicker/overview/defaultcs.aspx) Are there any workarounds or should a feature request be submitted?

## Answer

**Svetoslav Dimitrov** answered on 27 May 2021

Hello Eli, I am sorry to see that the built-in component behavior is giving you a hard time. When we evaluate the input of a date we take into account two things The date itself And if the separator is typed in. The separator is dependant on the provided date format in the Format parameter (for example it might be forward-slash (/), comma (,) or a full-stop (.). The way the input focuses on the next date segment is By typing a valid value, in the below examples I would take the Month segment as a base Typing two (2) the input will automatically focus on the next segment singe there are no months with two digits that start with 2 Typing one (1) the input will allow the user to type another digit as there are months with two digits that start with 1 - 10, 11, 12 If the user would like to select January (1) he can either type 01, or 1 and tap on the separator or the right/left keyboard arrow By tapping on the separator or clicking on the right/left keyboard arrow That being said, this behavior is implementing in order to provide quick typing. If the format is M/d/yyyy the use can type 2252021 and the component will format it automatically to a valid DateTime object - 2/25/2021. The reason why we decided to take into account when user inputs in the separator is for the cases where they would like to enter a single digit month that starts with 1 as an alternative to the left/right keyboard arrow. Taking into account the written above the behavior of the component is expected to remain the same and is not on the line for changes. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Eli** commented on 27 May 2021

Thank you for the reply. I can understand why some decisions were made, but this is inconsistent across your products. ASP.NET Core works the way I prefer: [https://demos.telerik.com/aspnet-core/dateinput,](https://demos.telerik.com/aspnet-core/dateinput,) As does Kendo React: [https://www.telerik.com/kendo-react-ui/components/dateinputs/dateinput/](https://www.telerik.com/kendo-react-ui/components/dateinputs/dateinput/) in addition to the Telerik Ajax tools I already stated. I did not see any of the Telerik frameworks behave as Blazor components do. I will use the built in InputDate going forward (which also performs in our preferred way) even though it lacks in other areas.

### Response

**Svetoslav Dimitrov** commented on 28 May 2021

Hello Eli, To take advantage of the feature the TelerikDatePicker offers above the built-in InputDate you can use it with a format separated with space - for example, Format="M d yyyy". If you set this as a format when the users click on the forward-slash our component will not automatically focus on the next date segment. Let me know if this is a suitable solution for your application.

### Response

**Eli** commented on 28 May 2021

That works in principal but ultimately as soon as I implement something like that I will be questioned by users on why it is not showing the slashes in the edit display. I will use InputDate component or use a text box and have it validate the date when moving focus. At some point I may add a Feature Request to simply ignore format string and allow free edit and then validate to the format string on exit.

### Response

**Svetoslav Dimitrov** commented on 01 Jun 2021

Hello Eli, We added an Efficient Keyboard Input section in the Overview article for the DateInput component. It uses the information from my answer above and extends on it. You can take a look at it to get a better perspective on our decision of UX.

### Response

**Mike** commented on 15 Feb 2022

I would just like to second Eli's issue. The format you have chosen is very inconsistent and jarring to users who are used to entering dates with separators. I understand the convenience of not having to enter them, but most users I have come across enter the separators. There isn't a way to do both? Couldn't you have logic like the following (assumming M/D/YYYY here): The user enters a 2-9 in the month and you automatically move to the day. If the user is on the first day digit and they hit slash, period or comma, then just ignore it and stay where you are. If they enter a 0, 1, 2 or 3 in the first day digit, then stay in the day section. If they enter a different number in the first day digit, then automatically move to the year. If a separator value key is hit after #3 (above) then move to the year. If the separator value key is hit after #4 (above) then just stay in the first digit of the year. I would think this methodology would handle both scenarios for people that do enter in the separators as well as those that just want to type the numbers. What you have now is less intuitive, because even the people that don't want to type in the separators would still need to under some circumstances, unless they always type 2 digit months and 2 digit days (02/05/2022).

### Response

**Svetoslav Dimitrov** commented on 18 Feb 2022

Hello Mike, I read through your suggestions carefully and I would like to say that this is mostly the current way the DateInput behaves. Let me provide some examples: Let's take the M/d/yyyy as a date format: If you type 2-9 in the month segment the DateInput will automatically focus on the next date segment, in this case, the day If the user types 4-9 in the day segment the DateInput will automatically focus on the year segment. If the user types 0-3 the focus will remain in the day segment until the second digit is typed in. If a separator is hit the DateInput will automatically focus on the next date segment. I think that this behavior is the expected and the expected UX of the component. Let me know of your feedback.

### Response

**Mike** commented on 18 Feb 2022

I think you may be missing what this post is trying to say. I get that your control mostly does what I'm suggesting. The issue is in my #2 step. Right now when a user hits a 2-9 and it advances to the day segment if the user then hits the / key it takes them to the year segment skipping over the day segment altogether. What I'm proposing is alter your functionality slightly, so that if the user hits a / when they are at the beginning of the day segment, stay where you are. The way it works now, it is great for those that know enough not to hit the slash key, but most users are going to type that / key, and it ends up throwing them off, and having to go back and re-type things in because all of a sudden they have jumped to the year, accidentally entered in the day, and then realized it was wrong. This actually makes the control less productive. And while this is an annoyance for a sighted user, for a blind user with a screen reader it becomes unusable because there is no cue for them that they have moved to the next section, so the only way to tell is if they tab out, and then tab back in for it to read the date back to them. By tweaking the input method a bit so you handle those that choose to type the full date in, you can save a lot of headaches, and make it more user friendly and accessible for screen readers.

### Response

**Eli** commented on 18 Feb 2022

Mike is exactly right. The problem is in a user typing slash (after 2-9) causing the control to leave a empty section of date and go to the year. Auto jumping to the second segment is fine, but if that happens and then if a slash is entered prior to any input, it should stay and not leave an empty section of date.

### Response

**Svetoslav Dimitrov** commented on 23 Feb 2022

Hello Eli and Mike, There are two main scenarios that each date input component can cover: Quick typing - Allow the users of the component to type continuously input integers until a valid date is fully input. For example, type 2252022 would automatically generate the 25th of February 2022. This is the current approach that the Telerik Date inputs for Blazor have taken. Normal typing - This would require the users to manually type the separators between the different date segments. Typing 2252022 would not result in a valid date, but the component would be stuck on the Month segment, given that the M/d/yyyy format is selected. Typing 2 would result in 2/d/yyyy, the second 2 would bring the same result, the third integer would result in 5/d/yyyy. A valid date input would be 2/25/2022, or other separators based on the specific application culture. These two different ways to input dates would not be able to be mixed together as there would be inconsistent UX behavior and too many formats to be covered by the component. This would only complicate if we refer to the DateTimePicker where time should be input too. To achieve the desired custom behavior of the Date input components I would suggest you take a look at the source code for the Telerik UI for Blazor and modify it to suit the needs of your application.

### Response

**Eli** commented on 23 Feb 2022

Thank you. We were/are users of your AJAX and Core controls for a long time and they had chosen #2 method. I understand sometimes change is necessary. Last point that may be helpful to Mike, I use the built in InputDate rather than Telerik version at this point. It is able to handle #1 and #2 scenarios seamlessly. "2252002","2/25/2022","02/25/2022" all produce the desired date in the control. [https://blazorrepl.telerik.com/QmEQGdln57FaEEY711](https://blazorrepl.telerik.com/QmEQGdln57FaEEY711)

### Response

**Mike** commented on 23 Feb 2022

Hi Eli, I ended up rolling my own control. It requires entering the date with slashes, but my main requirement for my project is accessibility, and the Telerik control is just not feasible for screen reader users. Unfortunately, I'm finding this issue for a lot of the Telerik controls. While they provide keyboard support, and that's great, they just aren't informing screen readers where they are in within the control and they become unusable. I'm hoping that more of a push is made towards making all of the controls more accessible. That being said, the InputDate control has its own set of accessibility issues with the datepicker portion of the built in control, so I'm not able to use that either. Also, I also want to point out that in your sample while the 2/25/2022 date works with all 3 scenarios, it doesn't work for 2/2/2022. It doesn't take the / as a valid key so it doesn't move past the day section and will write the first 2 from 2022 in the day making it 2/22/022. Just an FYI.

### Response

**Eli** commented on 23 Feb 2022

Good to know, thank you!

### Response

**Svetoslav Dimitrov** commented on 28 Feb 2022

Hello Mike, Could you open a support ticket for the accessibility issues in the DateTimePicker? I am asking that because we are currently not aware of those issues and we would like to provide fixes for them as accessibility is a big topic in our components. Best regards, Svetoslav

### Response

**Mike** commented on 28 Feb 2022

I've opened a bug report for this at the following link: [https://feedback.telerik.com/blazor/1555604-nvda-screen-reader-issues-with-datepicker-control](https://feedback.telerik.com/blazor/1555604-nvda-screen-reader-issues-with-datepicker-control) Thanks, Mike

### Response

**Joana** commented on 03 Mar 2022

Mike, thank you for openning a separate thread for the accessibility of the component. We will look into it and continue the conversation there on this matter.

### Response

**Joana** commented on 23 Mar 2022

Hello everyone, Me and my colleague Svetoslav continued an internal conversation and research on the user experience and demand. We have opened a feature request about the configuration of the auto tab behavior. You can track the progress below: [https://feedback.telerik.com/blazor/1558915](https://feedback.telerik.com/blazor/1558915)
