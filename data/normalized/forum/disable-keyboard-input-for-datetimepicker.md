# Disable Keyboard Input for DateTimePicker

## Question

**Dus** asked on 19 Jan 2023

On mobile you dont really want to change the DateTime with Keyboard. Is it possible to disable this feature because we develop a Maui Blazor Hybrid.

## Answer

**Nadezhda Tacheva** answered on 24 Jan 2023

Hi Dustin, By default, the keyboard navigation is enabled in the DateTimePicker to allow accessibility coverage. For those who are unable to use a mouse, a keyboard is the primary method for navigation. We do have a feature request for allowing the customization of the default keyboard shortcuts. We gather feedback on the needed customization including disabling the navigation for specific components. I already added your request to the internal item. You may additionally vote for and follow the public request. For mobile usage, however, the keyboard navigation is not really applicable. So, whether or not is disabled should not be an issue. May I ask you to share some more details on the use case, your concerns and why it is needed to disable the keyboard navigation? Does it cause any problems on your side? Regards, Nadezhda Tacheva Progress Telerik

### Response

**Dustin** commented on 25 Jan 2023

Hi Nadezhda, Thank you for the detailed answer. Yes it does cause problems while using the App whenever the user tabs "set" or "cancel" the Keyboard opens. This causes problem with usability in our scenario especially when it is not clear why the Keyboard opens (for example the Picker is hidden by Keyboard) Kind regards Dustin

### Response

**Nadezhda Tacheva** commented on 27 Jan 2023

Hi Dustin, I'd like to share some more details on the matter to provide more clarity. The keyboard navigation feature provides the users with a fast keyboard-only navigation capability and is also part of the web accessibility features - it enables users with disabilities to fully control their website or app access through the keyboard. This functionality introduces predefined key commands that will perform a specific action in the component - you may check the list here: [https://demos.telerik.com/blazor-ui/datetimepicker/keyboard-navigation.](https://demos.telerik.com/blazor-ui/datetimepicker/keyboard-navigation.) The keyboard navigation, however, does not control when the mobile keyboard will be shown. By default, the mobile keyboard appears when there is focused input on the page, so the user can start typing. What essentially happens when the user presses the "Set" or "Cancel" buttons is that the focus is moved to the input - once the input is focused, the mobile keyboard appears. I hope you will find this information useful. Please let us know if any further questions appear.
